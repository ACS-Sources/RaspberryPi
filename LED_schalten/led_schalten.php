<?php
	echo "Dies ist ein Test\n";
	echo "In diesem Beispiel wird ein Python Skript ausgefuehrt.\n";
	
	$res = shell_exec("sudo /usr/bin/python /home/pi/PythonCode_Samples/led_schalten.py");
	var_dump($res)."<p>";

	$res = shell_exec("ls -la /home/pi/PythonCode_Samples/");
	var_dump($res)."<p>";
?>
