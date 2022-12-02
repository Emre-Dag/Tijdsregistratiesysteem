import mysql.connector
import re

mydb = mysql.connector.connect(
  host="db4free.net",
  user="kmpspxl",
  password="kompaspxl",
  database="kmpspxl"
)

mycursor = mydb.cursor()


"""mycursor.execute("INSERT INTO studenten (NFC_ID) VALUES (['0xbb', '0x76', '0x7b', '0x2b'])")"""

uid = ['0xbb', '0x76', '0x7b', '0x2b']

mylist = []
for i in uid:
  d = int(i, base=16)
  print(d)
  mylist.append(d)
  output_id = str(mylist).strip("[,]")
  s=re.sub(", ","",output_id)
  

out_int = int(s)
print(mylist)
print(s)
print(type(out_int))
print(out_int)
mydb.commit()