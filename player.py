import entity



class Player(entity):
    def __init__(self,health):
        super.__init__(health)
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

        iten.interact()
        self.inventory.remove(item)

    def attack(self):
        pass


    
   

    

