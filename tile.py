import constants
import pygame

class Tile():
	
	location = (0,0)
	traversable = False
	def __init__(self, location):
		self.location = location
		self.traversable = True
		self.image = pygame.image.load(self.image_name).convert_alpha()
	def update(self):
		#add generic update function if needed
		pass
	
	def draw(self, screen):
		true_x_value = constants.TILE_WIDTH * self.location[0]
		true_y_value = constants.TILE_HEIGHT * self.location[1]
		print("drawing tile")
		screen.blit(self.image, (true_x_value, true_y_value))
		
class TrapTile(Tile):
	image_name = "res/tile.png"
	def __init__(self, location, damage):
		super( location)
		self.damage = damage

class ItemTile(Tile):
	image_name = "res/tile.png"
	def __init__(self, location, item):
		super(ItemTile, self).__init(location)
		self.item = item
	def give_item(self, player):
		#need to discuss how item pickup should work
		pass
	
class FloorTile(Tile):
	image_name = "res/tile.png"
	def __init__(self, location):
		super(FloorTile, self).__init__(location)

class WallTile(Tile):
	image_name = "res/tile.png"
	def __init__(self, location):
		super(WallTile, self).__init__(location)
		self.traversable = False
		
class HiddenTile(Tile):
	image_name = "res/tile.png"
	def __init__(self, location):
			super(HiddenTile, self).__init__(location)	