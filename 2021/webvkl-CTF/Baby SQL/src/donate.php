<?php
session_start();
include_once("config.php");
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
}
if (isset($_POST['send'])) {
    $name = $_POST['name'];
    $star = $_POST['star'];
    // check status
    $stmt = $conn->prepare('select status from users where username=?');
    if (!$stmt)
        throw new Exception("prepare query error:" . $conn->error);
    $stmt->bind_param('s', $name);
    $stmt->execute();
    $result = $stmt->get_result();
    $checkStatus = 0;
    while ($row = $result->fetch_assoc()) {
        $checkStatus = $row['status'];
    }
    // donate
    if ($checkStatus === 0 && $star <= 20) {
        // var_dump($checkStatus);
        $stmt1 = $conn->prepare('update users set star = star + ? where username=?');
        if (!$stmt1)
            throw new Exception("prepare query error:" . $conn->error);
        $stmt1->bind_param('is', $star, $name);
        $stmt1->execute();

        sleep(2);
        $stmt2 = $conn->prepare("update users set star = star - ? where username=?");
        if (!$stmt2)
            throw new Exception("prepare query error:" . $conn->error);
        $stmt2->bind_param("is", $star, $_SESSION['username']);
        $stmt2->execute();
        // set status
        sleep(2);
        $stmt3 = $conn->prepare("update users set status = 1 where username=?");
        if (!$stmt3)
            throw new Exception("prepare query error:" . $conn->error);
        $stmt3->bind_param("s", $name);
        $stmt3->execute();
        echo "<script>alert('Donate Success!');</script";

    }
    else {
        echo "<script>alert('ineligible account :(');</script>";
    }
}
?>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Fonts -->
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Raleway:300,400,600" rel="stylesheet" type="text/css">

    <link rel="stylesheet" href="css/style.css">

    <link rel="icon" href="Favicon.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">

    <title>Web VKL</title>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light navbar-laravel">
    <div class="container">
        <a class="navbar-brand" href="#">Web VKL</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/index.php">Home</a>
                </li>
            </ul>

        </div>
    </div>
</nav>

<main class="login-form">
    <div class="cotainer">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Donate</div>
                    <div class="card-body">
                        <form action="" method="POST">
                            <div class="form-group row">
                                <label for="email_address" class="col-md-4 col-form-label text-md-right">Recipient's name</label>
                                <div class="col-md-6">
                                    <input type="text" id="name" class="form-control" name="name" required autofocus>
                                </div>
                                <label for="email_address" class="col-md-4 col-form-label text-md-right">Star</label>
                                <div class="col-md-6">
                                    <input type="text" id="star" class="form-control" name="star" required autofocus>
                                </div>
                            </div>
                            <div class="col-md-6 offset-md-4">
                                <button type="submit" class="btn btn-primary" name="send">
                                    Send
                                </button>
                            </div>
                    </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    </div>
</main>
</body>
</html>