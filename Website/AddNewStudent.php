<?php
    $servername = "db4free.net";
    $username = "kmpspxl";
    $password = "kompaspxl";
    $dbname = "kmpspxl";

	// Create connection
	$conn = new mysqli($servername, $username, $password,$dbname);

	$sql = "INSERT INTO studenten_default (VOORNAAM ,ACHTERNAAM, KLAS,NFC_ID) VALUES ('".$_GET['Voornaam']."','".$_GET['Achternaam']."','".$_GET['Klas']."',".$_GET['NFCID'].")";
	if ($conn->query($sql) === TRUE) 
	{
		echo "New record created successfully.";
	} 
	else 
	{
	  echo "Error: " . $sql . "<br>" . $conn->error;
	}
	$conn->close();
?>