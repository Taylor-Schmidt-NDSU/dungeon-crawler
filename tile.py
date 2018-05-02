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
	def TrapTile(self, image, location, damage):
		self.super(image, location)
		self.damage = damage

class ItemTile(Tile):
	def ItemTile(self, image, location, item):
		self.super(image, location)
		self.item = item
	def give_item(self, player):
		#need to discuss how item pickup should work

class FloorTile(Tile):
	def FloorTile(self, image, location):
		self.super(image, location)

class WallTile(Tile):
	def WallTile(self, image, location):
		self.super(image, location)
		self.traversable = False
		
class HiddenTile(Tile):
	def HiddenTile(self, image, location):
		self.super(image, location)
	