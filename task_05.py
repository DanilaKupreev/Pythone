def date_in_future(x):
	from datetime import datetime
	d=datetime.now()
	a=d.strftime('%d-%m-%Y %H:%M:%S')
	if x !=[]:
		import datetime
		c=int(x)
		b=datetime.datetime.now() + datetime.timedelta(days=c)
		a=b.strftime('%d-%m-%Y %H:%M:%S')
	return a