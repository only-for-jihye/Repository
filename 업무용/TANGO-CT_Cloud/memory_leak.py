

# list에서 list를 빼기
if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [1, 3, 4]
    c = [x for x in a if x not in b]
    print(c)

    