import socket
import time
import sys
import lib.screen as screen

sys.path.append('../')
from helpers import configloader as cfg

config = cfg.load('config.json')

screenWidthInPixels = screen.getScreenWidth()
colorRange = 256

def generateValueWithinRange(value, newRange, oldRange):
    """
    Creates a new value which fits in a newRange e.g : [0,oldRange] into [0,newRange]
    @params value int the value being modified to fit inside the new range
    @params newRange int the new range we want e.g : [0,255]
    """
    return int((value * newRange) / oldRange)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((config['socket']['host'], config['socket']['port']))

    while True:
        command = input('Which command do you want to send: ')
        if command == "mouse":
            try:
                while True: 
                    p = screen.getCursorPosition()
                    # create a new range [0,255] from an old range [0, screenWidthInPixels]
                    newValue = generateValueWithinRange(p['x'], colorRange, screenWidthInPixels)
                    print(newValue)
                    s.sendall(str(newValue).encode())
                    time.sleep(0.02)
            except KeyboardInterrupt:
                pass
        elif command == "rainbow":
                s.sendall(command.encode())
        elif command == "disconnect":
            s.sendall(command.encode())
            s.close()
            break
            

