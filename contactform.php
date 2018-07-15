<?php
// https://www.youtube.com/watch?v=4q0gYjAVonI

if (isset($_POST['submit'])) {
	$name = $_POST['name'];
	$subject = $_POST['subject'];
	$mailFrom = $_POST['mail'];
	$message = $_POST['message'];

	$mailTo = 'firamos@uci.edu';
	$headers = "From: ".$mailFrom;
	$txt = "You have received an email from ".$name.".\n\n".$message;
// No error handling to check if email is legit...

	mail($mailTo, $subject, $txt, $headers);
	header("Location: form.html?mailsend")
}