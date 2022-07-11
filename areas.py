#define all areas here
from area import *
from enemies import *

starting_area = Area("Starting Area", "A place for all adventurers to start", [])

plains = Area("plains","not much to see here, other than some enemies",[])

haunted_forest = Area("forest","it is quiet among the trees. There are things moving in the shadows...",[])

#define all encounters here
npc_encounter_oneA = Encounter("i hear your trying to deafeat the dragon, haha what a foolish goal for a scrawny guy like you",None,None, True)

npc_encounter_twoA = Encounter("a random guy eyes you and gets a smug look on his face",None,None, True)

fight_wolf = Combat_Encounter("you have encountered a wolf!",None,None,True,wolf, True)

fight_slime = Combat_Encounter("you have encountered a slime!",None,None,True,slime, True)

fight_boar = Combat_Encounter("you have encountered a boar!",None,None,True,boar, True)

fight_orc = Combat_Encounter("you have encountered a orc!",None,None,True,orc, True)

fight_goblin = Combat_Encounter("you have encountered a goblin!",None,None,True,goblin, True)

advance_next_areaA = Advance_To_Next_Area_Event("you are now entering the forest area!",None,None, haunted_forest , True)

Advance_oneA = Advance_To_Next_Encounter_Event("you deafeated the goblin!",None,None,npc_encounter_oneA, False)

Advance_twoA = Advance_To_Next_Encounter_Event("after the odd encounter with the smug traveller you see some bushes rustling",None,None,fight_slime, False)

Advance_threeA = Advance_To_Next_Encounter_Event("after the encounter with the slime a shadowy figure emerges from behind you!", None, None,fight_orc, False)

Advance_fourA = Advance_To_Next_Encounter_Event("you see a path behind the orc you just defeated it where could it lead?",None,None,advance_next_areaA, False)

Start_Encounter = Encounter("You set out on an adventure. You don't have much right now ", None, None, False)


#assign lists of encounters in an area here
starting_area.set_encounters([Start_Encounter, npc_encounter_oneA, npc_encounter_twoA, fight_wolf, fight_slime, fight_boar, fight_orc,fight_goblin, advance_next_areaA, Advance_oneA, Advance_twoA, Advance_threeA, Advance_fourA])

haunted_forest.set_encounters([])