#use this for general encounters
class Encounter():
    def __init__(self,encounter_dialogue,npc, game):
        self.encounter_dialogue = encounter_dialogue
        self.attached_game = game
        self.attached_game.is_ok_to_continue = false

    def interact(self):

        #do stuff
        self.attached_game.is_ok_to_continue = false
         
    

# use this for encounters that advance a player to another area    
def Advance_To_Next_Area_Event(Encounter):
    def __init__(self, encounter_dialogue,npc, game, next_area,game):
        Encounter.__init__(encounter_dialogue,npc, game)
        self.attached_gamee = game
        self.next_area = next_area

    def advance_to_next_area(self):
        self.attached_game.area = self.next_area


# use this for encounters that come one after another
def Advance_To_Next_Encounter_Event(Encounter):
    def __init__(self,encounter_dialogue,npc, game, next_encounter):
        Encounter.__init__(encounter_dialogue,npc, game)
        self.game_to_advance = game
        self.next_encounter = next_area

    def advance_to_next_encounter(self):
        self.attached_game.current_encounter = self.next_area

#use this for merchant encounters
def Merchant_Encounter(Encounter):
    def __init__(self,encounter_dialogue,npc, game, merchant_npc):
        Encounter.__init__(encounter_dialogue,npc, game)
        self.merchant = merchant_npc

