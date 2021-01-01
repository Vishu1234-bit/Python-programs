def findsubarray(array,n,s):
    for i in range(n):
        add=array[i]
        j=i+1
        while(j<=n):
            if(add==s):
               print(i+1,j)
               return 1
                
            if (add>s or j==n):
                break

            add = add+array[j]
            j+=1
    print("-1")
    return 0
t = int(input())
for i in range(0,t):
    n,s = list(map(int,input().split()))
    array = [int(i) for i in input().split()][:n]
    findsubarray(array,n,s)
