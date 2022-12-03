def multiply_numbers(x=None):
	a=1
	try:
		for i in x:
			try:
				a=a*int(i)
			except:
				a=a
	except:
		a=a
	
	try:
		if x == float(x):
			s=str(x)
			for i in s:
				try:
					a=a*int(i)
				except:
					a=a
	except:
		a=a
	if x==None:
		a=None
	if a == 1:
		a=None
	return a