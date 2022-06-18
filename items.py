from item import*

#consumables

health_potion = Consumable(200,"health potion","restores 30 health", "health", 30)

greater_health_potion = Consumable(500,"greater_health_potion","restores 60 health", "health", 60)

greatest_health_potion = Consumable(1000, "greatest_health_potion", "restores 100 health", "health", 60)

defense_potion = Consumable(300,"defense potion","adds 5 temperary armor", "armor", 5)

greater_defense_potion = Consumable(600,"greater_defense_potion","adds 10 temperary armor", "health", 10)

greatest_defense_potion = Consumable(1200, "greatest_defense_potion", "adds 15 temperary armor", "health", 15)

attack_potion = Consumable(300,"attack potion","adds 10 temperary attack", "attack", 10)

greater_attack_potion = Consumable(600,"greater_attack_potion","adds 20 temperary attack", "attack", 20)

greatest_attack_potion = Consumable(1200, "greatest_attack_potion", "adds 30 temperary attack", "attack", 30)

#equipables


#shop items
leather_helmet = Equippable(500,"leather_helmet","an old helmet made of leather","armor", 3 ,"headgear")

leather_torso = Equippable(600,"leather_torso","old leggings made of leather","armor", 4,"torso")

leather_boots = Equippable(400,"leather_boots","old boots made of leather","armor", 2 ,"footwear")

rusty_sword = Equippable(500, "rusty_sword","an old rusty sword that is on the verge of snapping in half","attack",10)

iron_helmet = Equippable(700,"iron_helmet","a helmet made of iron","armor", 4 ,"headgear")

iron_torso = Equippable(800,"iron_torso","leggings made of iron","armor", 5,"torso")

iron_boots = Equippable(600,"iron_boots","boots made of iron","armor", 4,"footwear")

iron_sword = Equippable(800, "iron_sword","a decent sword made of iron","attack",14, "weapon")

steel_helmet = Equippable(900,"steel_helmet","helmet made of steel","armor", 5 ,"headgear")

steel_torso = Equippable(1000,"steel_torso","leggings made of steel","armor", 6,"torso")

steel_boots = Equippable(700,"steel_boots","boots made of steel","armor", 5,"footwear")

steel_sword = Equippable(900, "steel_sword","a good, sturdy sword made of solid steel","attack",20, "weapon")

platinium_helmet = Equippable(1200,"platinium_helmet","helmet made of platinium","armor", 8,"headgear")

platinium_torso = Equippable(1500,"platinium_torso","leggings made of platinium","armor", 9,"torso")

platinium_boots = Equippable(1100,"platinium_boots","boots made of platinium","armor", 7,"footwear")

platinium_sword = Equippable(1400, "platinium","a shiny, sharp and competant sword made of the world's finest platinium","attack",25, "weapon")


#enemy drops
goblin_dagger = Equippable(0,"goblin_dagger","a tiny but deadly dagger constructed by a goblin","attack",13, "weapon")

orc_club = Equippable(0, "orc_club","a oversized baseball bat made for a orc","attack", 15, "weapon")

dinosaur_teeth_sword = Equippable(0, "dinosaur_teeth_sword","a sword created from a large_dinosaur's teeth","attack", 18, "weapon")

mountain_wolf_coat = Equippable(0,"mountain_wolf_coat","a warm fuzzy coat made from a wolf's fur that is very sturdy","armor",6, "weapon")

scorpion_exoskeleton_helmet = Equippable(0, "scorpion_exoskeleton_helmet","a helmet made of the scorpian's hard exoskeleton","armor",7 ,"headgear")

skeletons_helmet = Equippable(0,"skeleton's_helmet","a helmet worn by the skeletons who dwell in the caves biome","armor",7 ,"headgear")

poisonous_spiders_leg = Equippable(0,"poisonous_spiders_leg","this spider's leg is actually very sharp and deadly","attack", 22)

yeti_fur_coat = Equippable(0,"yeti_fur_coat","a fur coat made from a yeti's fur, very nice and cozy","armor",10, "weapon")

black_skeleton_sword = Equippable(0,"black_skeleton_sword","a sword dropped by black skeletons, very very sharp","attack",30, "weapon")







