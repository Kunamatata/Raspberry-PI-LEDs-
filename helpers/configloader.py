# import os
import json

def load(filename):
    with open(filename) as f:
        res = json.load(f)
        return res 
