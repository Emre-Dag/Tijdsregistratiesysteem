from picamera import PiCamera, Color

camera = PiCamera()
camera.resolution = (640,480)

camera.capture('/home/pxl/Desktop/image.jpg')