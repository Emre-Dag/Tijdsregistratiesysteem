# Requires Adafruit_Python_PN532_SPI
# Additional import 
import binascii
import sys
import struct

import board
import busio
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI

try:
    input = raw_input
except NameError:
    pass

# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)
# Configure the key to use for writing to the MiFare card.  You probably don't
# need to change this from the default below unless you know your card has a
# different key associated with it.
CARD_KEY =b"\xFF\xFF\xFF\xFF\xFF\xFF"

# Prefix, aka header from the card
HEADER = b'BG'

ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

# Step 1, wait for card to be present.
print('PN532 NFC Module Writer')
print('')
print('== STEP 1 =========================')
print('Place the card to be written on the PN532...')
uid = pn532.read_passive_target()
while uid is None:
    uid = pn532.read_passive_target()
print('')
print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
print('')
print('==============================================================')
print('WARNING: DO NOT REMOVE CARD FROM PN532 UNTIL FINISHED WRITING!')
print('==============================================================')
print('')

# Step 2, pick a block type.
print('== STEP 2 =========================')
block_choice = None
while block_choice is None:
    print('')
    block_choice = input('Enter user ID (max 12 numbers): ')
    try:
        block_choice = str(block_choice)
    except ValueError:
        print('Error! Unrecognized option.')
        continue
    print('')
print('You chose the block type: {0}'.format(block_choice))
print('')

# Confirm writing the block type.
print('== STEP 3 =========================')
print('Confirm you are ready to write to the card:')
print('User ID: {0}'.format(block_choice))
choice = input('Confirm card write (Y or N)? ')
if choice.lower() != 'y' and choice.lower() != 'yes':
    print('Aborted!')
    sys.exit(0)
print('Writing card (DO NOT REMOVE CARD FROM PN532)...')

# Write the card!
# First authenticate block 4.
if not pn532.mifare_classic_authenticate_block(uid, 4, MIFARE_CMD_AUTH_B,
                                               CARD_KEY):
    print('Error! Failed to authenticate block 4 with the card.')
    sys.exit(-1)
# Next build the data to write to the card.
# Format is as follows:
# - 2 bytes 0-1 store a header with ASCII value, for example 'BG'
# - 6 bytes 2-7 store the user data, for example user ID
data = bytearray(16)
# Add header
data[0:2] = HEADER
#-----------------------------------------------------
# Convert int to hex string with up to 6 digits
value = format(str(block_choice))
print(value)
while (12 > len(value)):
    value = '0' + value
    print(value)
data[2:8] = bytes.fromhex(value)
#-----------------------------------------------------
# Finally write the card.
if not pn532.mifare_classic_write_block(4, data):
    print('Error! Failed to write to the card.')
    sys.exit(-1)
print('Wrote card successfully! You may now remove the card from the PN532.')