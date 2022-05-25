<?php

require_once "db.php";

// Initialize the session
session_start();


// Check if the user is logged in, otherwise redirect to login page
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
  header("location: login.php");
  exit;
}


$username = $_SESSION["username"];
$target_dir = "/var/www/html/uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$message = "";
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

$bad_extensions = ["php", "phtml", "pht"];
$sql_query = "SELECT username FROM fileupload_users WHERE username = ? AND staff = 0x1;";
if ($sql_statement = mysqli_prepare($database_connection, $sql_query)) {
  mysqli_stmt_bind_param($sql_statement, "s", $username);
  mysqli_stmt_execute($sql_statement);
  $result = "";
  mysqli_stmt_bind_result($sql_statement, $result);
  mysqli_stmt_fetch($sql_statement);
  if ($result === '') {
    $message = "Only staff users can upload data right now. Sorry.";
    $uploadOk = 0;
    mysqli_close($database_connection);
    goto render;
  }
  mysqli_close($database_connection);
} else {
  $message = "Not logged in";
  $uploadOk = 0;
  goto render;
}


// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
  $uploadOk = 0;
  $message = "Sorry, your file is too large.";
  goto render;
}

// Allow certain file formats
foreach ($bad_extensions as $bad) {
  if (str_contains($imageFileType, $bad)) {
    $message = "Please only upload images files. Any hacking attempts will be reported.";
    $uploadOk = 0;
    goto render;
  }
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 1) {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    $message = "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded.";
    // Open file and check for <? 
    $uploaded_file = fopen($target_file, "r") or die("Unable to open file!");
    $file_content = fread($uploaded_file, filesize($target_file));
    fclose($uploaded_file);
    if (str_contains($file_content, '<?')) {
      // If found write this to the log for later reporting
      error_log("Some hackers tried to upload code to our server. Pls check if we were compromised");
      // Overwrite the offending file with a warning to the hackers.
      $uploaded_file = fopen($target_file, "w");
      fwrite($uploaded_file, "Nice try hackers!");
    }
  } else {
    $message = "Sorry, there was an error uploading your file.";
  }
}

render:

?>

<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" href="favicon.ico">

  <title><?php echo $SITE_NAME ?> - Index</title>

  <!-- Bootstrap core CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">

  <link href="css/custom.css" rel="stylesheet">

</head>

<body>

  <div class="jumbotron">
    <div class="container custom-container">
      <h1>Upload result</h1>
    </div>
  </div>
  <div class="container">
    <main role="main">
      <div class="container">
        <?php
        if ($uploadOk == 1) {
          ?>
          <div class="alert alert-success" role="alert">
            <?php echo $message ?>
          </div>
          <?php
        }
        else {
          ?>
          <div class="alert alert-danger" role="alert">
          <?php echo $message ?>
        </div>
        <?php
        }
        ?>
      </div>
    </main>

  </div>
  <br><br>

  <footer class="container">
    <p>&copy; <?php echo $SITE_NAME ?> 2022</p>
  </footer>

  <!-- Bootstrap core JavaScript
    ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script>
    window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')
  </script>
  <script src="js/vendor/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
</body>

</html>