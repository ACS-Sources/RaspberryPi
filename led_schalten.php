<?php
	echo "Dies ist ein Test\n";
	echo "In diesem Beispiel wird ein Python Skript ausgefuehrt.\n";
	
	$res = shell_exec("sudo /usr/bin/python /var/www/led_on.py");
	var_dump($res)."<p>";

	$res = shell_exec("ls -la /var/www/");
	var_dump($res)."<p>";
?>
