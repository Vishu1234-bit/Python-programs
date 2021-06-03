class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
     
            h= max(arr)
            if(h<1):
                return 1
            l=[0]*h
            for i in arr:
                if(i>0):
                    if(l[i-1]!=1):
                        l[i-1]=1
            for i in range(len(l)):
                if(l[i]==0):
                    return i+1
            return i+2
                
