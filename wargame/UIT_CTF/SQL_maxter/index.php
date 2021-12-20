<?php
include 'config.php';
include 'waf.php';

$heroname = $_POST['heroname'] ?? NULL;
$mission = $_POST['mission'] ?? NULL;

if(preg_match($waf, $heroname))
{
    die("Wrong way h4ck3r");
}

$hero  = "SELECT * FROM heroes WHERE name = '{$heroname}'";
$result = $mysqli->query($hero);

$enemy = "SELECT power FROM heroes WHERE name='boros'";
$enemy__power = $mysqli->query($enemy);

if ($result-> num_rows === 1) {
    $hero__info = $result->fetch_array();
    $enemy__power = $enemy__power->fetch_array();
    if ($hero__info['mission'] == $mission || $hero__info['power'] > $enemy__power['power']) {
        die($flag);
    } else {
        die("Mission failed");
    }
} else {
    die("Mission failed!!!");
}
?>