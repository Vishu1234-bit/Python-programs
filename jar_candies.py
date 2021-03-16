n=10
k=5
sold = int(input())
if(sold>=1 & sold<=5):
    print("NUMBER OF CANDIES SOLD :",sold)
    print("NUMBER OF CANDIES AVAILABLE :",n-sold)
else:
    print("INVALID INPUT")
    print("NUMBER OF CANDIES LEFT : ",n)
    
