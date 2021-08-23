<?php
session_start();
include_once("config.php");
if (isset($_SESSION['username'])) {
	$stmt = $conn->prepare('select * from users where username=?');
	if (!$stmt)
		throw new Exception("prepare query error:" . $conn->error);
	$stmt->bind_param('s', $_SESSION['username']);
    $stmt->execute();
    $result = $stmt->get_result();
    $data = [];
    while ($row = $result->fetch_assoc()) {
    	$data[] = $row;
	}
} else {
	header("Location: login.php");
}
?>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title></title>
	<link rel="stylesheet" href="">
</head>
<body>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Web-vkl CTF</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/index.php">Home</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="/flag.php">FLAG</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="/donate.php">Donate</a>
      </li>
    </ul>
  </div>
</nav>
<div class="container">
    <div class="row">
        <div class="col-xs-12 col-sm-6 col-md-6">
            <div class="well well-sm">
                <div class="row">
                    <div class="col-sm-6 col-md-4">
                        <img src="http://placehold.it/380x500" alt="" class="img-rounded img-responsive" />
                    </div>
                    <div class="col-sm-6 col-md-6">
                    	<?php if($data): ?>
                    		<?php foreach($data as $row): ?>
                    			<h1><b>Name: </b><?= $row['username'] ?></h1>
                    			<h3><b>Star: </b><?= $row['star'] ?></h3>
                    			<h3><b>Status: </b><?= $row['status'] ?></h3>
                    		<?php endforeach ?>
    					<?php else: ?>
    						No data found
    					<?php endif ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>