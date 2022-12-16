import random
import time


def shell_sort(a):
    gap = len(a) // 2

    while gap > 0:
        for i in range(gap, len(a)):
            current_value = a[i]
            position = i

            while position >= gap and a[position - gap] > current_value:
                a[position] = a[position - gap]
                position -= gap
                a[position] = current_value
        gap = gap // 2
    return a


lst = random.sample(range(10000), 9999)
t_strt = time.time()
print(shell_sort(lst))
t_end = time.time()
print(f'время Шелла {t_end-t_strt}')
t_strt = time.time()
print(sorted(lst))
t_end = time.time()
print(f'время py {t_end-t_strt}')
