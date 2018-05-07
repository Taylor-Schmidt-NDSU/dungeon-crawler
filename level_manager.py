'''
Created on Apr 12, 2018

@author: taylor.n.schmidt
'''
from level import Level
from player import Player
from keystroke_manager import KeystrokeManager

class LevelManager():
    '''
    classdocs
    '''
    
    instance = None
    
    class __LevelManager():
        players = []
        def __init__(self):
            self.players.append(Player())
            self.level = self.load_level(1)
            self.keystroke_manager = KeystrokeManager()
            
        def load_level(self, level_number):
                return Level(level_number)
                
        
        def get_current_level(self):
            return self.level
        
        def leave_level(self):
            pass
        
        def advance_level(self):
            self.load_level(self.level.level_number, self.leave_level())
            
        def handle_keyboard_event(self, event):
            self.keystroke_manager.handle_keyboard_event(event, self.players[0])
        
        def update_level(self, screen):
            self.players[0].update(screen)
            self.level.update(screen)
            
        def draw_level(self, screen):
            self.players[0].draw(screen)
            self.level.draw(screen)

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __init__(self):
        if not LevelManager.instance:
            LevelManager.instance = LevelManager.__LevelManager()
    
    