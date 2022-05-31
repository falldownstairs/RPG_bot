from item import Item

class Equippable(Item):

	def __init__(self, price, name, desc, affected_stat, effect_value):
		super.__init__(price, name, desc)
		self.affected_stat = effect_value
		self.effect_value = effect_value
