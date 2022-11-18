def palindrom(x):
    f = x
    a = 0
    b = -1
    c = []
    y =['!' , ',' , '.' , '/' , '-' , ';' , ':' , '$' , '=' , '`' , '~' ,'@' , '#' , '%','^','&','*','_','+','<','>' ,'?']
    for i in f:
        g=i
        for i in g:
            v = i.lower()
            if v not in y:
                c.append(v.split())
    if c[0:]==c[::-1]:
        x = 'Это палиндром'
    else:
        x = "Это не палиндром"
    
    return x 
while True:    
    a = input().strip().split()
    print(palindrom(a))
