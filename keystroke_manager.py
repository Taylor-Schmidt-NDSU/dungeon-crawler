'''
Created on May 2, 2018

@author: taylor.n.schmidt
'''
import pygame

class KeystrokeManager(object):
    '''
    classdocs
    '''
    

    def __init__(self, params):
        '''
        Constructor
        '''
        #make sure player isn't moving
        self.player_movement_flags = [False, False, False, False]
        
    def handle_event(self, event, level):
        if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
            self.handle_movement(event, level)
            
    def handle_movement(self, event, level): 
        player_to_move = level.player[0]
        
        #key being pressed
        if event == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_to_move.move_up_flag = True
            elif event.key == pygame.K_a:
                player_to_move.move_down_flag = True
            elif event.key == pygame.K_s:
                player_to_move.move_left_flag = True
            elif event.key == pygame.K_d:
                player_to_move.move_right_flag = True
        #key being released
        if event == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_to_move.move_up_flag = False
            elif event.key == pygame.K_a:
                player_to_move.move_down_flag = False
            elif event.key == pygame.K_s:
                player_to_move.move_left_flag = False
            elif event.key == pygame.K_d:
                player_to_move.move_right_flag = False
        