# 4 - сортировка выбором
def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(select_sort([3,1,5,3,4,2,6,4,6,9,1]))