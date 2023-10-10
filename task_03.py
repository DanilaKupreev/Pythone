def max_odd(x):
    lower = 0

    for i in x:
        try:
            if int(i)%2==1 and i>lower:
                lower = i
        except:
            pass
    
    if lower != 0: 
        return int(lower)
    
