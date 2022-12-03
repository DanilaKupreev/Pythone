def combine_anagrams(x):
	z=sorted(x)
	a,c=[],[]
	t=0
	v=''
	for i in z:
		for i2 in x:
			if sorted(i) == sorted(i2):
				if i2 not in a:
					v=str(i2)
					a.append(v)
	z=[]
	for t in range(len(a)-1):
		if sorted(a[t]) == sorted(a[t+1]):
			c+=[str(a[t])]
		elif sorted(a[t]) != sorted(a[t+1]):
			c+=[str(a[t])]
			z.append(c)
			c=[]
		else:
			c=[]
	if sorted(a[-1]) not in z:
		z.append([a[-1]])
	if len(a)==2:
		if sorted(a[0])==sorted(a[1]):
			z=[]
			c=[a[0]]+[a[1]]
			z.append(c)
	return z