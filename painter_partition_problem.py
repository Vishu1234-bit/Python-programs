def paint( A, B, C):
    def ispossible(m):
        su=0
        painters =1
        for i in C:
            su = su+i
            if(su>m):
                painters +=1
                su=i
        return painters
                
    l,h = max(C),sum(C)
    while(l<h):
        m = (l+h)//2
        reqpainters = ispossible(m)
        if(reqpainters<=A):
            h =m
        else:
            l = m+1
    return (l*B)%10000003
print(paint(2,5,[1,10]))
    

