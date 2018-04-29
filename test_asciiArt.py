# Title: ASCII Art Test
# Date: 2018-04-29
# Author: Zachary Welk
# Description: Test class for ASCII Art

import unittest, asciiArt

class TestAsciiArt(unittest.TestCase):
    def test_output(self, f, a, q):
        #Tests that the output of the function 'f' with args 'a'matches output 'q'
        self.assertMultiLineEqual(first=f(a*), second=q)
        self.assertRaises(TypeError)
