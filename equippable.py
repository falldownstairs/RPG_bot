from item import Item

class Equippable(Item):

	def __init__(self, price, name, desc, affected_stat, effect_value, equip_type):
		Item.__init__(price, name, desc)
		self.affected_stat = effect_value
		self.effect_value = effect_value
		self.type = equip_type

	def interact(self, player):
		if self.type == "headgear":
			if player.headgear != None:
				player.inventory.append(entity.headgear)
			player.headgear = self
		elif self.type == "torso":
			if player.torso != None:
				player.inventory.append(entity.torso)
			player.torso = self
		elif self.type == "footwear":
			if player.footwear != None:
				player.inventory.append(entity.footwear)
			player.footwear = self
		elif self.type == "weapon":
			if player.weapon != None:
				player.inventory.append(entity.weapon)
			player.weapon = self
		player.inventory.remove(self)