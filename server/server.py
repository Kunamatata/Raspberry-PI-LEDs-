import socket
import time
import board
import neopixel
import sys

from threading import Thread

import modules.rainbow as rainbow

sys.path.append('../')
from helpers import configloader as cfg


config = cfg.load('config.json')
BUFFER = config['socket']['buffer']

pixels = neopixel.NeoPixel(board.D18, config['pixels'])
pixels.fill((0,0,0))

def ledsFollowingMouse(mouseValue,pixels):
    value = int(data)
    if  value <= 255:
        value = value // 10
        pixels.show()
        for i in range(value):
            pixels[i] = (255,0,0)
            pixels.show()
        for j in range(value, len(pixels)):
            pixels[j] = (10,58,10)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((config['socket']['host'], config['socket']['port']))
    s.listen()

    while True: 
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)

            while True:
                data = conn.recv(BUFFER).decode()
                if data == "disconnect":
                    pixels.fill((0,0,0))
                    conn.close()
                    break
                elif data == "Rainbow":
                    while True:
                        rainbow.colorChase(pixels, (255,0,0), 0.5)
                        rainbow.rainbowCycle(pixels, 0)
                else:
                    ledsFollowingMouse(data, pixels)
                    



