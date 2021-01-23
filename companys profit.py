n = int(input())
arr = list(map(int,input().split()))
query = int(input())
for i in range(query):
    l,r = map(int,input().split())
    if(l>r):
        print("-1")
    count=0
    for j in range(0,len(arr)):
        if(arr[j]>=l and arr[j]<=r):
          count+=1
    print(count)
    
