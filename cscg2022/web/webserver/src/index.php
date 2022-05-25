<?php
// Initialize the session
session_start();

// Check if the user is logged in, if not then redirect him to login page
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
  header("location: login.php");
  exit;
}

require_once "db.php";
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
      <h1>Upload page</h1>
      <p> Because of a hacking incident only staff accounts are allowed to upload data just now. Sorry for the inconvinience.</p>
    </div>
  </div>
  <div class="container">
    <main role="main">
      <div class="container">
        <!-- Example row of columns -->
        <div class="row">
          <form action="upload.php" method="post" enctype="multipart/form-data">
            <div class="form-group">
              <label for="file">File: </label>
              <br>
              <input type="file" name="fileToUpload" id="fileToUpload">
            </div>

            <br>
            <button type="submit" class="btn btn-primary">Upload Image</button>
          </form>
        </div>
        <div class="row">
          <a href="/logout.php">Log out</a>
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