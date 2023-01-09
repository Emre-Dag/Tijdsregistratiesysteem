function start(){
  PrintTabel();
}

function currentTime() 
{
  var date = new Date(); /* creating object of Date class */
  var hour = date.getHours();
  var min = date.getMinutes();
  var sec = date.getSeconds();
  hour = updateTime(hour);
  min = updateTime(min);
  sec = updateTime(sec);
  document.getElementById("clock").innerText = hour + " : " + min + " : " + sec; /* adding time to the div */
	var t = setTimeout(function(){ currentTime() }, 1000); /* setting timer */
}

function updateTime(k) 
{
  if (k < 10) {
	return "0" + k;
  }
  else {
	return k;
  }
}
currentTime();

function PrintTabel()
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() 
  {
		document.getElementById("tabel").innerHTML = this.responseText;
	};
	xmlhttp.open("GET","DatumFilter.php?MinTime="
              +document.getElementById("MinTime").value
              +"&MaxTime="+document.getElementById("MaxTime").value
              +"&Datum="+document.getElementById("Datum").value
              +"&Voornaam="+document.getElementById("VoornaamF").value
              +"&Achternaam="+document.getElementById("AchternaamF").value
              +"&Klas="+document.getElementById("KlasF").value
              +"&NFCID="+document.getElementById("NFCIDF").value,true);
	xmlhttp.send();
}
function UpdateStudentWithUID()
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() 
  {
    document.getElementById("Update").innerHTML = this.responseText;
	};
	xmlhttp.open("GET","Update_Values_With_UID.php?Voornaam="
              +document.getElementById("Voornaam").value
              +"&Achternaam="+document.getElementById("Achternaam").value
              +"&Klas="+document.getElementById("Klas").value
              +"&NFCID="+document.getElementById("NFCID").value,true);
	xmlhttp.send();
}

function UpdateUIDWithStudent()
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() 
  {
    document.getElementById("Update2").innerHTML = this.responseText;
	};
	xmlhttp.open("GET","Update_UID_With_Values.php?Voornaam="
              +document.getElementById("Voornaam2").value
              +"&Achternaam="+document.getElementById("Achternaam2").value
              +"&Klas="+document.getElementById("Klas2").value
              +"&NFCID="+document.getElementById("NFCID2").value,true);
	xmlhttp.send();
}

function AddNewStudent()
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() 
  {
    document.getElementById("AddStudent").innerHTML = this.responseText;
	};
	xmlhttp.open("GET","AddNewStudent.php?Voornaam="
              +document.getElementById("VoornaamN").value
              +"&Achternaam="+document.getElementById("AchternaamN").value
              +"&Klas="+document.getElementById("KlasN").value
              +"&NFCID="+document.getElementById("NFCIDN").value,true);
	xmlhttp.send();
}
function DeleteUID()
{
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() 
  {
    document.getElementById("DeleteUID").innerHTML = this.responseText;
	};
	xmlhttp.open("GET","DeleteUID.php?NFCID="+document.getElementById("NFCIDD").value,true);
	xmlhttp.send();
}