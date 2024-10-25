def k_statistic(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    p=arr[len(arr)//2]
    less=[i for i in arr if i < p]
    same=[i for i in arr if i == p]
    greater=[i for i in arr if i > p]

    if k < len(less):
        return k_statistic(less, k)
    elif k < len(less)+len(same):
        return same[0]
    else:
        return k_statistic(greater, k-len(less)-len(same))

massive=[10, 6, 14, 7, 3, 2, 18, 4, 5, 13, 6, 8]

print(k_statistic(massive, len(massive)//2))
print(k_statistic(massive, 6))