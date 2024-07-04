# greedy algorithm
# 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 거스름돈 예제

n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)