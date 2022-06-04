from item import Item

class Consumable(Item):

	def __init__(self, price, name, desc, effect_type, effect_value):
		super.__init__(price, name, desc)
		self.effect_type = effect_type
		self.effect_value= effect_value

	def interact(self, player):
		pass