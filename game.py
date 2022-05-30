#represents a game

class Game():

	def __init__(self, thread_id, player_id):
		self.thread_id = thread_id
		self.player_id = player_id

	def getTid(self):
		return self.thread_id

	def getPid(self):
		return self.player_id