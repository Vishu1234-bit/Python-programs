def alnum(input1,input2):
     alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     if(input2==0):
         count=0
         if(input1.isalpha()):
             return 0
         else:
             for i in input1:
                 if (i not in alpha):
                    count+=int(i)
             return count
     if(input2==1):
        ret = ""
        if(input1.isdigit()):
            return 0
        else:
            for i in input1:
                if(i in alpha):
                    ret=ret+i
            return ret
              
              
              
input1 ="abcd"
input2 =0
print(alnum(input1,input2))
