# Tijdsregistratiesysteem

**Handleiding gebruik website en Raspberry Pi.**

* [Raspberry Pi](#1)
* [Website](#2)
* [Database](#3)
* [NFC (PN532)](#4)

#### 1. Uitleg rpi <a name="1"></a>
Om een project te kunnen uitvoeren op een Raspberry Pi, moet het Raspberry Pi operating system geïnstalleerd worden op een SD-kaart van minstens 16GB. Deze SD-kaart mag volledig geformatteerd worden vooraleer eraan begonnen wordt. 
Om dit te doen, moet je eerst de Raspberry Pi Imager (link in md zetten) installeren op je computer. Deze tool is een snelle en eenvoudige manier om het Raspberry Pi OS op een SD-kaart te installeren. 
Steek de SD-kaart in je computer en open de Imager. Bij het openen van de Imager, zie je een welkomstscherm.

![image](https://user-images.githubusercontent.com/79916493/212494599-78593b8f-7f71-4e07-ac3d-df20608baf87.png)
 
Om het Raspberry Pi operating system te installeren, klik je in de Raspberry Pi Imager op 'CHOOSE OS' en selecteer je Raspberry Pi OS (32-bit). Vervolgens kies je de SD-kaart waarop je het OS wilt installeren door op 'CHOOSE STORAGE' te klikken en de SD-kaart te selecteren.
Wanneer het schrijven van de image succesvol is afgerond, mag je de SD-kaart verwijderen uit je computer en in de Raspberry Pi plaatsen. Sluit vervolgens de randapparatuur aan zoals het toetsenbord, muis, camera, scherm (HDMI). 
De Raspberry Pi is nu klaargemaakt, maar moet nog geconfigureerd worden.

Raspberry Pi verbinden met wifi
Sluit de Raspberry Pi aan en wacht tot deze is ingeschakeld.
Startscherm:
![image](https://user-images.githubusercontent.com/79916493/212494614-df387db6-3c75-4315-9492-5c45c7201bfb.png)

 
Om verbinding te maken met een wifi-netwerk, klikt u op het wifi-icoontje in de rechterbovenhoek van het scherm. Zet de wifi aan en selecteer vervolgens het gewenste wifi-netwerk.
![image](https://user-images.githubusercontent.com/79916493/212494618-fd9cc7a0-12c8-4040-af19-d79da590fc8b.png)

 
Na het kiezen van uw netwerk, verschijnt er een venster in het midden. Voer hier uw netwerkwachtwoord in.
![image](https://user-images.githubusercontent.com/79916493/212494623-e12ee1f1-16d5-4063-89ac-5f2f6f26ec43.png)

 
Zorg dat de Raspberry Pi verbonden is met het netwerk en noteer het toegewezen IP-adres door met de cursor over het wifi-icoontje te bewegen. Hierdoor zal een venster verschijnen met het IP-adres. Let erop dat zowel de Raspberry Pi als je PC op hetzelfde wifi-netwerk zijn aangesloten.
![image](https://user-images.githubusercontent.com/79916493/212494639-40bbff51-ea16-4650-b226-7e30f3fe2880.png)

Mogelijke IP-adres: 169.154.146.220, niet overnemen.

Configureren Raspberry Pi
Om SSH in te schakelen op de Raspberry Pi, ga je naar het menu bovenaan links en selecteer je "Preferences" en vervolgens "Raspberry Pi Configuration". In het tabblad "Interfaces" klik je vervolgens op "SSH" om het in te schakelen.
![image](https://user-images.githubusercontent.com/79916493/212494652-a994224c-8bbf-4e99-b110-24e068bf60f1.png)

 
Als volgende stap gaan we de benodigde bibliotheken downloaden en functionaliteiten activeren op de RPI via een specifiek .sh bestand, hiervoor zal Putty op je PC gebruikt worden. Wanneer Putty wordt geopend, zal het volgende scherm zich presenteren.
PuTTY is een gratis en open-source seriële console en netwerkbestandsoverdracht applicatie. Het wordt veel gebruikt om op afstand toegang te krijgen tot servers, netwerkapparaten en andere uitrusting. Het is beschikbaar voor Windows, Linux en macOS.

Als je Putty op je computer opent, zul je worden begroet met een welkomsscherm:
![image](https://user-images.githubusercontent.com/79916493/212494657-e4f1334b-3232-4622-b91e-b584159f476d.png)

 
Om verbinding te maken met een Raspberry Pi via SSH, moet u het IP-adres van de Raspberry Pi invoeren bij de hostnaam. Zorg ervoor dat de PC en de Raspberry Pi zich op hetzelfde wifi-netwerk bevinden. Voer vervolgens poortnummer 22 in en selecteer SSH als het verbindingstype. Druk vervolgens op Open om de verbinding te openen.
![image](https://user-images.githubusercontent.com/79916493/212494661-c5a04aec-dc92-4a98-bf08-639ff6700a5e.png)

 
Om in te loggen op de Raspberry Pi, gebruikt u de standaard inloggegevens van "pi" als gebruikersnaam en "raspberry" als wachtwoord. Als u een andere gebruikersnaam en wachtwoord heeft gekozen, gebruikt u deze in plaats daarvan.
Elk keer wanneer u opnieuw wilt inloggen met Putty, moet u deze stappen herhalen.
Als u succesvol bent ingelogd, zal uw terminal er als volgt uitzien:
![image](https://user-images.githubusercontent.com/79916493/212494664-db53baee-d1e4-4bad-ac42-0b66b8613d7b.png)

 
Inloggegevens ter illustratie, niet overnemen.
Installeren van bibliotheken om de code te kunnen uitvoeren:
Kopieer en plak (rechtmuisknop) in de Putty terminal om onderstaande te installeren.
•	sudo pip3 install adafruit-circuitpython-pn532
•	sudo pip3 install mysql-connector-python
•	sudo pip3 install adafruit-blinka


#### 2. Website <a name="2"></a>
    // algemene uitleg van functionaliteiten
    // instructies: hoe eraan geraken, services voor user uitleggen
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

 
#### 3. Database <a name="3"></a>
phpMyAdmin is een gratis en open-source webgebaseerde tool geschreven in PHP die wordt gebruikt om MySQL en MariaDB databases te beheren en administreren. Het biedt een gebruiksvriendelijke webinterface om met databases te communiceren, waarmee gebruikers verschillende taken kunnen uitvoeren zoals het maken, wijzigen en verwijderen van databases en tabellen, beheren van gebruikers , SQL-queries uitvoeren en meer.
In the project there are 2 tables used as database. One is used purely for keeping track of students' time and the other for keeping track of all the students with their information.
Both tables use the following information. A general ID, this is nothing special and is just a counter when a new line comes in. The NFC ID is the Uid (unique identifier) of the NFC tag. This is followed by the student's general information such as first name, last name and the class the student is in. Only in the database that keeps track of students' time records is also a column with the time + date attached.
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
![image](https://user-images.githubusercontent.com/79916493/212494753-7373b34e-3af5-426e-a041-d2f9546b4c99.png)

 
It is of importance to properly designate the appropriate communication protocol on the PN532. This project employs the use of the SPI communication protocol. The image below provided the appropriate positioning of the sliders. Additionally, as indicated in the table, the left slider button on the PN532 should be in the down position, while the right one should be in the up position.
![image](https://user-images.githubusercontent.com/79916493/212494761-b1d3f154-fb9b-4f97-a64a-23f5f015b4d5.png)

 
After all configurations have been imported both software-wise with all proper libraries and hardware configurations with proper wiring and proper communication protocol chosen, the suitable code can be executed.
// extra chips bijbestellen? website geven als voorbeeld


// apart file voor code uitleg (meerdere files van ieder py file: nfc, qr, extra van nikita)

//// punten opschrijven die nog gedaan (future) worden

// videos?








Conclusie: Wegens tijdgebrek hebben we deze projecten niet kunnen installeren. We kregen een te laat antwoord op de mail waarop we dachten om deze te installeren in de kerstvakantie.

Tijden aanwezig gewerkt aan het project:
- 7/10: 3uur
- naar kompas: 3uur
- 26/10: 3uur
- 28/10: 3uur
- 14/11: 3uur
- 18/11: 3.5-4uur
- 21/11: 3uur
- 25/11: 2.5uur
- 2/12: 3uur
- 5/12: 3uur
- 9/12: 3.5uur
- 12/12: 1.5uur
- 16/12: 2uur
- 23/12: 3.5uur
- 13/01: 5uur

Ongeveer +- 45uur (2 dagen per week, elke vrijdag in corda 3 of 7)

