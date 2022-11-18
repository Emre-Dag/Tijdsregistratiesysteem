#https://www.geeksforgeeks.org/webcam-qr-code-scanner-using-opencv/

import cv2
import webbrowser
from picamera import PiCamera
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cam = PiCamera()
detector = cv2.QRCodeDetector()
# Check if camera opened successfully
if (cam.start_preview() == False):
  print("Error opening video stream or file")

# Read the video
while(cam.start_preview()):
    check, frame = cam.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(frame)
    # check if there is a QRCode in the image
    if data:
       a=data
       b=webbrowser.open(str(a))
       break
    cv2.imshow('QRCODEscanner', frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()