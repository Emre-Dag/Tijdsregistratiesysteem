# import libraries
import board
import busio
from digitalio import DigitalInOut
import time
import RPi.GPIO as GPIO
from adafruit_pn532.spi import PN532_SPI
import mysql.connector
import re

# connect to database
mydb = mysql.connector.connect(
  host="db4free.net",
  user="kmpspxl",
  password="kompaspxl",
  database="kmpspxl"
)

mycursor = mydb.cursor()

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)
ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print("Waiting for RFID/NFC card...")
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=1)
    """print(".", end="")"""
    # Try again if no card is available.
    if uid is not None:
        print("Found card with UID:", [hex(i) for i in uid])
        id_dec = str(uid).strip("\,[,],(,),'")
        print(id_dec)
        # Converting UID to integer value
        mylist = []
        for i in uid:
          print(i)
          d = int(str(i), base=16)
          print(d)
          mylist.append(d)
          output_id = str(mylist).strip("[,]")
          s=re.sub(", ","",output_id)

        out_int = int(s)
        # Print the UID(NFC ID)
        print(mylist)
        print(out_int)
        # Copy information of the UID(Name,Surname,Class) from table "studenten_default" to "studenten" with the current time
        mycursor.execute("INSERT INTO studenten (KLAS,VOORNAAM,ACHTERNAAM,NFC_ID, TIJD) SELECT KLAS,VOORNAAM,ACHTERNAAM,NFC_ID,NOW() FROM studenten_default WHERE NFC_ID =({})".format(out_int))
        mydb.commit()
        print("data verstuurd!!!!!!!!!!!")

        # Zoomer high for 1 second
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
