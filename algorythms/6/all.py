from .insection import insection_sort
from .quick import qsort
from .select import select_sort
from time import time

massive=[10, 6, 14, 7, 3, 2, 18, 4, 5, 13, 6, 8]

start=time()
insection_sort(massive)
stop=time()

print(f'Insection sort = {stop-start}')


start=time()
inv=select_sort(massive)
stop=time()

print(f'Selection sort = {stop-start}, {inv[1]}')

start=time()
qsort(massive)
stop=time()

print(f'Quick sort = {stop-start}')