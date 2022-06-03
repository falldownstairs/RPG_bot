import entity

class enemy(entity):
    def ___init__(self,health):
        super.__init__()
    def loot(self):
        pass


# plains terrain enemies
class goblin(enemy):
    pass
   
class wolf(enemy):
    pass

class boar(enemy):
    pass

class orc(enemy):
    pass

class slime(enemy):
    pass

# forest terrain enemies

class small_dinosaur(enemy):
    pass

class large_dinosaur(enemy):
    pass

class giant_spider(enemy):
    pass

class tree_monster(enemy):
    pass

class forest_goblin(enemy):
    pass

# mountain terrain enmies

class troll(enemy):
    pass

class stone_giant(enemy):
    pass

class horned_goat(enemy):
    pass

class mountain_wolf(enemy):
    pass

# desert terrain enemies

class scorpion(enemy):
    pass

class mummy(enemy):
    pass

class sand_giant(enemy):
    pass

class camel(enemy):
    pass

# cave terrain enemies

class large_rat(enemy):
    pass

class skeleton(enemy):
    pass

class large_bat(enemy):
    pass

class poisonous_spider(enemy):
    pass

# volcano terrain enemies

class dragon(enemy):
    pass

class fire_slime(enemy):
    pass

class large_fireant(enemy):
    pass

class black_skeletons(enemy):
    pass

# snowy mountains terrain enemies

class drake(enemy):
    pass

class ice_golem(enemy):
    pass

class polar_bear(enemy):
    pass

class yeti(enemy):
    pass

class white_wolf(enemy):
    pass