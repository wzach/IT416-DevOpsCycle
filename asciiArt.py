# Title: ASCII Art
# Date: 2018-04-29
# Author: Zachary Welk
# Description: Imports, exports, and displays ASCII art

def openTXT(path):
    #if type(path) != type(b""):
    #    raise TypeError("Path must be a string")
    f = open(path, 'r')
    raw = f.read()
    f.close()
    return raw
