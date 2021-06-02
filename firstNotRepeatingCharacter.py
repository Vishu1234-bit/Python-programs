def firstNotRepeatingCharacter(s):
    d = dict()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res = '_'
    for i in d.keys():
        if(d[i]==1):
            res = i
            break
    return res
s = input()
print(firstNotRepeatingCharacter(s))
