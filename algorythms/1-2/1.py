def linearSearch(massive):
    emax = 0
    count = True
    for i in massive:
        if(count):
            emax = i
            count = False
        if(emax < i):
            emax = i

    return emax

print(linearSearch([4,10,1,0,-3,21,9,2,0,12,-1]))