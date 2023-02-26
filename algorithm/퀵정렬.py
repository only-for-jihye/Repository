# 퀵 정렬
# 대표적인 '분할 정복' 알고리즘으로 평균 속도가 O(N * logN)

number = 10
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

def quickSort(data, start, end):
    if (start >= end): # 원소가 1개인 경우
        return
    
    key = start # 키는 첫번째 원소
    i = start + 1
    j = end
    temp = 0

    while (i <= j): # 엇갈릴 때까지 반복
        while (data[i] <= data[key]): # 키 값보다 큰 값을 만날 때까지
            i = i + 1
        while (data[j] >= data[key] & j > start): # 키 값보다 작은 값을 만날 때까지
            j = j - 1
        if (i > j) : #현재 엇갈린 상태면 키 값과 교체
            temp = data[j]
            data[j] = data[key]
            data[key] = temp
        else :
            temp = data[j]
            data[j] = data[i]
            data[i] = temp

    quickSort(data, start, j - 1)
    quickSort(data, j + 1, end)

if __name__ == "__main__" :
    quickSort(array, 0, number - 1)

    for i in range(0, number - 1):
        print(array[i])