from collections import deque
cache_size = int(input())
pages = int(input())
arr= []
for i in range(0,pages):
    j = int(input())
    arr.append(j)
print(cache_size,arr,pages)
cache = deque()
count=0
for i in range(0,len(arr)):
    if arr[i] not in cache:
        cache.append(arr[i])
    if(len(cache)==cache_size):
        count+=1
        cache.popleft()
print(count)
        
    
