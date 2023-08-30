while True:
    k = int(input())
    if k == 0:
        break
    n,m = [int(x) for x in input().split()]
    for i in range(k):
        result = ''
        x,y = [int(j) for j in input().split()]
        if x == n or y == m:
            print('divisa')
            continue
        result += 'N' if y - m > 0 else 'S'
        result += 'E' if x - n > 0 else 'O'
        print(result)
