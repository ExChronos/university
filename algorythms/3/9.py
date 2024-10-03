# 9 - время выполнения алгоритмов
import time, random

massive = [random.randint(0, 900) for i in range(10000)]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

start = time.time()
bubble_sort(massive)
stop = time.time()
print(stop-start)

def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

start = time.time()
select_sort(massive)
stop = time.time()
print(stop-start)

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        k = arr[0]
        same = [l for l in arr if l == k]
        less = [i for i in arr if i < k]
        greater = [j for j in arr if j > k]

        return qsort(less) + same + qsort(greater)

start = time.time()
qsort(massive)
stop = time.time()
print(stop-start)