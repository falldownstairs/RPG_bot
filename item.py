
class Item():

	def __init__(self, price, name, description):
		self.price = price
		self.name = name
		self.desc = description

	def interact(self):
		pass

class Equippable(Item):

	def __init__(self, price, name, desc, affected_stat, effect_value, equip_type):
		Item.__init__(price, name, desc)
		self.affected_stat = effect_value
		self.effect_value = effect_value
		self.type = equip_type

	def interact(self, player):
		if self.type == "headgear":
			if player.headgear != None:
				player.inventory.append(player.headgear)
			player.headgear = self
		elif self.type == "torso":
			if player.torso != None:
				player.inventory.append(player.torso)
			player.torso = self
		elif self.type == "footwear":
			if player.footwear != None:
				player.inventory.append(player.footwear)
			player.footwear = self
		elif self.type == "weapon":
			if player.weapon != None:
				player.inventory.append(player.weapon)
			player.weapon = self
		player.inventory.remove(self)




class Consumable(Item):

	def __init__(self, price, name, desc, effect_type, effect_value):
		Item.__init__(price, name, desc)
		self.effect_type = effect_type
		self.effect_value= effect_value

	def interact(self, player):
		if self.effect_type == "health":
			player.health += self.effect_value
		elif self.effect_type == "armor":
			player.armor += self.effect_value
		elif self.effect_type == "attack":
			player.attack += self.effect_value

		player.inventory.remove(self)

