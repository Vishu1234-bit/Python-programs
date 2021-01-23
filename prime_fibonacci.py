def prime(n):
    count=0
    for i in range(2,1000):
        flag = 0
        for j in range(2,i):
            if(i%j == 0):
                flag=1
                break
        if(flag ==0):
            count+=1
            if(count==n):
                return i
                break
def fibonacci(n):
    first=1
    second =1
    if(n==1):
        return first
          
    if(n==2):
        return second
      
    count=2
    while(count<=n):
        third = first+second
        first = second
        second =third
        count+=1
        if(count==n):
            return third
            break
        
n = int(input())
if(n%2==0):
    print(prime(n/2))
else:
    print(fibonacci((n//2)+1))
