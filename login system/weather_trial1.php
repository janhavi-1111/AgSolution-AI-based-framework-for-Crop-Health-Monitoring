<?php
require 'partials/nav2.php';
$a=$_GET['city'];
#echo $a;
echo "<br>";
echo shell_exec("python weather.py $a");

?>