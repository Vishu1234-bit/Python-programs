def firstDuplicate(a):
    b = [0]*(max(a)+1)
    for i in a:
        if(b[i]==1):
            return i
            break
        else:
            b[i] =1
    return -1
        
a = list(map(int,input().split()))
print(firstDuplicate(a))

