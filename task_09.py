def connect_dicts(x,y):
	a={}
	z,v=0,0
	for i in x:
		z+=x[i]
	for i in y:
		v+=y[i]
	
	if z>v:
		for i in x:
			if x[i] >= 10:
				a[i]=x[i]
		for i in y:
			if i not in a and y[i]>=10:
				a[i]=y[i]
	elif z<v or z==v:
		for i in y:
			if y[i] >= 10:
				a[i]=y[i]
		for i in x:
			if i not in a and x[i]>=10:
				a[i]=x[i]
	sorted_rooms = dict(sorted(a.items(), key=lambda item: item[1]))
	a=sorted_rooms
	return a