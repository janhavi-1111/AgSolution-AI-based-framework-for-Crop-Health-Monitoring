<?php
$server = "localhost";
$username = "root";
$password = "";
$database = "users";

$conn = mysqli_connect($server, $username, $password, $database);
if (!$conn){
//     echo "success";
// }
// else{
    die("Error". mysqli_connect_error());
}

?>

<?php
//include 'partials/_dbconnect.php';
//if(isset($_POST["submit"])
if(count($_POST)>0) {
mysqli_query($conn,"UPDATE users set username='" . $_POST['username'] . "', password='" . $_POST['password'] .  "' WHERE email='" . $_POST['email'] . "'");
$message = "Record Modified Successfully";


$result = mysqli_query($conn,"SELECT * FROM users WHERE email='" . $_POST['email'] . "'");
$row= mysqli_fetch_array($result);}
?>
<html>
<head>
<title>Update Employee Data</title>
</head>
<body>
<div class="container my-4">
    <h1 class="text-center">Update</h1>
    <form action="/loginsystem/update.php" method="post">
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" name="username" aria-describedby="emailHelp">

        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" name="password">
        </div>
        <div class="form-group">
            <label for="cpassword">Confirm Password</label>
            <input type="password" class="form-control" id="cpassword" name="cpassword">
            <small id="emailHelp" class="form-text text-muted">Make sure to type the same password</small>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" name="email">
        </div>

        <button type="submit" class="btn btn-primary">Update</button>
    </form>
</div>
</body>
</html>