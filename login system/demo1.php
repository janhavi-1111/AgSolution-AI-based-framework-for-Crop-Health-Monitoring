<?php
require 'partials/nav2.php';
$a=$_GET['n'];
$b=$_GET['p'];
$c=$_GET['k'];
$d=$_GET['temp'];
$e=$_GET['hum'];
$f=$_GET['pH'];
#echo $a," ", $f;
echo "<br>";
echo shell_exec("python cropR.py $a $b $c $d $e $f");

?>