<?php
require 'partials/nav2.php';
$a=$_GET['state'];
$b=$_GET['dis'];
$c=$_GET['year'];
$d=$_GET['seas'];
$e=$_GET['crop'];
$f=$_GET['temp'];
$g=$_GET['hum'];
$h=$_GET['soil'];
$i=$_GET['area'];
#echo $a," ", $i;
echo "<br>";
echo shell_exec("python Crop_Production_Prediction_Model.py $a $b $c $d $e $f $g $h $i");
?>