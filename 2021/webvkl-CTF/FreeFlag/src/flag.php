<?php
session_start();
?>
<!DOCTYPE html>
<html>
<head>
  <title>Web VKL</title>
  <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <style>
    * {
  font-family: sans-serif; /* Change your font family */
}

.content-table {
  border-collapse: collapse;
  margin: 70px 50px;
  width: 90%;
  font-size: 1.0em;
  min-width: 400px;
  border-radius: 5px 5px 0 0;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.content-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
  font-weight: bold;
}

.content-table th,
.content-table td {
   max-width: 55px;
  text-align:justify;
  word-break:keep-all;
  padding: 12px 15px;
}

.content-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.content-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.content-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.content-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}

.header {
  text-align: center;
  position: relative;
  margin: 50px auto;
}
h2 {
  font-family: arial;
  color: #333;
  font-size: 40px;
  text-align: center;
  margin: 0 30px;
  text-transform: uppercase;
}
span {
  display: inline-block;
  position: absolute;
  background: #faa;
  height: 3px;
  left: 50%;
}
span.top {
  width: 70px;
  top: 20px;
}
span.bottom {
  width: 120px;
  top: 35px;
}
span.left {
  transform: translateX(-350px);
}
span.bottom.left {
  transform: translateX(-400px);
}
span.right {
  transform: translateX(280px);
}

</style>
</head>
<body>
  
  <div class="header">
  <span class="top right"></span>
  <span class="top left"></span>
  <h2>Web VKL</h2>
  <span class="bottom right"></span>
  <span class="bottom left"></span>
  <form method="GET">
  <input type="numer" name="id" style="margin-top: 5%;" placeholder="ID">
  <button type="submit">Search</button>
  </form>
  <!-- ?source -->
</div>

  <table class="content-table">
  <thead>
    <tr>
      <th>ID</th>
      <th>FLAG NAME</th>
      <th>FLAG FAKE</th>
    </tr>
    </thead>
    <tbody>
<?php
include_once("config.php");
if (isset($_SESSION["admin"]) && $_SESSION["admin"] === true) {
  if (isset($_GET['id'])) {
    $id = $_GET['id'];
    if (preg_match("/insert|substr|mid|left|right|ord|chr|sys|pi|rand|0x|version|concat|ascii|convert|and|or|procedure|xml|extract|by|create|like|sleep|if|case|db|load|to|count|where|column|in|[1-9`~.^\-\/\\\=<>|$*]/i",$id) || substr_count($id,'0') > 1) {
      die("no hack");
    } else {
      $query = "SELECT id,flag_name,flag_fake FROM flag WHERE id={$id};";
      $result = $conn->query($query);
      while ($row = $result->fetch_assoc()) {
        echo "<tr><th>".$row['id']."</th><th>".$row['flag_name']."</th><th>".$row['flag_fake'];
      }
    }
  }
  if(isset($_GET['ai_di'])) {
    $ai_di = $_GET['ai_di'];
    if (preg_match("/insert|substr|mid|left|right|ord|chr|sys|pi|rand|0x|version|concat|ascii|convert|and|or|procedure|xml|extract|by|create|like|sleep|if|case|db|load|to|count|where|column|in|[2-9`~.^\-\/\\\=<>|$]/i",$ai_di) || substr_count($ai_di,'1') > 1 || substr_count($ai_di,'0') > 2) {
      die("hack ghe vay bro ?");
    } else {
      $query = "SELECT id,flag_name,flag_fake FROM flag WHERE id={$ai_di};";
      $result = mysqli_query($conn,$query);
      if (!$result) {
        echo mysqli_error($conn);
      } else {
        echo "nice!";
      }
    }
  }
} else {
  die("no admin");
}
if (isset($_GET['source'])) {
  readfile("flag.php");
}
?>
</tbody>
</table>
</body>
</html>