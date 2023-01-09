# Requires Adafruit_Python_PN532

import binascii
import socket
import time
import signal
import sys

import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
#
# NOTE: pick the import that matches the interface being used
#
# from adafruit_pn532.i2c import PN532_I2C
from adafruit_pn532.spi import PN532_SPI

try:
    input = raw_input
except NameError:
    pass

# PN532 configuration for a Raspberry Pi GPIO:

# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)

# UART connection
# uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=100)
# pn532 = PN532_UART(uart, debug=False)

ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
# Configure the key to use for writing to the MiFare card.  You probably don't
# need to change this from the default below unless you know your card has a
# different key associated with it.
CARD_KEY = b"\xFF\xFF\xFF\xFF\xFF\xFF"
# Number of seconds to delay after reading data.
DELAY = 0.5

# Prefix, aka header from the card
HEADER = b'BG'

def close(signal, frame):
        sys.exit(0)

signal.signal(signal.SIGINT, close)

# Create and initialize an instance of the PN532 class
pn532.SAM_configuration()

print('PN532 NFC RFID 13.56MHz Card Reader')
while True:
    # Wait for a card to be available
    uid = pn532.read_passive_target()
    # Try again if no card found
    if uid is None:
        continue
    # Found a card, now try to read block 4 to detect the block type
    print('')
    print('Card UID 0x{0}'.format(binascii.hexlify(uid)))
    # Authenticate and read block 4
    if not pn532.mifare_classic_authenticate_block(uid, 4, MIFARE_CMD_AUTH_B,
                                                   CARD_KEY):
        print('Failed to authenticate with card!')
        continue
    data = pn532.mifare_classic_read_block(4)
    if data is None:
        print('Failed to read data from card!')
        continue
    # Check the header
    if data[0:2] !=  HEADER:
        print('Card is not written with proper block data!')
        continue
    # Parse out the block type and subtype
    value = data[2:8]
    print(value)
    print(list(value))
    h = value.hex()
    i = int.from_bytes(value, "big")
    s = value.decode()

    print("hex number: ",h)    
    print("int number: ",i)
    print("string: ",s)
    #print('User Id: {0}'.format(float(data[2:8]).decode("utf-8"), 16))
    time.sleep(DELAY)