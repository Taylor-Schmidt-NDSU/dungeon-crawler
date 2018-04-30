'''
Created on Apr 30, 2018

@author: taylor.n.schmidt
'''
from game_object import Game_Object

class Character(Game_Object):
    '''
    classdocs
    '''
    

    def __init__(self, max_health):
        '''
        Constructor
        '''
        self.health = max_health
        self.max_health = max_health
    
    def move_up(self, screen, vel = 3):
        #ensures char cannot move off of screen
        self.y = max(self.y-vel, 0)
        
    def move_down(self, screen, vel = 3):
        #ensures char cannot move off of screen
        self.y = min(self.y + vel, screen.get_height() - self.image.get_height())
        
    def move_left(self, screen, vel = 3):
        #ensures char cannot move off of screen
        self.x = max(self.x-vel, 0)
        
    def move_right(self, screen, vel = 3):
        #ensures char cannot move off of screen
        self.y = min(self.y + vel, screen.get_width() - self.image.get_width())