def isCryptSolution(crypt, solution):
    dict={}
    for i in solution:
        dict[i[0]] = i[1]
    cral = []
    for i in crypt:
        st = ''
        for j in i:
           st = st+dict[j] 
        cral.append(st)
    flag = True
    for i in cral:
        if (i[0] == '0' and len(i)!=1):
            flag=False
            break
    if(flag == True):  
        if(int(cral[0])+int(cral[1]) == int(cral[2])):
               flag=True
        else:
               flag = False
    return flag
        
