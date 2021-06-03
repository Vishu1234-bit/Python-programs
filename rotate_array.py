def rotateImage(a):
    t = zip(*a)
    res = []
    for r in t:
       res.append(r[::-1]) 
    return res
