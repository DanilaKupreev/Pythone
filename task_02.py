def coincidence(x=None,y=None):
    a=[]
    c=0
    
    try:
        for i in x:    
            try:
                if int(i) in y:
                    a.append(i)
            except:
                c+=1
    except:
        c+=1
    return a
