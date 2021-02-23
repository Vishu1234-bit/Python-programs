def countPairs(a,b,m,n):
    #code here
    import bisect
    def count(x,b,n,noy):
        if x==0:
            return 0
        if x==1:
            return noy[0]
        idx = bisect.bisect_right(b,x)
        ans = n-idx
        ans+=(noy[0]+noy[1])
        if x==2:
            ans-=(noy[3]+noy[4])
        if x==3:
            ans+=(noy[2])
        return ans
    pairs =0
    noy = [0]*5
    for i in b:
        if i<5:
           noy[i]+=1
    b.sort()
    for x in a:
        pairs+=count(x,b,n,noy)
    return pairs
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        m,n=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        print(countPairs(a,b,m,n))
        #code here
# } Driver Code Ends
