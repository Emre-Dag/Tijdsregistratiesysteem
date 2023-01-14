<?php
    $servername = "db4free.net";
    $username = "kmpspxl";
    $password = "kompaspxl";
    $dbname = "kmpspxl";

    // Create connection
    $conn = new mysqli($servername, $username, $password,$dbname);

    if ($conn->connect_error) 
    {
        die("Connection failed: " . $conn->connect_error);
    }
//------------------------------------------------------------------------
    $NFC_ID=1;
    $Klas=1;
    $Voornaam=1;
    $Achternaam=1;
    if($_GET['NFCID']!='')    
    {
        $NFC_ID = "NFC_ID = ".$_GET['NFCID'];
    }
    if($_GET['Klas']!='')    
    {
        $Klas =  "KLAS = '".$_GET['Klas']."'";
    }
    if($_GET['Voornaam']!='')    
    {
        $Voornaam = "VOORNAAM = '".$_GET['Voornaam']."'";
    }
    if($_GET['Achternaam']!='')    
    {
        $Achternaam = "ACHTERNAAM = '".$_GET['Achternaam']."'";
    }

//------------------------------------------------------------------------
    $MinDateNoTime = $_GET['Datum']." 00:00:00";
    $MaxDateNoTime = $_GET['Datum']." 23:59:59";
    if($_GET['Datum']==true&&$_GET['MinTime']==true&&$_GET['MaxTime']==true)
    {
        $MinDate = date("Y-m-d H:i:s", strtotime($_GET['Datum']." ".$_GET['MinTime'].":00"));
        $MaxDate = date("Y-m-d H:i:s",strtotime($_GET['Datum']." ".$_GET['MaxTime'].":00"));
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==true&&$_GET['MaxTime']==false)
    {
        $MinDate = date("Y-m-d H:i:s",strtotime($_GET['Datum']." ".$_GET['MinTime'].":00"));
        $MaxDate = $MaxDateNoTime;
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==false&&$_GET['MaxTime']==true)
    {
        $MinDate = $MinDateNoTime;
        $MaxDate = date("Y-m-d H:i:s",strtotime($_GET['Datum']." ".$_GET['MaxTime'].":00"));
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==false&&$_GET['MaxTime']==false)
    {
        $MinDate = $MinDateNoTime;
        $MaxDate = $MaxDateNoTime;
    }
//------------------------------------------------------------------------
    if($_GET['Datum']==true)
    {
        $sql ="SELECT * FROM studenten WHERE TIJD BETWEEN '".$MinDate."' AND '".$MaxDate."' 
               AND ".$NFC_ID." 
               AND ".$Klas." 
               AND ".$Voornaam." 
               AND ".$Achternaam;
    }
    else
    {
        $sql ="SELECT * FROM studenten WHERE 
        ".$NFC_ID." 
        AND ".$Klas." 
        AND ".$Voornaam." 
        AND ".$Achternaam;
    }
//------------------------------------------------------------------------
        $result = $conn->query($sql);
        if ($result->num_rows > 0) 
        {
            echo "<table><tr><th>ID</th><th>NFC_ID</th><th>KLAS</th><th>VOORNAAM</th><th>ACHTERNAAM</th><th>TIJD</th></tr>";
            // output data of each row
            while($row = $result->fetch_assoc()) 
            {
                echo "<tr><td>".$row["ID"]."</td><td>".$row["NFC_ID"]."</td><td>".$row["KLAS"]."</td><td>".$row["VOORNAAM"]."</td><td>".$row["ACHTERNAAM"]."</td><td>".$row["TIJD"]."</td></tr>";
            }
            echo "</table>";
        }
        else 
        {
            echo "0 results";
        }
//------------------------------------------------------------------------
            $conn->close();
?>