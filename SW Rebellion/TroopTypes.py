import numpy as np


class Trooper():
    
    def __init__(self):

        self.hp = 1
        self.max_hp = 1
        self.black_die = 1
        self.red_die = 0
    
    def is_dead(self):
        return self.hp <= 0

class Walker():

    def __init__(self):
        self.hp = 2
        self.max_hp = 2
        self.black_die = 1
        self.red_die = 1

    def is_dead(self):
        return self.hp <= 0


     
