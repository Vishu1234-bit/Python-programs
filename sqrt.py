class Solution:
    def countSquares(self, N):
        # code here 
        if(int(math.sqrt(N))**2 == N):
            return int(math.sqrt(N)-1)
        else:    
            return int(math.sqrt(N))
