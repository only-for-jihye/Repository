# 이진 삽입 정렬 알고리즘 구현 (bisect.insort 사용)

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬 bisect.insort"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
        # bisect.insort(a, x, lo, hi)
        # a가 이미 정렬된 상태를 유지하면서
        # a[lo] ~ a[hi] 사이에 x를 삽입
        # 만약 a안에 x와 같은 값을 갖는 원소가 여러 개 있으면 가장 오른쪽 위치에 삽입

if __name__ == '__main__':
    print('이진 삽입 정렬 수행')
    num = int(input('원소 수를 입력 : '))

    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    
    binary_insertion_sort(x)

    print('오름 차순 정렬')
    for i in range(num):
        print(f'x[{i}] : {x[i]}')


