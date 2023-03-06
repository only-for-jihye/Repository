# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0 # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1 # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc # 검색 성공
        elif a[pc] < key:
            pl = pc + 1 # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1 # 검색 범위를 앞쪽으로 절반 좁힘
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력 : '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요 : ')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]: # 바로 직전에 입력한 원솟값보다 큰 값을 입력
                break
            else:
                print('직전 값보다 큰 값을 입력하세요')
    
    ky = int(input('검색할 값? : '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('X')
    else:
        print(f'x[{idx}]에 있음')