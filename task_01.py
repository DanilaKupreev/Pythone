def is_palindrome(x):
    y=[",","'",".","/","<",">","?",";",":","[","]","{","}","-","_","+","=",")","(","*","&","^","%","$","#","@","!","`","~","№"," "]
    a=[]
    x=str(x)
    for i in x:
        if i not in y:
            a.append(i.lower())
    if a[0:]==a[::-1]:
        c=True
    else:
        c=False
    return c