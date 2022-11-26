# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example shows connecting to the PN532 with I2C (requires clock
stretching support), SPI, or UART. SPI is best, it uses the most pins but
is the most reliable and universally supported.
After initialization, try waving various 13.56MHz RFID cards over it!
"""

import board
import busio
from digitalio import DigitalInOut
import time
import RPi.GPIO as GPIO
from adafruit_pn532.spi import PN532_SPI
import mysql.connector

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
        mycursor.execute("INSERT INTO kompas_studenten (NFC_ID ) VALUES (50)")
        mydb.commit()
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
