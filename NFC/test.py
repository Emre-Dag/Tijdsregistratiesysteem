import mysql.connector

# Database instellingen
mydb = mysql.connector.connect(
  host="sql11.freemysqlhosting.net",
  user="sql11590372",
  password="lj2xrt6AXi",
  database="sql11590372",
  port= 3306,
)

mycursor = mydb.cursor()


#mycursor.execute("select Kleur from Orders where OrderId=25")

#mail = mycursor.fetchall()
#print(mail)
