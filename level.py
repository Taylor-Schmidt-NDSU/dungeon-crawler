from map import Map
from player import Player


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
		
	generate_enemies(num_of_enemies):
	