"""
    File: prob2.py
    Author: Xin Li
    Purpose: In this program
"""
class Color:
    def __init__(self, r,g,b):
        if r> 255:
            r = 255
        if r< 0:
            r =0
        if g> 255:
            g = 255
        if g< 0:
            g =0
        if b> 255:
            b = 255
        if b< 0:
            b =0
        self._r = r
        self._g = g
        self._b = b

    def __str__(self):
        return 'rgb('+str(self._r)+','+str(self._g)+','+str(self._b)+')'
    def html_hex_color(self):
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}"
    def get_rgb(self):
        return (self._r, self._g, self._b)
    def set_standard_color(self, name):
        assert name.lower() =='red' \
        or name.lower() == 'yellow' \
        or name.lower() == 'white' \
        or name.lower() == 'black'
        if name.lower() =="red":
            self._r = 255
            self._g = 0
            self._b = 0
        if name.lower() =="yellow":
            self._r = 255
            self._g = 255
            self._b = 0
        if name.lower() =="black":
            self._r = 0
            self._g = 0
            self._b = 0
        if name.lower() =="white":
            self._r = 255
            self._g = 255
            self._b = 255
    def remove_red(self):
        self._r = 0
