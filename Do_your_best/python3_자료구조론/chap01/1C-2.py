# 세 정수를 입력받아 중앙값 구하기 1

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('세 정수의 중앙값을 구함')
a = int(input('정수 a :'))
b = int(input('정수 b :'))
c = int(input('정수 c :'))

print(f'중앙값은 {med3(a,b,c)}')