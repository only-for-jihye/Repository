# 선택정렬

if __name__ == "__main__":
    array = [12, 1, 10, 5, 8, 7, 6, 4, 3, 2, 9, 11]

    min = 0
    index = 0
    temp = 0
    for i in range(0, len(array)):
        min = 9999;
        for j in range(i, len(array)):
            if (min > array[j]):
                min = array[j]
                index = j
        temp = array[i]
        array[i] = array[index]
        array[index] = temp
    
    for i in range(0,len(array)):
        print(array[i])

# 시간 복잡도 
# 빅오표기법
# O(N^2)