
<?php
if(isset($_POST["submit"])) {
    $target_file =$_FILES["file"]["tmp_name"];
    $xml=file_get_contents($target_file);
    $dom = new DOMDocument();
    $dom->loadXML($xml, LIBXML_NOENT | LIBXML_DTDLOAD);
    $creds = simplexml_import_dom($dom);
    $user = $creds->user;
    $year = $creds->year;
    echo "<h1>H3R3 1s wh4t y0u 45k3d f0r : </h1><br><h1>This ch4d was <br>$user</br> from year :<br>$year<br></h1>";
}