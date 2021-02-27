listinput = list(map(str,input().split()))
out = []
for i in range(0,len(listinput)-1):
    if((listinput[i][0]==listinput[i+1][0] )& (listinput[i][-1]==listinput[i+1][-1])):
        out.append("True")
    else:
        out.append("False")
print(out)
        
    
