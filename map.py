from tile import *

class Map():
	tiles = []
	
	def __init__(self):	
		self.generate(1)
	def generate(self, level):
		for row in ([WallTile((0,0)), WallTile((1,1)), WallTile((0,2)), WallTile((0,3)), WallTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), FloorTile((0,1)), FloorTile((0,2)), FloorTile((0,3)), FloorTile((0,4)), WallTile((0,5))],
					[WallTile((0,0)), WallTile((0,1)), WallTile((0,2)), WallTile((0,3)), WallTile((0,4)), WallTile((0,5))]):
			self.tiles.append(row)
					
	def update(self):
		for row in self.tiles:
			for tile in row:
				tile.update()
	
	def draw(self, screen):
		for row in self.tiles:
			for tile in row:
				tile.draw(screen)