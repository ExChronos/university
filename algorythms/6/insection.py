def insection_sort(arr):
    k = len(arr)

    for i in range(1, k):
        x = arr[i]
        j = i

        while j > 0 and arr[j-1] > x:
            arr[j] = arr[j-1]
            j -= 1
        
        arr[j] = x
        
    
    return arr