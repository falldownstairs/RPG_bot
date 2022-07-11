#represents a game
from areas import *
from entity import *

class Game():

	def __init__(self, thread_id, player_id, desc):
		self.thread_id = thread_id
		self.player_id = player_id
		self.current_area = starting_area
		self.current_area.game = self
		#makes sure that player starts in the starting area, with the first encounter in the list
		self.current_encounter = starting_area.encounters[0]
		self.current_encounter.attached_game = self
		self.player = Player(100, 0, 10)
		self.is_ok_to_continue = False
		self.desc = desc

	def getTid(self):
		return self.thread_id

	def getPid(self):
		return self.player_id

	def getDesc(self):
		return self.desc

	def get_current_encounter(self):
		return self.current_encounter

		
	def set_current_encounter(self, encounter):
		self.current_encounter = encounter

	def get_current_area(self):
		return self.current_area 

	def set_current_area(self, area):
		self.current_area = area