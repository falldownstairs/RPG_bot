#use this for general encounters
class Encounter():
    def __init__(self,encounter_dialogue,npc, game, is_random):
        self.encounter_dialogue = encounter_dialogue
        self.attached_game = game
        self.is_random = is_random

    def interact(self):

        #do stuff
        self.attached_game.is_ok_to_continue = True
         
    

# use this for encounters that advance a player to another area    
class Advance_To_Next_Area_Event(Encounter):
    def __init__(self, encounter_dialogue,npc, game, next_area, is_random):
        Encounter.__init__(self, encounter_dialogue,npc, game, is_random)
        self.attached_game = game
        self.next_area = next_area

    def advance_to_next_area(self):
        self.attached_game.current_area = self.next_area
        self.attached_game.current_encounter = current_area.encounters[0]
        self.attached_game.current_encounter.attached_game = self.attached_game
        self.is_ok_to_continue = False

    def interact(self):
        #do stuff
        advance_to_next_area()
        self.attached_game.is_ok_to_continue = True


# use this for encounters that come one after another
class Advance_To_Next_Encounter_Event(Encounter):
    def __init__(self,encounter_dialogue,npc, game, next_encounter, is_random):
        Encounter.__init__(self, encounter_dialogue,npc, game, is_random)
        self.game_to_advance = game
        self.next_encounter = next_encounter

    def advance_to_next_encounter(self):
        self.attached_game.current_encounter = self.next_encounter

    def interact(self):
        #do stuff
        self.advance_to_next_encounter()
        self.attached_game.is_ok_to_continue = False


#use this for merchant encounters
#class Merchant_Encounter(Encounter):
 #   def __init__(self,encounter_dialogue,npc, game, merchant_npc):
 #       Encounter.__init__(encounter_dialogue,npc, game)
 #       self.merchant = merchant_npc

#use this for encounters with up to 4 choices
class Choice_Encounter(Encounter):
    def __init__(self,encounter_dialogue,npc, game, choice1_encounter, choice2_encounter, choice3_encounter, choice4_encounter, num_of_choices, is_random):
        Encounter.__init__(self, encounter_dialogue,npc, game, is_random)
        self.encounter_dialogue = encounter_dialogue
        self.attached_game = game
        self.choice1 = choice1_encounter
        self.choice2 = choice2_encounter
        self.choice3 = choice3_encounter
        self.choice4 = choice4_encounter
        self.num_choices = num_of_choices


    def interact(self, choice_num):
        if choice_num > self.num_choices:
            return

        if choice_num == 1:
            if self.choice1 == None:
                self.attached_game.is_ok_to_continue = True
                self.attached_game.current_encounter = None
                return
            self.attached_game.current_encounter = self.choice1_encounter

        elif choice_num == 2:
            if self.choice2 == None:
                self.attached_game.is_ok_to_continue = True
                self.attached_game.current_encounter = None
                return
            self.attached_game.current_encounter = self.choice2_encounter

        elif choice_num == 3:
            if self.choice3 == None:
                self.attached_game.is_ok_to_continue = True
                self.attached_game.current_encounter = None
                return
            self.attached_game.current_encounter = self.choice3_encounter

        elif choice_num == 4:
            if self.choice4 == None:
                self.attached_game.is_ok_to_continue = True
                self.attached_game.current_encounter = None
                return
            self.attached_game.current_encounter = self.choice4_encounter

        #do stuff
        self.attached_game.is_ok_to_continue = False


class Combat_Encounter(Encounter):
    def __init__(self,encounter_dialogue,npc, game, successful_fight_encounter, enemy, is_random):
        Encounter.__init__(self, encounter_dialogue,npc, game, is_random)
        self.encounter_dialogue = encounter_dialogue
        self.attached_game = game
        self.successful_fight_encounter  = successful_fight_encounter
        self.enemy = enemy

    def interact(self):
        #creates button-enabled UI for fight




        #loop while fight is going on
        if self.attached_game.player.health > 0 or enemy.health > 0:
            return self.enemy

        #do stuff
        self.attached_game.is_ok_to_continue = True