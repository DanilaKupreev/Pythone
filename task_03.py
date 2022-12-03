def max_odd(x):
    c=0
    a=1
    for i in x:
        try:
            if int(i) % 2 == 1:
                if i>c:
                    c=i
        except:
            a+=1
    if c == 0:
        c=None
    return c

print(max_odd(['ololo',21,23.001,3,'fufufu']))