def sortByHeight(a):
    out = []
    for i in a:
        if(i!= -1):
            out.append(i)
    out.sort()
    for i in range(0,len(a)):
        if(a[i]== -1):
            out.insert(i,a[i])
    return out
a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))
