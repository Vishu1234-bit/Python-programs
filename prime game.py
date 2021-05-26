def main():
    
    n = int(input())
    for i in range(n):
        first =0
        last=-1
        l,r = map(int,input().split())
        for i in range(l,r+1):
            if(isprime(i)):
                first =i
                break
        for i in range(r,l-1,-1):
            if(isprime(i)):
                last = i
                break
        print(last-first)
def isprime(n):
    flag =0
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                flag =1
                break
    if(flag):
        return 0
    else:
        return 1

 # Write code here 

main()
