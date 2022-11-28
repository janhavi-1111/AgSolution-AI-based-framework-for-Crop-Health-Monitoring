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

    <title>Weather</title>
</head>
<body>
<style>
        p {text-align: center;}
    </style>
    <form action="weather_trial1.php" method="get">
        <p>
        Enter city:<br>
        <input name="city"><br>

        <button class="btn btn-primary" type="submit">Submit</button>
</p>
    </form>
    
    
</body>
</html>