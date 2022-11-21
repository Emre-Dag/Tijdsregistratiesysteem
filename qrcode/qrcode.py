#most importantly for this code to run is to import OpenCV which we do in the below line
import cv2

# set up camera object called Cap which we will use to find OpenCV
cap = cv2.VideoCapture(0)

# QR code detection Method
detector = cv2.QRCodeDetector()

#This creates an Infinite loop to keep your camera searching for data at all times
while True:
    
    # Below is the method to get a image of the QR code
    _, img = cap.read()
            
    # Below will display the live camera feed to the Desktop on Raspberry Pi OS preview
    cv2.imshow("code detector", img)
    
    #At any point if you want to stop the Code all you need to do is press 'q' on your keyboard
    if(cv2.waitKey(1) == ord("q")):
        break
    
# When the code is stopped the below closes all the applications/windows that the above has created
cap.release()
cv2.destroyAllWindows()