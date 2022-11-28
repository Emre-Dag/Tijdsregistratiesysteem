import mysql.connector

mydb = mysql.connector.connect(
  host="db4free.net",
  user="kmpspxl",
  password="kompaspxl",
  database="kmpspxl"
)

mycursor = mydb.cursor()


mycursor.execute("INSERT INTO studenten (NFC_ID) VALUES (5)")
mydb.commit()