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
		if JellyBean.flavor()==False:
			return False
		if self.name != None:
			return True

class JellyBean(Dessert):
	alt=""
	def __init__(self, name=None):
		self.name=name
		JellyBean.alt=name
	
	def __get__(self,x):
		return self.__x
	
	def __set__(self,x):
		self.x=x
		print("dxfgv")
	
	@staticmethod
	def flavor():
		if JellyBean.alt=="black licorice":
			return False