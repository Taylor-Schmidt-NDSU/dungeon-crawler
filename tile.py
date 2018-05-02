import constants

class Tile():
	image = ""
	location = (0,0)
	traversable = False
	def Tile(self, image, location):
		self.image = image
		self.location = location
		self.traversable = True
	def update(self):
		#add generic update function if needed
		pass
	def draw(self, screen):
		true_x_value = constants.TILE_WIDTH * self.location[0]
		true_y_value = constants.TILE_HEIGHT * self.location[1]
		screen.blit(self.image, (true_x_value, true_y_value))
		
class TrapTile(Tile):
	image = ""
	def __init__(self, location, damage):
		self.super(self.image, location)
		self.damage = damage

class ItemTile(Tile):
	image = ""
	def __init__(self, location, item):
		self.super(self.image, location)
		self.item = item
	def give_item(self, player):
		#need to discuss how item pickup should work
		pass
	
class FloorTile(Tile):
	image = ""
	def __init__(self, location):
		self.super(self.image, location)

class WallTile(Tile):
	image = ""
	def __init__(self, location):
		self.super(self.image, location)
		self.traversable = False
		
class HiddenTile(Tile):
	image = ""
	def __init__(self, location):
		self.super(self.image, location)
	