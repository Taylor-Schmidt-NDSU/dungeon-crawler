from map import Map
from player import Player
import constants

class Level():
	map
	players = []
	enemies = []
	
	def __init__(self, level_number, players):

		#TODO: dynamically create enemies based on level_number
		for player in players:
			self.players.append(player)
		
		#Will set up players, enemies, and map
		self.initialize()
		
	def update(self):
		self.map.update()
		for player in self.players:
			player.update()
		for enemy in self.enemies:
			enemy.update()
	
	#TODO make it move player and enemies to correct location		
	def initialize(self):
		self.map = Map()
	
	def draw(self, screen):
		#clear the screen
		screen.fill(constants.WHITE)
		#draw everything
		self.map.draw(screen)
		for enemy in self.enemies:
			enemy.draw(screen)
		for player in self.players:
			player.draw(screen)