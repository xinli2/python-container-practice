"""
    File: prob1.py
    Author: Xin Li
    Purpose: In this program, it will have one class each
    (Color, and Room, respectively).
"""

class Simplest:
    def __init__(self,val1,val2,val3):
        self.a = val1
        self.b = val2
        self.c = val3



class Rotate:
    def __init__(self,first,second,third):
        self._first = first
        self._second = second
        self._third = third
    def get_first(self):
        return self._first
    def get_second(self):
        return self._second
    def get_third(self):
        return self._third
    def rotate(self):
        temp = self._first
        self._first = self._second
        self._second = self._third
        self._third = temp




class Band:
    def __init__(self,singer):
        '''
        Constructor. It should store the singer it is passed,
        set the drummer to None, and record that the band
        dose not (yet) have any guitar players.
        '''
        self._singer = singer
        self._drummer = None
        self._guitar_player = []
    def get_singer(self):
        return self._singer
    def set_singer(self,new_singer):
        self._singer = new_singer
    def get_drummer(self):
        return self._drummer
    def set_drummer(self, new_drummer):
        self._drummer = new_drummer
    def add_guitar_player(self, new_guitar_player):
        self._guitar_player.append(new_guitar_player)
    def fire_all_guitar_players(self):
        self._guitar_player = []
    def get_guitar_players(self):
        return self._guitar_player[:]
    def play_music(self):
        if self._singer =="Frank Sinatra":
            print('Do be do be do')
        elif self._singer =="Kurt Cobain":
            print('bargle nawdle zouss')
        else:
            print("La la la")
        if self._drummer != None:
            print("Bang bang bang!")
        for i in self._guitar_player:
