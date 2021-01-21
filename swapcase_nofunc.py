def swap_case(s):
   upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   lower = "abcdefghijklmnopqrstuvwxyz"
   new=""
   for i in s:
       if i in upper:
           v = upper.index(i)
           new= new+lower[v]
       if i in lower:
            h = lower.index(i)
            new = new+upper[h]
   return new
s = "firtPAGE"
print(swap_case(s))
