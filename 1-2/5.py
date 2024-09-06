def troyka(massive):
    variants = []
    for i in range(len(massive)):
        e = massive[i]
        for j in range(i+1, len(massive)):
            e2 = massive[j]
            for k in range(j+1, len(massive)):
                e3 = massive[k]
                if e+e2+e3 == 0:
                    variants.append([e,e2,e3])
    
    return variants

print(troyka([-4,5,0,-1,-2,9,-8]))