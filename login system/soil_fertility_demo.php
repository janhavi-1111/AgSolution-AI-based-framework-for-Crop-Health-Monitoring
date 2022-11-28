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

    <title>Soil fert</title>
</head>
<body>
<style>
        p {text-align: center;}
    </style>
    <form action="soil_fertility_demo1.php" method="get">
        <p>
        Enter pH:<br>
        <input name="pH"><br>
        Enter EC:<br> 
        <input name="EC"><br>
        Enter OC:<br> 
        <input name="OC"><br>
        Enter OM:<br> 
        <input name="OM"><br>
        Enter N:<br>
        <input name="N"><br>
        Enter P:<br> 
        <input name="P"><br>
        Enter K:<br> 
        <input name="K"><br>
        Enter Zn:<br>
        <input name="Zn"><br>
        Enter Fe:<br> 
        <input name="Fe"><br>
        Enter Cu:<br> 
        <input name="Cu"><br>
        Enter Mn:<br>
        <input name="Mn"><br>
        Enter Sand:<br> 
        <input name="Sand"><br>
        Enter Silt:<br> 
        <input name="Silt"><br>
         Enter Clay:<br>
        <input name="Clay"><br>
        Enter CaCO3:<br> 
        <input name="CaCO3"><br>
        Enter CEC:<br> 
        <input name="CEC"><br><br>                    
        <button class="btn btn-primary" type="submit">Submit</button>
        </p>
    </form>
    
    
</body>
</html>