class Dessert:
	def __init__(self, x=None, y=None):
		self.name=x
		self.calories=y
	def __get__(self,x):
		return self.__x
	def is_healthy(self):
		try:
			if self.calories<200:
				return True
			else:
				return False
		except:
			return False

	def is_delicious(self):
		if self.name != None:
			return True
		else:
			return False


