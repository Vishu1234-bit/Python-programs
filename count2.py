def countof2(input1,input2):
    j= '2'
    count=0
    for i in range(input1,input2):
        if j in str(i):
            count = count+numberof2(i)
    return count
def numberof2(i):
    count=0
    while(i>0):
        if(i%10==2):
            count=count+1
        i=i//10
    return count
print(countof2(2,60))
            
