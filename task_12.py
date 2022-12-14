class Dessert:
	def __init__(self, x=None, y=None):
		self.name=x
		self.calories=y
		
	def __get__(self,x):
		return self.__x
	
	def __set__(self,x):
		self.x=x
	
	def is_healthy(self):
		try:
			if self.calories<200:
				return True
			else:
				return False
		except:
			return False
	
	def is_delicious(self):
		if JellyBean.alt != "black licorice":
			return True
		else:
			return False

class JellyBean(Dessert):
	alt=""
	def __init__(self, x=None):
		self.name=x
	@property
	def flavor(self):
		self.name
	@flavor.setter
	def flavor(self,x):
		JellyBean.alt=x
		self.name=x
	@flavor.getter
	def flavor(self):
		return self.name
