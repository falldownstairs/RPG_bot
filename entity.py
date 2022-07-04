class Entity():
    def ___init__(self,health, armor, attack):
        self.health = health
        self.armor = armor
        self.attack = attack
        pass
    def attack(self):
        pass
    def skill(self):
        pass
    def die(self):
        pass
    def defend(self):
        pass

class Enemy(Entity):
    def __init__(self,health, armor, attack, name, description):
        Entity.__init__(health, armor, attack)
        self.name = name
        self.description = description
    def loot(self):
        pass


class Player(Entity):
    def __init__(self,health, armor, attack):
        Entity.__init__(health, armor, attack)
        self.head_armor = None
        self.body_armor = None
        self.footwear = None
        self.weapon = None
        self.inventory = []
   
    def use_item(self, item_name):
        item = None
        for i in self.inventory:
            if i.name == item_name:
                item = i

        item.interact()
        self.inventory.remove(item)

    def attack(self):
        pass


    
   

    

