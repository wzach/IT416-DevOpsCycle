# Title: ASCII Art
# Date: 2018-04-29
# Author: Zachary Welk
# Description: Imports, exports, and displays ASCII art

def openASCII(path):
    if type(path) != type(""):
        raise TypeError("Path must be a string")
    f = open(path, 'r')
    raw = f.read()
    f.close
    return raw
