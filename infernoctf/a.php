<?php
class user {
    var $name;
    var $pass;
    var $secret;
}


$a = new user();

$a->name = 'admin';
$a->pass = &$a->secret;
echo serialize($a);



?>