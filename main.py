'''
Created on Apr 30, 2018

@author: taylor.n.schmidt
'''
import pygame
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