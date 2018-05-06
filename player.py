'''
Created on Apr 30, 2018

@author: taylor.n.schmidt
'''
from character import Character

class Player(Character):
    '''
    classdocs
    '''
    
    max_health = 100
    vel = 3
    
    def __init__(self, params):
        '''
        Constructor
        '''
        
        self.super.__init__(self.max_health)
        
        #Set movement flags all to false
        self.move_up_flag = False
        self.move_down_flag = False
        self.move_right_flag = False
        self.move_left_flag = False
    
    def update(self, screen):
        if self.move_up_flag:
            self.move_up(screen, self.vel)
        if self.move_down_flag:
            self.move_down(screen, self.vel)
        if self.move_left_flag:
            self.move_left(screen, self.vel)
        if self.move_right_flag:
            self.move_right(screen, self.vel)