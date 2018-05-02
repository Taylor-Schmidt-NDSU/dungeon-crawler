'''
Created on Apr 12, 2018

@author: taylor.n.schmidt
'''
from level import Level
from player import Player
class LevelManager():
    '''
    classdocs
    '''
    
    instance = None
    
    class __LevelManager():
        def __init__(self, players):
            self.level = self.load_level(1, players)
            
        def load_level(self, level_number, players):
                self.level = Level(level_number, players)
                self.level.initialize()
        
        def get_current_level(self):
            return self.level
        
        def leave_level(self):
            return self.players
        
        def advance_level(self):
            self.load_level(self.level.level_number, self.leave_level())

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __init__(self):
        if not LevelManager.instance:
            LevelManager.instance = LevelManager.__LevelManager(Player())