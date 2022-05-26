from djitellopy import tello
from time import sleep

me = tello.Tello() # set the tello library
me.connect() # connect function
print(me.get_battery())

