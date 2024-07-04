# 스택으로 재귀함수 구현하기 (재귀를 제거)

from stack import Stack

def recur(n: int) -> int:
    """재귀를 제거한 recur() 함수"""

    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)       # n값을 푸시
            n = n - 1
            continue
        if not s.is_empty():    # 스택이 비어 있지 않으면
            n = s.pop()         # 저장한 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input('정숫값을 입력하세요. : '))

recur(x)