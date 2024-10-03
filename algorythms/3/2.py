# 2 - подсчет сравнений и обменов
def bubble_sort(arr):
    changes = 0
    compare = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                changes += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
            compare+=1

    return (arr, changes, compare)

print(bubble_sort([4,2,5,1,3,6,7,9,8]))