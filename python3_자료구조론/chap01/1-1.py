# 세 정수의 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 A : '))
b = int(input('정수 B : '))
c = int(input('정수 C : '))

maximum = a

if b > maximum : maximum = b
if c > maximum : maximum = c
print(f'최댓값은 {maximum}')

# 문자열도 입력받기
print('name : ', end='')
name = input()
print(f'hi ~ {name}')