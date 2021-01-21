def swap_case(s):
    m = ""
    for i in s:
        if(i.isupper()):
            i=i.lower()
            m = m+i
        else:
            i=i.upper()
            m = m+i
    return m
s = "firtPAGE"
print(swap_case(s))
