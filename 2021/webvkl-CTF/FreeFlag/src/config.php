<?php
    $server = 'mysql8';
    $username = 'root';
    $password = 'f7e63b54818c243e2cd34a4e3edd5127';
    $db = 'main';
    $conn = new mysqli($server, $username, $password, $db);
    if($conn->connect_error){
        die("connect_error: " . $conn->connect_error);
    }
?>