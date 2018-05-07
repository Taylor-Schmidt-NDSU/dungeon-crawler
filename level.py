from map import Map
from player import Player
import constants

class Level():
	map
	enemies = []
	
	def __init__(self, level_number):

		#TODO: dynamically create enemies based on level_number
		self.map = Map()
		
		
		
	def update(self, screen):
		self.map.update()
		for enemy in self.enemies:
			enemy.update(screen)
	
	#TODO: make it move player and enemies to correct location		
	
	def draw(self, screen):
		#clear the screen
		screen.fill(constants.WHITE)
		#draw everything
		self.map.draw(screen)
		for enemy in self.enemies:
			enemy.draw(screen)
