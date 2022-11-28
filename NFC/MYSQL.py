import mysql.connector

mydb = mysql.connector.connect(host="db4free.net",    # your host, usually localhost
                                         user="kmpspxl",         # your username
                                         passwd="kompaspxl",  # your password
                                         db="kmpspxl") 

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM kompas_studenten")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
