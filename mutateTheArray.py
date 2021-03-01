def mutateTheArray(n, a):
    if n==1:
        return a
    else:
        b=[]
        b.append(0+a[0]+a[1])
        for i in range(1,n-1):
            b.append(a[i-1]+a[i]+a[i+1])
        b.append(a[-2]+a[-1]+0)
        return b
n= 5
a= [4, 0, 1, -2, 3]
print(mutateTheArray(n,a))
        
