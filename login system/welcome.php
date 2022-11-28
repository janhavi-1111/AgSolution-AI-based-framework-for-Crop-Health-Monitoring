

<?php
session_start();

if(!isset($_SESSION['loggedin']) || $_SESSION['loggedin']!=true){
    header("location: login.php");
    exit;
}


?>
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">


    <!-- Bootstrap CSS -->
    <style>
body {
  background-image: url('farm.jpg');
}
</style>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Welcome - <?php $_SESSION['username']?></title>
</head>
<style> 
/*body {
  background-image: url("farm.png");
  background-repeat: no-repeat, repeat;
  background-color: #cccccc;
}*/
h1 {
  font-size: 40px;
}
h2 {
  font-size: 30px;
}
h3 {
  font-size: 20px;
  white-space: pre;
}

</style>

<body>


<?php require 'partials/nav1.php';
include 'partials/_dbconnect.php';
$query = "SELECT * FROM `users`";
$result = mysqli_query($conn, $query);?>

<h1><div style="color:White;">Welcome - <?php echo $_SESSION['username']?></h1>
    </div>
      <div style="color:White; font-size:30px;">Crop Prediction System using Machine Learning</div>
   <h2><div style="color:White;">Information</div></h2>
   <h4><div style="color:White;"><p>A large population and rising urban and rural income is driving the demand. External demand is driving export from agriculture sector</p></div></h4>
      <br>
      <h4><div style="color:White;"><p>Demand for agricultural inputs such as hybrid seeds and fertilizers and allied services like warehousing and cold storages is increasing in India at a fast pace.</p></div></h4>
            </div>
           
            <!--<div class="svgs">
        <img src="imgs/bg_svg.svg"></div> -->
       


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br><br>

<!-- Footer -->
<footer class="text-center text-lg-start bg-light text-muted">
  
  
  <!-- Section: Social media -->
  <section
    class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom"
  >
  
    <!-- Left -->
    <div class="me-5 d-none d-lg-block">
      <span></span>
    </div>
    <!-- Left -->

    <!-- Right -->
    
    <!-- Right -->
  </section>
  <!-- Section: Social media -->

  <!-- Section: Links  -->
  <section class="">
    <div class="container text-center text-md-start mt-5">
      <!-- Grid row -->
      <div class="row mt-3">
        <!-- Grid column -->
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <!-- Content -->
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3"></i>  Developed By 
          </h6>
          <ul>
                    Govind Kotecha 
                    <br>   
                    Paras Shah
                    <br>
                    Nandini Dubbe
                    <br>
                    Janhavi Chavhan
                    <br>
                    </ul>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        
        <!-- Grid column -->

        <!-- Grid column -->
        
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Contact
          </h6>
          <p><i class="fas fa-home me-3"></i> MITWPU</p>
          <p>
            <i class="fas fa-envelope me-3"></i>
            paras@gmail.com
          </p>
          <p><i class="fas fa-phone me-3"></i> + 01 234 567 88</p>
          <p><i class="fas fa-print me-3"></i> + 01 234 567 89</p>
        </div>
        <!-- Grid column -->
      </div>
      <!-- Grid row -->
    </div>
  </section>
  <!-- Section: Links  -->

  <!-- Copyright -->
  <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2022 Copyright:
    <a class="text-reset fw-bold" href="">MITWPU</a>
  </div>
  <!-- Copyright -->
</footer>
<!-- Footer -->

<?php




//include 'partials/_dbconnect.php';
/* echo 'ID'.' '.'Username'.' '.'Password'.' '.'Email'.'<br>';
$query = "SELECT * FROM `users`";

if ($is_query_run = mysqli_query($conn,$query))
{
// echo "Query Executed";
// loop will iterate until all data is fetched
while ($query_executed = mysqli_fetch_assoc ($is_query_run))
{
// these four line is for four column
//echo $query_executed['sno'].' ';
echo $query_executed['username'].' ';
echo $query_executed['password'].'<br>';
echo $query_executed['email'].' ';
}
}
else
{
echo "Error in execution";
}*/
?>


<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>  
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />  
           <script src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>  
           <script src="https://cdn.datatables.net/1.10.12/js/dataTables.bootstrap.min.js"></script>            
           <link rel="stylesheet" href="https://cdn.datatables.net/1.10.12/css/dataTables.bootstrap.min.css" />  


</body>
</html>

<script>  
 $(document).ready(function(){  
      $('#employee_data').DataTable();  
 });  
 </script>  

