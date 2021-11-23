<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <style>
        body {
            background-image: url("images/login.jpg");
            background-size: cover;
            background-repeat: no-repeat;
        }
        .login-box {
            width: 320px;
            height: 420px;
            background: #000;
            color: #fff;
            top: 50%;
            left: 50%;
            position: absolute;
            transform: translate(-50%,-50%);
            box-sizing: border-box;
            padding: 70px 30px;
        }
        .textbox {
            width: 100%;
            box-sizing: border-box;
            padding: 10px;
            border-bottom: 2px solid #fff;
            border-top: none;
            border-left: none;
            border-right: none;
            background: transparent;
            color: #fff;
        }
        .textbox:focus {
            outline: none;
        }
        .btn {
            width: 100%;
            background: transparent;
            border: 2px solid #fff;
            color: #fff;
            margin-top: 10px;
            border-radius: 5px;
            padding: 10px;
        }
        .fas {
            padding: 10px;
            font-size: 20px;
            color: #fff;
            background: #000;
            border-radius: 5px;
        }
        .fas:hover {
            background: #fff;
            color: #000;
        }
        .fa-user {
            padding: 10px;
            font-size: 20px;
            color: #fff;
            background: #000;
            border-radius: 5px;
        }
        .fa-user:hover {
            background: #fff;
            color: #000;
        }
        .fa-lock {
            padding: 10px;
            font-size: 20px;
            color: #fff;
            background: #000;
            border-radius: 5px;
        }
        .fa-lock:hover {
            background: #fff;
            color: #000;
        }
        .fa-sign-in-alt {
            padding: 10px;
            font-size: 20px;
            color: #fff;
            background: #000;
            border-radius: 5px;
        }
        input[type="submit"] {
            width: 100%;
            background: transparent;
            border: 2px solid #fff;
            color: #fff;
            margin-top: 10px;
            border-radius: 5px;
            padding: 10px;
        }
        input[type="submit"]:hover {
            background: #fff;
            color: #000;
        }
        input[type="submit"]:focus {
            outline: none;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            box-sizing: border-box;
            padding: 10px;
            border-bottom: 2px solid #fff;
            border-top: none;
            border-left: none;
            border-right: none;
            background: transparent;
            color: #fff;

        }
        input[type="text"]:focus, input[type="password"]:focus {
            outline: none;
        }
        .btn {
            width: 100%;
            background: transparent;
            border: 2px solid #fff;
            color: #fff;
            margin-top: 10px;
            border-radius: 5px;
            padding: 10px;
        }

    </style>
</head>
<body>
    <div class="login-box">
        <h1>Login</h1>
        <form action="login.php" method="post">
            <div class="textbox">
                <i class="fas fa-user"></i>
                <input type="text" placeholder="Username" name="username" required>
            </div>

            <div class="textbox">
                <i class="fas fa-lock"></i>
                <input type="password" placeholder="Password" name="password" required>
            </div>

            <input class="btn" type="submit" name="submit" value="Sign in">
        </form>
    </div>
</body>
<footer>
    <p>&copy; Copyright 2020</p>
</footer>
</html>
