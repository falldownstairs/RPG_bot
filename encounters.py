from enemies import *
from encounter import *


npc_encounter_oneA = Encounter("i hear your trying to deafeat the dragon, haha what a foolish goal for a scrawny guy like you",None,None)

npc_encounter_twoA = Encounter("a random guy eyes you and gets a smug look on his face",None,None)

fight_wolf = Combat_Encounter("you have encountered a wolf!",None,None,True,wolf)

fight_slime = Combat_Encounter("you have encountered a slime!",None,None,True,slime)

fight_boar = Combat_Encounter("you have encountered a boar!",None,None,True,boar)

fight_orc = Combat_Encounter("you have encountered a orc!",None,None,True,orc)

fight_goblin = Combat_Encounter("you have encountered a goblin!",None,None,True,goblin)

advance_next_areaA = Advance_To_Next_Area_Event("you are now entering the forest area!",None,None)

Advance_oneA = Advance_To_Next_Encounter_Event("you deafeated the goblin!",None,None,npc_encounter_oneA)

Advance_twoA = Advance_To_Next_Encounter_Event("after the odd encounter with the smug traveller you see some bushes rustling",None,None,fight_slime)

Advance_threeA = Advance_To_Next_Encounter_Event("after the encounter with the slime a shadowy figure emerges from behind you!",fight_orc)

Advance_fourA = Advance_To_Next_Encounter_Event("you see a path behind the orc you just defeated it where could it lead?",None,None,advance_next_areaA)



