#use this for general encounters
class Encounter():
    def __init__(self,encounter_dialouge,npc):
        self.encounter_dialouge = encounter_dialouge
        self.npc = npc
        pass
    def interact(self):
        pass
    

# use this for encounters that advance a player to another area    
def Advance_To_Next_Area_Event(Encounter):
    def __init__(self,game, next_area):
        super.__init__()
        self.game_to_advance = game
        self.next_area = next_area

    def advance_to_next_area(self):
        self.game_to_advance.area = self.next_area


# use this for encounters that come one after another
def Advance_To_Next_Encounter_Event(Encounter):
    def __init__(self,game, next_encounter):
        super.__init__()
        self.game_to_advance = game
        self.next_encounter = next_area

    def advance_to_next_encounter(self):
        self.game_to_advance.current_encounter = self.next_area