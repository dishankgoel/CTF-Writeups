<?php
define('DB_SERVER', 'mysql');
define('DB_USERNAME', 'user');
define('DB_PASSWORD', 'VerySafePassword1337');
define('DB_NAME', 'fileuploadplatform');

$SITE_NAME = "File Upload";

$database_connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME, 3306);

if($database_connection === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

?>
