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
              +"&Voornaam="+document.getElementById("Voornaam").value
              +"&Achternaam="+document.getElementById("Achternaam").value
              +"&StudentenID="+document.getElementById("StudentenID").value
              +"&NFCID="+document.getElementById("NFCID").value,true);
	xmlhttp.send();
}