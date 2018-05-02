'''
Created on Apr 30, 2018

@author: taylor.n.schmidt
'''
import pygame
import constants
from level_manager import LevelManager

# Initialize Pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([constants.SCREEN_WIDTH,
                                  constants.SCREEN_HEIGHT])

clock = pygame.time.Clock()
 
level_manager = LevelManager()


done = False

# -------- Main Program Loop -----------
while not done: 
    
    
    level_manager.draw_level()
    level_manager.update_level()
    
    clock.tick(60)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
            break
        
        level_manager.handle_keyboard_event(event)