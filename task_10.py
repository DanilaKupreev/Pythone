def count_words(x):
	y=[",","'",".","/","<",">","?",";",":","[","]","{","}","-","_","+","=",")","(","*","&","^","%","$","#","@","!","`","~","№",' ','\n']
	c=''
	a=[]
	b={}
	for i in x:
		if i not in y:
			c=c+str(i)
		if i == ' ':
			if c != '':
				a.append(c.lower())
			c=''
	a.append(c.lower())
	for i in a:
		c=a.count(i)
		if i not in b:
			b[i]=c
	return b

