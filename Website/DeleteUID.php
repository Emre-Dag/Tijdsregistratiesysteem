<?php
    $servername = "db4free.net";
    $username = "kmpspxl";
    $password = "kompaspxl";
    $dbname = "kmpspxl";

	// Create connection
	$conn = new mysqli($servername, $username, $password,$dbname);

	$sql = "DELETE FROM studenten_default
    WHERE NFC_ID = ".$_GET['NFCID']."";
	if ($conn->query($sql) === TRUE) 
	{
		echo "Student deleted.";
	} 
	else 
	{
	  echo "Error: " . $sql . "<br>" . $conn->error;
	}
	$conn->close();
?>