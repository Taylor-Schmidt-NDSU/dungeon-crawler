'''
Created on Feb 13, 2018

@author: taylor.n.schmidt
'''
import pygame

class GameSprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''

# init method that works with sprite sheets, haven't implemented yet
#     def __init__(self, image_details):
#         '''
#         image_details [image_name, columns, rows]
#         will create frame_image and frames[] automatically so it has required attributes for sprite class
#         '''
#         super().__init__()
#         image_name = image_details[0]
#         columns = image_details[1]
#         rows = image_details[2]
#         self.frame_image = pygame.image.load(image_name).convert_alpha()
#         self.frame_width = self.frame_image.get_width() / columns
#         self.frame_height = self.frame_image.get_height() / rows
#         self.frames = self.get_frames_from_sheet(self.frame_image, (0,0), (self.frame_width, self.frame_height), columns, rows)
#         self.image = self.frames[0]
#         self.image_count = 1
    def __init__(self, image_name):
        super().__init__()
        self.image = pygame.image.load(image_name).convert_alpha()
          
    def get_frames_from_sheet(self, sheet, start, sprite_size, columns, rows = 1):
        
        
        frames = []
        
        for row in range(0, rows):
            for column in range(0, columns):
                frame_rect = pygame.Rect(start[0] + sprite_size[0] * column, start[1] + sprite_size[1] * row, sprite_size[0], sprite_size[1] )
                frame = sheet.subsurface(frame_rect)
                frames.append(frame)
        
        
        return frames
    
    def draw(self, screen):  
        screen.blit(self.image, (self.location[0], self.location[1]))