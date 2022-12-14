class MyError(Exception):
	pass

def rps_game_winner(x):
	y = ["S","R","P"]
	if len(x)==2:
		if x[0][1] in y and x[1][1] in y:
			if x[0][1]=='P':
				if x[1][1]=='R':
					a=x[0][0]+' '+x[0][1]
				elif x[1][1]=='P':
					a=x[0][0]+' '+x[0][1]
				else:
					a=x[1][0]+' '+x[1][1]
			if x[0][1]=='R':
				if x[1][1]=='R':
					a=x[0][0]+' '+x[0][1]
				elif x[1][1]=='S':
					a=x[0][0]+' '+x[0][1]
				else:
					a=x[1][0]+' '+x[1][1]

			if x[0][1]=='S':
				if x[1][1]=='S':
					a=x[0][0]+' '+x[0][1]
				elif x[1][1]=='P':
					a=x[0][0]+' '+x[0][1]
				else:
					a=x[1][0]+' '+x[1][1]
			return a
		else:
			raise MyError("NoSuchStrategyError")
	if len(x)!=2:
		raise MyError("WrongNumberOfPlayersError")
