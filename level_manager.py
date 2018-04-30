'''
Created on Apr 12, 2018

@author: taylor.n.schmidt
'''
from level import Level

class Level_Manager():
    '''
    classdocs
    '''
    
    instance = None
    
    class __Level_Manager():
        def __init__(self, players):
            self.level = self.load_level(1, players)
            
        def load_level(self, level_number, players):
                self.level = Level(level_number, players)
                self.level.initialize()
        
        def get_current_level(self):
            return self.level
        
        def leave_level(self, score = 0):
            #figure out of having a dedicated title screen will be best
            #self.level = titlescreen
            pass
        
        
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __init__(self):
        if not Level_Manager.instance:
            Level_Manager.instance = Level_Manager.__LevelManager()