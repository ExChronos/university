def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        p = arr[0]
        less = [i for i in arr if i < p]
        same = [j for j in arr if j == p]
        greater = [k for k in arr if k > p]

        return qsort(less) + same + qsort(greater)