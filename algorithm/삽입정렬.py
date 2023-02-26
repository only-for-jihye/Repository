# 삽입정렬

if __name__ == "__main__":
    array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    temp = 0

    for i in range(0, len(array)-1):
        j = i
        while (array[j] > array[j+1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            j = j - 1

    for i in range(0, len(array) - 1):
        print(array[i])

# 시간 복잡도
# 빅오표기법 O(N^2)
# 왼쪽은 정렬이 되어있다고 가정 후, 정렬 시작

# swap 동작의 수가 적을수록 효율적인 정렬 알고리즘
# 즉 연산 동작이 적다

# 거의 정렬된 상태라면 굉장히 효율적이다

