import time

def qsort(arr):

    stack = []

    stack.append((0, len(arr)-1))
    
    print(f'array до начала изменений - {arr}')

    while stack:
        start, end = stack.pop()

        pivot = arr[end]
        pIndex = start

        
        print(f'{pivot} - начальный элемент до старта, {pIndex} - индекс куда будет вставлен опорный элемент после разбиения массива - в начале')

        for i in range(start, end):
            
            if arr[i] < pivot:
                arr[i], arr[pIndex] = arr[pIndex], arr[i]
                pIndex += 1
            
            arr[pIndex], arr[end] = arr[end], arr[pIndex]

            if pIndex - 1 > start:
                stack.append((start, pIndex-1))
            if pIndex + 1 < end:
                stack.append((pIndex + 1, end))
            
            print(
                f'array - {arr}\n'
                f'start - {start}\n'
                f'end - {end}\n'
                f'pivot - {pivot}\n'
                f'pIndex - {pIndex}\n'
                f'arr[i] - {arr[i]}\n'
                f'arr[pIndex] - {arr[pIndex]}\n'
                f'arr[end] - {arr[end]}\n'
                f'stack: {stack}\n\n'
                )
        time.sleep(0.5)

    return arr

array = [10,7,8,9,1,5]
sorted_array = qsort(array)
print(sorted_array)