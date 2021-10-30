"""
    File: prob3.py
    Author: Xin Li
    Purpose: In this program
"""
class Room:
    def __init__(self,name):
        self._name = name
        self.n = None
        self.e = None
        self.s = None
        self.w = None
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name
    def collapse_room(self):
        if self.s is not None:
            self.s.n  = None
        if self.n is not None:
            self.n.s = None
        if self.e is not None:
            self.e.w = None
        if self.w is not None:
            self.w.e = None

        self.n = None
        self.e = None
        self.s = None
        self.w = None


def build_grid(wid,hei):
    lst = []
    for b in range(hei):
        lst1 = []
        for a in range(wid):
            lst1.append(Room('('+str(a)+','+str(b)+')'))
        lst.append(lst1)
    for i in range(hei):
        for j in range(wid):
            if i != 0:
                lst[i][j].n = lst[i-1][j]
            if i != hei-1:
                lst[i][j].s = lst[i+1][j]
            if j != 0:
                lst[i][j].w = lst[i][j-1]
            if j != wid-1:
                lst[i][j].e = lst[i][j+1]
    return lst[hei-1][0]
