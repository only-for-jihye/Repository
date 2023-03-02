# seq_search() 함수를 사용하여 실수 검색하기

from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "end"를 입력하면 종료합니다.')

number = 0
x = [] # 빈 리스트 x를 생성

while True:
    s = input(f'x[{number}] : ')
    if s == 'end':
        break
    x.append(float(s)) # 배열 맨 끝에 원소를 추가
    number += 1

ky = float(input('검색할 값을 입력하세요. : ')) # 검색할 키 ky 입력 받기

idx = seq_search(x, ky) # ky와 값이 같은 원소를 x에서 검색

if idx == -1:
    print('검색 없음')
else:
    print(f'검색 값은 x[{idx}]에 있음')
