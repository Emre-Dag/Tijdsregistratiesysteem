import cv2
import picamera
import picamera.array

detector = cv2.QRCodeDetector()

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        while True:
            camera.capture(stream, format='bgr')
            image = stream.array
            data, bbox, _ = detector.detectAndDecode(image)
            #img = cv2.imdecode(data, 1)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # check if there is a QRCode in the image
            if data:
                webbrowser.open(str(data))
                time.sleep(5)
                break
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
# reset the stream before the next capture
stream.seek(0)
stream.truncate()

cv2.destroyAllWindows()