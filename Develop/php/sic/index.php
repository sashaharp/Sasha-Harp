<?php
    session_start();
    $loggedin = false;
	$conn = new PDO("mysql:host=localhost;dbname=sicDB", "root");
	$stmt = $conn->prepare("SELECT pwd FROM users WHERE id = :id");
	if(isset($_GET['logout'])) {
		unset($_SESSION['uname']);
		unset($_SESSION['pwd']);
	}
	if (isset($_SESSION['uname'])) {
        $stmt->bindParam(":id", $_SESSION['uname']);
		$stmt->execute();
		$result = $stmt->fetch();
		if(password_verify($_SESSION['pwd'], $result[0])) {
			$loggedin = true;
		} else {
			unset($_SESSION['uname']);
			unset($_SESSION['pwd']);
			header('Location: index.php');
		}
    } else if (isset($_POST['username'])) {
        $id = md5($_POST['username']);
		$stmt->bindParam(":id", $id);
		$stmt->execute();
		$result = $stmt->fetch();
		if(password_verify(md5($_POST['password']), $result[0])) {
			$_SESSION['uname'] = $id;
			$_SESSION['pwd'] = md5($_POST['password']);
			$loggedin = true;
		} else {
			header('Location: index.php');
		}
    } else if (!$loggedin) {
		?>
		<html>
			<head><title>Dictionary</title></head>
			<body>
				<form action="index.php" method="POST">
					username: <input type="text" name="username"><br />
					password: <input type="password" name="password"><br />
					<input type="submit" value="login">
				</form>
			</body>
		</html>
		<?php
    } 
    if ($loggedin) {
        ?>
		<html>
			<head><title>Dictionary</title></head>
			<body>
				<p>hello</p>
			</body>
		</html>
		<?php
    }
?>