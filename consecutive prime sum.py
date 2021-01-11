def isprime(n):
    for i in range(2,(n//2)+2):
        if (n%i == 0):
            return False
        else:
            return True
num = int(input())
arr=[]
for i in range(2,num):
    if (isprime(i)):
        arr.append(i)
#print(arr)
sum = 0
count = 0
for j in range(0,len(arr)):
    sum = sum+arr[j]
#print("sum=",sum)
    if(sum<=num):
       if (isprime(sum)):
          count+=1
print(count)
        
    

