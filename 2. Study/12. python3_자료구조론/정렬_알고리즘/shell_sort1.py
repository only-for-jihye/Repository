# 셸 정렬 알고리즘 구현하기

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """셸 정렬"""
    n = len(a)
    h = n // 2
    print(f'h : {h}')
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2


if __name__ == '__main__':
    print('셸 정렬 수행')
    num = int(input('원소 수를 입력 : '))

    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    
    shell_sort(x)

    print('오름 차순 정렬')
    for i in range(num):
        print(f'x[{i}] : {x[i]}')

