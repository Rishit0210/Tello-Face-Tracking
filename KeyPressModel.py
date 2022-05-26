from djitellopy import tello
from time import sleep
import cv2
import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName)) # insert keyName into {}
    if keyInput[myKey]: # if valid input
        ans = True
    pygame.display.update()

    return ans

def main():
    #print(getKey("a"))

    if getKey("LEFT"):
        print('left key pressed')
    if getKey("RIGHT"):
        print('right key pressed')

if __name__ == '__main__':
    init()
    while True:
        main()
        sleep(0.1)
