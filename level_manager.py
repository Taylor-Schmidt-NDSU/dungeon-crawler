'''
Created on Apr 12, 2018

@author: taylor.n.schmidt
'''
from level import Level

class Level_Manager():
    '''
    classdocs
    '''
    


    def __init__(self, params):
        '''
        Constructor
        '''
     
    class __Level_Manager():
        
        def __init__(self, players):
            self.level = Level(1, players)
            self.level.initialize()
            
        def load_level(self, level_number, players):
                self.level = Level(level_number, players)
                self.level.initialize()