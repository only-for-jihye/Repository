# 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)

x = int(input('정숫값을 입력 : '))

recur(x)