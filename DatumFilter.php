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
    if($_GET['Datum']==true&&$_GET['MinTime']==true&&$_GET['MaxTime']==true)
    {
        $MinDate = date("Y-m-d H:i:s", strtotime($_GET['Datum']." ".$_GET['MinTime'].":00"));
        $MaxDate = date("Y-m-d H:i:s",strtotime($_GET['Datum']." ".$_GET['MaxTime'].":00"));
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==true&&$_GET['MaxTime']==false)
    {
        $MinDate = date("Y-m-d H:i:s",strtotime($_GET['Datum']." ".$_GET['MinTime'].":00"));
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==false&&$_GET['MaxTime']==true)
    {
        $MaxDate = date("Y-m-d H:i:s",strtotime($_GET['Datum']." ".$_GET['MaxTime'].":00"));
    }

    $MinDateNoTime = $_GET['Datum']." 00:00:00";
    $MaxDateNoTime = $_GET['Datum']." 23:59:59";
//------------------------------------------------------------------------
    if($_GET['Datum']==true&&$_GET['MinTime']==true&&$_GET['MaxTime']==true)
    {
        $sql ="SELECT * FROM studenten WHERE TIJD BETWEEN '".$MinDate."' AND '".$MaxDate."'";
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==true&&$_GET['MaxTime']==false)
    {
        $sql ="SELECT * FROM studenten WHERE TIJD BETWEEN '".$MinDate."' AND '".$MaxDateNoTime."'";
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==false&&$_GET['MaxTime']==true)
    {
        $sql ="SELECT * FROM studenten WHERE TIJD BETWEEN '".$MinDateNoTime."' AND '".$MaxDate."'";
    }
    elseif($_GET['Datum']==true&&$_GET['MinTime']==false&&$_GET['MaxTime']==false)
    {
        $sql ="SELECT * FROM studenten WHERE TIJD BETWEEN '".$MinDateNoTime."' AND '".$MaxDateNoTime."'";
    }
    else
    {
        $sql ="SELECT * FROM studenten";
    }
//------------------------------------------------------------------------
        $result = $conn->query($sql);
        if ($result->num_rows > 0) 
        {
            echo "<table><tr><th>ID</th><th>NFC_ID</th><th>STUDENTEN_ID</th><th>VOORNAAM</th><th>ACTERNAAM</th><th>TIJD</th></tr>";
            // output data of each row
            while($row = $result->fetch_assoc()) 
            {
                echo "<tr><td>".$row["ID"]."</td><td>".$row["NFC_ID"]."</td><td>".$row["STUDENTEN_ID"]."</td><td>".$row["VOORNAAM"]."</td><td>".$row["ACHTERNAAM"]."</td><td>".$row["TIJD"]."</td></tr>";
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