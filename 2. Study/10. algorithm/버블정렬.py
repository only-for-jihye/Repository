# 버블정렬
# 좌우 비교해서 큰 수는 맨 끝으로
if __name__ == "__main__":
    temp = 0
    
    array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    
    #print(len(array))
    for i in range(0, len(array)):
        for j in range(0, len(array)-1-i):
            #print(j)
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    for i in range(0, len(array)):
        print(array[i])

# 시간 복잡도
# 빅오표기법
# O(N^2)
# 실제 수행 시간은 '선택정렬'보다 느리다.
# 정렬 알고리즘 중 가장 느림 ㅎ