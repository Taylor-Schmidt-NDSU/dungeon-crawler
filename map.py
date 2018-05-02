from tile import *

class Map():
	tiles = []
	
		
	def generate(self, level):
		self.tiles.append([WallTile(), WallTile(), WallTile(), WallTile(), WallTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), FloorTile(), FloorTile(), FloorTile(), FloorTile(), WallTile()],
					[WallTile(), WallTile(), WallTile(), WallTile(), WallTile(), WallTile()])
					
	def update(self):
		for tile in self.tiles:
			tile.update()
	
	def draw(self, screen):
		for tile in self.tiles:
			tile.draw()