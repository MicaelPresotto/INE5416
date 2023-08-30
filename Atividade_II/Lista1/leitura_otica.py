while True:
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        cont = 0
        possible_answer = -1
        numbers = [int(i) for i in input().split()]
        dic = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2], 'D': numbers[3], 'E': numbers[4], '*': '*'}
        for i in numbers:
            if i <= 127:
                cont += 1
                possible_answer = i
        if possible_answer == -1:
            possible_answer = '*'
        if cont > 1:
            print('*')
            continue
        for k,v in dic.items():
            if v == possible_answer:
                print(k)   