<?php
    $servername = "db4free.net";
    $username = "kmpspxl";
    $password = "kompaspxl";
    $dbname = "kmpspxl";

	// Create connection
	$conn = new mysqli($servername, $username, $password,$dbname);

	$sql = "UPDATE studenten_default SET NFC_ID = ".$_GET['NFCID']."  WHERE VOORNAAM = '".$_GET['Voornaam']."' AND 
    ACHTERNAAM = '".$_GET['Achternaam']."' AND KLAS = '".$_GET['Klas']."'";
	if ($conn->query($sql) === TRUE) 
	{
		//echo "New record created successfully.";
	} 
	else 
	{
	  echo "Error: " . $sql . "<br>" . $conn->error;
	  echo "Vull alle velden in!";
	}
	$conn->close();
?>