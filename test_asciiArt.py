# Title: ASCII Art Test
# Date: 2018-04-29
# Author: Zachary Welk
# Description: Test class for ASCII Art

import unittest
from asciiArt import *

#Such sample text, much unittest, wow
validOutput= \
"""░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█ very code
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌ such test
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█ much pass
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█ WoW
"""

class TestAsciiArt(unittest.TestCase):
    def test_import(self):
        #Tests that the openTXT function is working properly
        self.assertMultiLineEqual(first=validOutput, second=openTXT(b"test.txt"))

    # def test_types(self):
    #     self.assertRaises(TypeError, openTXT, False)
    #     self.assertRaises(TypeError, openTXT, True)
    #     self.assertRaises(TypeError, openTXT, tuple())
    #     self.assertRaises(TypeError, openTXT, list())
    #     self.assertRaises(TypeError, openTXT, dict())
    #     self.assertRaises(TypeError, openTXT, set())
    #     self.assertRaises(TypeError, openTXT, None)
print(validOutput)
