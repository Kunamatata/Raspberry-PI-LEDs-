from ctypes import windll, Structure, c_long, byref
import struct

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def getCursorPosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def getScreenWidth():
    return windll.user32.GetSystemMetrics(0)