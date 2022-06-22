import math
import encounters
from encounter import *
import random

class Area():
    def __init__(self,name,description, encounters):
        self.name = name
        self.description = description
        self.encounters = encounters
        self.game = None

    def get_next_encounter(self):
        #get next encounter and then load it with game
        #replace this later
        next_enounter = None

        #find a non-random encounter
        while next_enounter == None:
            selected = self.encounters[random.choice(range(0, len(self.encounters)))]
            if selected.is_random == True:
                next_enounter = selected

        #inject game into encounter instance
        next_enounter.attached_game = self.game

        return next_enounter