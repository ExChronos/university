# 8 - реверсивная быстрая сортировка
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        k = arr[0]
        same = [l for l in arr if l == k]
        less = [i for i in arr if i < k]
        greater = [j for j in arr if j > k]

        return qsort(greater) + same + qsort(less)

num = [5,3,1,6,3,2,7,4,9,1,6,2,4,8]

print(qsort([5,3,1,6,3,2,7,4,9,1,6,2,4,8]))