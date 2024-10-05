from shell_s import shell_sort
from bubble_s import bubble_sort
from insection_s import insection_sort
from select_s import select_sort
from quick_s import qsort
import time

massive = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150, ]
times=dict()

sh_start = time.time()
shell_sort(massive)
sh_stop = time.time()

sh_time = sh_stop-sh_start
times['Сортировка Шелла'] = sh_time

b_start = time.time()
bubble_sort(massive)
b_stop = time.time()

b_time = b_stop - b_start
times['Сортировка пузырьком'] = b_time

i_start = time.time()
insection_sort(massive)
i_stop = time.time()

i_time = i_stop - i_start
times['Сортировка вставкой'] = i_time

se_start = time.time()
select_sort(massive)
se_stop = time.time()

se_time = se_stop - se_start
times['Сортировка выбором'] = se_time
q_start = time.time()
qsort(massive)
q_stop = time.time()

q_time = q_stop-q_start
times['Быстрая сортировка'] = q_time

for key, value in times.items():
    print(f'{key} - {value}')