#bronnen: https://www.geeksforgeeks.org/webcam-qr-code-scanner-using-opencv/

import cv2
import webbrowser
import time
# Create a VideoCapture object
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#creates a QRCodeDetector object, which is used to detect and decode QR codes in images.
detector = cv2.QRCodeDetector()
# Check if camera opened successfully
if (cam.isOpened() == False):
  print("Error opening video stream or file")

# Read the video
while(cam.isOpened()):
    check, frame = cam.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(frame)
    # check if there is a QRCode in the image
    if data:
       print(bbox,data)
       #Open QR in web browser
       webbrowser.open(str(data))
       time.sleep(5)
       #break
    cv2.imshow('QR CODE scanner', frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()