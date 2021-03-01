def alternatingSort(a):
     b=[]
     print(a)
     print(a[::-1])
     for i,j in zip(a,reversed(a)):
         b.append(i)
         b.append(j)
    
     b = b[0:len(a)]
     print(b)
     res = sorted(set(a))
     print(res)
     if(b==res):
         return True
     else:
         return False
    
a = [-92, -17, 71, 76, 54, -35]
print(alternatingSort(a))
