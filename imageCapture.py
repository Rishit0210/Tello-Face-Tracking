from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
sleep(2)

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (640, 480))
    cv2.imshow('Drone', img)
    cv2.waitKey(1)
