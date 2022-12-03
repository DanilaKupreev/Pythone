def sort_list(x):
    try:
        a=max(x)
        b=min(x)
        c=[]
        for i in x:
            if a == i:
                c.append(b)
            elif b == i:
                c.append(a)
            else:
                c.append(i)
        c.append(b)
    except:
        c=[]
    return c
