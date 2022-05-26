import cv2
from djitellopy import tello
import time
from threading import Thread

counter = 1

me = tello.Tello ()
me.connect ()
print ( me.get_battery () )

keepRecording = True
me.streamon ()
frame_read = me.get_frame_read ()


def videoRecorder():
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('Drone.avi' + str(counter), cv2.VideoWriter_fourcc ( *'XVID' ), 30, (width, height) )

    while keepRecording:
        video.write ( frame_read.frame )
        time.sleep ( 1 / 30 )

    video.release ()


recorder = Thread ( target=videoRecorder )
recorder.start ()

time.sleep(20)

keepRecording = False
recorder.join ()