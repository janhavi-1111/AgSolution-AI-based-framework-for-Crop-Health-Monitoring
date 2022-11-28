<?php
require 'partials/nav2.php';
$a=$_GET['pH'];
$b=$_GET['EC'];
$c=$_GET['OC'];
$d=$_GET['OM'];
$e=$_GET['N'];
$f=$_GET['P'];
$g=$_GET['K'];
$h=$_GET['Zn'];
$i=$_GET['Fe'];
$j=$_GET['Cu'];
$k=$_GET['Mn'];
$l=$_GET['Sand'];
$m=$_GET['Silt'];
$n=$_GET['Clay'];
$o=$_GET['CaCO3'];
$p=$_GET['CEC'];
#echo $a," ", $p;
echo "<br>";
echo shell_exec("python Soil_FertilityPrediction_Model.py $a $b $c $d $e $f $g $h $i $j $k $l $m $n $o $p");

?>