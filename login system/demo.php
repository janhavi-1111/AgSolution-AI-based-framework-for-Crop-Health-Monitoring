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
    <form action="demo1.php" method="get">
       <p> Enter N:<br>
        <input name="n"><br><br>
        Enter P:<br> 
        <input name="p"><br><br>
        Enter K:<br> 
        <input name="k"><br><br>
        Enter Temperature:<br> 
        <input name="temp"><br><br>
        Enter Humidity:<br> 
        <input name="hum"><br><br>                        
        Enter pH:<br> 
        <input name="pH"><br><br>
                      
        <button class="btn btn-primary" type="submit">Submit</button></p>
    </form>
    
    
</body>
</html>