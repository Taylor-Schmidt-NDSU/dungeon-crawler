'''
Created on Apr 30, 2018

@author: taylor.n.schmidt
'''

class Game_Object(object):
    '''
    classdocs
    '''


    def __init__(self, location):
        '''
        Constructor
        '''
        self.x = location[0]
        self.y = location[1]
        