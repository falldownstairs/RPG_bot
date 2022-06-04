from item import Item

class Consumable(Item):

	def __init__(self, price, name, desc, effect_type, effect_value):
		super.__init__(price, name, desc)
		self.effect_type = effect_type
		self.effect_value= effect_value

	def interact(self, player):
		if effect_type == "health":
			player.health += effect_value
		elif effect_type == "armor":
			player.armor += effect_value
		elif effect_type == "attack":
			player.attack += effect_value

		player.inventory.remove(self)