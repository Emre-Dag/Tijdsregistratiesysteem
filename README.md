# Time registration system

**Manual use website and Raspberry Pi**

* [Raspberry Pi](#1)
* [Database](#2)
* [Website](#3)
* [NFC (PN532)](#4)
* [Link to projects](#5)
* [Possible extensions](#6)
* [Conclusion](#7)

---

#### 1. Raspberry Pi <a name="1"></a>
To run a project on a Raspberry Pi, the Raspberry Pi operating system must be installed on an SD card of at least 16GB. This SD card may be fully formatted before starting. 
To do this, you must first install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your computer. This tool is a quick and easy way to install the Raspberry Pi OS on an SD card. 
Insert the SD card into your computer and open the Imager. Upon opening the Imager, you will see a welcome screen.

![image](https://user-images.githubusercontent.com/79916493/212494599-78593b8f-7f71-4e07-ac3d-df20608baf87.png)
 
To install the Raspberry Pi operating system, click on 'CHOOSE OS' in the Raspberry Pi Imager and select Raspberry Pi OS (32-bit). Then choose the SD card you want to install the OS on by clicking on 'CHOOSE STORAGE' and selecting the SD card.
When the image writing is completed successfully, you may remove the SD card from your computer and insert it into the Raspberry Pi. Then connect the peripherals such as keyboard, mouse, camera, screen (HDMI).
The Raspberry Pi is now prepared, but still needs to be configured.

---

## Connecting Raspberry Pi to wifi

Plug in the Raspberry Pi and wait for it to turn on.

Start screen: 


![image](https://user-images.githubusercontent.com/79916493/212494614-df387db6-3c75-4315-9492-5c45c7201bfb.png)

 
To connect to a wifi network, click on the wifi icon in the upper right corner of the screen. Turn on the wifi and then select the desired wifi network.

![image](https://user-images.githubusercontent.com/79916493/212494618-fd9cc7a0-12c8-4040-af19-d79da590fc8b.png)

 
After choosing your network, a window appears in the middle. Enter your network password here.

![image](https://user-images.githubusercontent.com/79916493/212494623-e12ee1f1-16d5-4063-89ac-5f2f6f26ec43.png)

 
Make sure the Raspberry Pi is connected to the network and note the assigned IP address by moving the cursor over the Wi-Fi icon. This will bring up a window with the IP address. Make sure that both the Raspberry Pi and your PC are connected to the same wifi network.

![image](https://user-images.githubusercontent.com/79916493/212494639-40bbff51-ea16-4650-b226-7e30f3fe2880.png)

*possible IP-address: 169.154.146.220, do not take over.*

To enable SSH on the Raspberry Pi, go to the menu at the top left and select "Preferences" and then "Raspberry Pi Configuration." In the "Interfaces" tab, then click on "SSH" to enable it. Also enable "SPI" since it will be used later.

![image](https://user-images.githubusercontent.com/79916493/212494652-a994224c-8bbf-4e99-b110-24e068bf60f1.png)

*Download [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (MSI Windows Installer: 64-bit x86:)*

When Putty is opened, the following screen will present itself.

PuTTY is a free and open-source serial console and network file transfer application. It is widely used to remotely access servers, network devices and other equipment. It is available for Windows, Linux and macOS.

When you open Putty on your computer, you will be greeted with a welcome screen:

![image](https://user-images.githubusercontent.com/79916493/212494657-e4f1334b-3232-4622-b91e-b584159f476d.png)

To connect to a Raspberry Pi via SSH, enter the Raspberry Pi's IP address in the hostname. Make sure the PC and the Raspberry Pi are on the same Wi-Fi network. Next, enter port number 22 and select SSH as the connection type. Next, press Open to open the connection.

![image](https://user-images.githubusercontent.com/79916493/212494661-c5a04aec-dc92-4a98-bf08-639ff6700a5e.png)

 
To log in to the Raspberry Pi, use the default login credentials of "pi" as the username and "raspberry" as the password. If you have chosen a different username and password, use them instead.
Each time you want to log back in with Putty, you need to repeat these steps.

If you are successfully logged in, your terminal will look like this:

![image](https://user-images.githubusercontent.com/79916493/212494664-db53baee-d1e4-4bad-ac42-0b66b8613d7b.png)

*Login data for illustration purposes, do not copy.*

Installing libraries to run the code:
Copy and paste (right mouse button) into the Putty terminal to install the following.

- sudo pip3 install adafruit-circuitpython-pn532

- sudo pip3 install mysql-connector-python

- sudo pip3 install adafruit-blinka

- sudo apt-get install python3-rpi.gpio

- pip install opencv-python

- pip install webbrowser

- pip install time

---

Next, to transport the code on the Raspberry Pi, we need an FTP client. And finally an SSH client to execute commands on the Raspberry Pi. You should have installed these at the beginning.

First, download the full repository.

![MicrosoftTeams-image](https://user-images.githubusercontent.com/79916493/212497655-c7b27233-16d1-4b0e-8a11-f27185eb76c0.png)


*Download [FileZilla](https://filezilla-project.org/download.php?type=client)*

Open FileZilla and enter the data you had retrieved in the previous steps.

Host: IP-adres

Username: pi

Password: raspberry

Port: 22

Click 'Snelverbinden' to make a connection.

![tempsnip](https://user-images.githubusercontent.com/79916493/212497405-83cdc9a2-b6ce-4aa9-ba75-92b23529c712.png)

*On the left you see the working environment of your PC and on the right you see that of the Raspberry Pi. Now files can be exchanged between these 2 devices.*

On the left, select the repository that was downloaded and drag the code (RPI_master.py) on the right into the Desktop folder.

Commands below to run the code.

![image](https://user-images.githubusercontent.com/79916493/212497788-cd8056ea-5394-46ce-8456-73bfa622d8ff.png)


---
 
#### 2. Database <a name="2"></a>
phpMyAdmin is a free and open-source web-based tool written in PHP used to manage and administer MySQL and MariaDB databases. It provides a user-friendly web interface to interact with databases, allowing users to perform various tasks such as creating, modifying and deleting databases and tables, managing users , running SQL queries and more.    

In the project there are 2 tables used as database. One is used purely for keeping track of students' time and the other for keeping track of all the students with their information.
Both tables use the following information. A general ID, this is nothing special and is just a counter when a new line comes in. The NFC ID is the Uid (unique identifier) of the NFC tag. This is followed by the student's general information such as first name, last name and the class the student is in. Only in the database that keeps track of students' time records is also a column with the time + date attached.

---

#### 3. Website <a name="3"></a>

The website serves as a dashboard for modifying the database and is currently hosted on a PXL server owned by the student. However, it will need to be moved to a paid server in the future.
On the website, there are several functions that allow for manipulation of the ”studenten_default” database. One of these functions is the ability to add new students to the database.

![image](https://user-images.githubusercontent.com/79916493/212494675-f15757a0-f9a1-41b7-8afd-385caa641de2.png)

 
The website also has a function that allows for deletion of students from the database by inputting their unique NFC ID and clicking the "delete student" button.

![image](https://user-images.githubusercontent.com/79916493/212494681-bc449c9b-5bc9-4fd7-be7d-c672a8a1ff57.png)

 
Additionally, the website allows for editing NFC ID by inputting the student's information. This feature can be useful in cases such as when a student loses their NFC badge.

![image](https://user-images.githubusercontent.com/79916493/212494691-e7981278-59d1-4756-9b30-d3b35808ba13.png)

 
The website also allows for editing of a student's information by inputting their unique identification. This feature can be useful in cases such as when a student changes classes.

![image](https://user-images.githubusercontent.com/79916493/212494700-a343f2d7-d42a-4ff6-8e59-f838d52c83a8.png)

 
Finally, it is also possible to view student registrations and filter certain data from the "student" database.

![image](https://user-images.githubusercontent.com/79916493/212494706-f3992a91-6167-4f62-8c97-8ffadcfcbad5.png)

---

#### 4. PN532 <a name="4"></a>
What is NFC?
NFC, or Near Field Communication, is a technology standard that is based on the principles of Radio Frequency Identification (RFID). It enables the wireless transmission of information over short distances, allowing for a more efficient and convenient exchange of information. This technology has become increasingly popular among consumers worldwide, as it simplifies transactions, digital content exchange, and electronic device connectivity with a simple touch. Furthermore, the technology is compatible with the vast majority of contactless cards and readers currently in use worldwide.

![image](https://user-images.githubusercontent.com/79916493/212494718-de8acafc-00e8-46d9-b3c5-b51263935f0a.png)

 
How does it work?
The fundamental principle behind the functioning of NFC technology is inductive coupling, particularly for short-range implementation. To elaborate, the reader device generates a magnetic field by passing an electric current through a coil. When a tag, which also comprises of a coil, is brought within proximity, the field induces an electric current within the tag, without the need for any physical contact or wires. Once the initial connection is established, any stored data on the tag is wirelessly transmitted to the reader device.

![image](https://user-images.githubusercontent.com/79916493/212494731-4a0a5b1c-125d-45a5-ab26-069dffc74c23.png)

 
NFC vs RFID
The primary difference between RFID and NFC technology lies in the transmission range. RFID is generally utilized for longer distances, for example, some regions use RFID for automatic collection of road tolls. Additionally, if RFID tags are equipped with a power source, communication can occur over even longer distances. On the other hand, NFC has a limited transmission range of a few centimeters at most. Furthermore, in most smartphone-related applications, communication is initiated only when there is physical contact. Another important aspect to note is that NFC devices possess bidirectional capability, allowing them to function as either a reader or a tag. This feature enables the usage of a single piece of hardware such as a smartphone, for various applications.

![image](https://user-images.githubusercontent.com/79916493/212494738-6f6a71e4-11ce-4890-b0c7-8ee6ad2532a7.png)

 
PN532 NFC Module
The PN532 is a highly advanced NFC (Near Field Communication) controller developed by NXP. It is built on the 80C51 microcontroller platform, enabling efficient contactless communication at a frequency of 13.56 MHz. This device also features support for MIFARE Classic 1K and MIFARE Classic 4K cards, resulting in increased transfer speeds of up to 424 kbit/s in both directions. Additionally, the PN532 boasts a substantial 40 Kb ROM and 1Kb RAM, making it suitable for emulating ISO14443 cards. The ISO/IEC 14443 series of standards provides guidelines for the parameters of identification cards and objects for international interchange, which the PN532 effectively adheres to.

![image](https://user-images.githubusercontent.com/79916493/212494745-733828a7-a672-491a-be67-63d8a81e09a9.png)

 
Connection PN532 with Rasberry Pi 3
For the wiring diagram, the below diagram was applied. Using a wire, connect the diagram below from the rasberry pi headers to the headers (solder in yourself) of the PN532.

![image](https://user-images.githubusercontent.com/79916493/212496545-eea25161-0ee1-436c-9ea1-b0dc2b5f853a.png)

 
It is of importance to properly designate the appropriate communication protocol on the PN532. This project employs the use of the SPI communication protocol. The image below provided the appropriate positioning of the sliders. Additionally, as indicated in the table, the left slider button on the PN532 should be in the down position, while the right one should be in the up position.

![image](https://user-images.githubusercontent.com/79916493/212494761-b1d3f154-fb9b-4f97-a64a-23f5f015b4d5.png)

 
After all configurations have been imported both software-wise with all proper libraries and hardware configurations with proper wiring and proper communication protocol chosen, the suitable code can be executed.

---

#### 5. Link to projects <a name="5"></a>

The following folders contain the corresponding readmes and code.
- [General NFC code](https://github.com/Emre-Dag/Tijdsregistratiesysteem/tree/main/NFC) -> used
- [Website](https://github.com/Emre-Dag/Tijdsregistratiesysteem/tree/main/Website) -> used
- [Extra NFC code](https://github.com/Emre-Dag/Tijdsregistratiesysteem/tree/main/extra_nfc) -> different option, but not used
- [QR-code](https://github.com/Emre-Dag/Tijdsregistratiesysteem/tree/main/qrcode) -> different option, but not used

---

#### 6. Possible extensions <a name="6"></a>

- Installing and running this project.

- Export database to CSV file (log), possibly automatically per day/week/month/year
- Security and performance of code: double scanned, allowed time between scanning
- Website and database hosted on a better platform (local or paid server)
- Additional extension: hang screen so students can follow if registration is complete
- Making a casing for the NFC reader and RPI

---

#### 7. Conclusion <a name="7"></a>
This project has been finalized. All that needs to be done is to install the project in the method school, but due to lack of time, we have not been able to install this project. We received a late reply to the mail on which we thought to install them during the Christmas vacation.

---

Presence worked on the project:
- 7/10: 3h
- naar kompas: 3h
- 26/10: 3h
- 28/10: 3h
- 14/11: 3h
- 18/11: 3.5-4h
- 21/11: 3h
- 25/11: 2.5h
- 2/12: 3h
- 5/12: 3h
- 9/12: 3.5h
- 12/12: 1.5h
- 16/12: 2h
- 23/12: 3.5h
- 13/01: 5h

About +- 45 hours (2 days a week in corda 3 or 7)

