# Requires Adafruit_Python_PN532_SPI
# Additional import 
import binascii
import socket
import time
import signal
import sys

import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
from adafruit_pn532.spi import PN532_SPI

try:
    input = raw_input
except NameError:
    pass

# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)


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

# Configure PN532 to communicate with MiFare cards
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
    time.sleep(DELAY)