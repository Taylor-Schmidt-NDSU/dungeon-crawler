class Inventory():
	def __init__(self, max_items, items=[]):
		self.max_items = max_items
		self.items = items
	def add(self, item):
		if self.items.length < self.max_items :
			self.items.add(item)
		else:
			#figure out what to do with too many
	def remove(self, item):
		if self.items.contains(item):
			self.items.remove(item)
		else:
			#figure out error to throw
			
	