# 버블 정렬 알고리즘 구현하기 (알고리즘의 개선 2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬 (스캔 범위를 제한)"""
    n = len(a)
    #for i in range(n - 1):
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last

if __name__ == '__main__':
    print('버블 정렬 수행')
    num = int(input('원소 수 입력 : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    
    bubble_sort(x)  # 배열 x를 버블 정렬

    print('오름차순 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')