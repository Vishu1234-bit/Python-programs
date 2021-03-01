def concatSwaps(s,sizes):
    a=[]
    b=0
    h=sizes[0]
    for i in range(0,len(sizes)-1):
        a.append(s[b:h])
        b=b+sizes[i]
        h=h+sizes[i+1]
    a.append(s[b:len(s)])
    out=""
    if(len(sizes)%2!=0):
        for i in range(0,len(a)-1,2):
            out = out+a[i+1]+a[i]
        out = out+a[-1]
        return out
    else:
        for i in range(0,len(a)-1,2):
            out = out+a[i+1]+a[i]
        return out
s="descognail"
sizes=[3,2,3,1,1]
print(concatSwaps(s,sizes))
