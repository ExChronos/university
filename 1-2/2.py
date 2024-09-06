def Bsort(massive):
    for i in range(len(massive)):
        for e in range(len(massive)-i-1):
            if massive[e] > massive[e+1]:
                massive[e], massive[e+1] = massive[e+1], massive[e]

    return massive

print(Bsort([4,1,6,2,0,1,4,-1,5,2,-4]))