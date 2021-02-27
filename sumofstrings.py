a = int(input())
b = int(input())
stra = str(a)
strb = str(b)
if(len(stra) != len(strb)):
    if (len(stra)>len(strb)):
        strb = strb.zfill(len(stra))
    else:
        stra = stra.zfill(len(strb))

out = ""
for i in range(0,len(stra)):
    out = out+str(int(stra[i])+int(strb[i]))
print(out)
        
