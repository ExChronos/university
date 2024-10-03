# 6 - быстрая сортировка
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        k = arr[0]
        less = [i for i in arr if i < k]
        greater = [j for j in arr if j > k]

        return qsort(less) + [k] + qsort(greater)

print(qsort([5,3,1,6,3,2,7,4,9,8]))