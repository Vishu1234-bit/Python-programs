def rev(n):
    rev = 0
    while(n>0):
        rem = n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
def oppositesums(arr):
    pairs=0
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if((arr[i]+rev(arr[j])) == (arr[j] +rev(arr[i]))):
                
                pairs+=1
    return pairs
arr = list(map(int,input().split()))
print(oppositesums(arr))
            
