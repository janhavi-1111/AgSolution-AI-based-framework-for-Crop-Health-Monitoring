<!DOCTYPE html>
<html lang="en">
<?php
require 'partials/nav2.php';?>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Crop Rec</title>
</head>
<body>
<style>
        p {text-align: center;}
    </style>
    <form action="prod_demo1.php" method="get">
        <p>
        Enter State_Name:<br>
        <input name="state"><br><br>
        Enter District_Name:<br> 
        <input name="dis"><br><br>
        Enter Crop_Year:<br> 
        <input name="year"><br><br>
        Enter Season:<br> 
        <input name="seas"><br><br>
        Enter Crop:<br> 
        <input name="crop"><br><br>      
        Enter Temperature:<br> 
        <input name="temp"><br><br>                            
        Enter humidity:<br> 
        <input name="hum"><br><br>
        Enter Soil_Moisture:<br> 
        <input name="soil"><br><br>     
        Enter area:<br> 
        <input name="area"><br><br>  

        <button class="btn btn-primary" type="submit">Submit</button>
</p>
    </form>
    
</body>
</html>