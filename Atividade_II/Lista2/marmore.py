import bisect
contador = 1
while True: 
    n , q = [int(x) for x in input().split()]
    if n == q == 0:
        break
    print(f'CASE# {contador}:')
    contador += 1 
    lista_to_sort = []
    for _ in range(n):
        m = int(input())
        lista_to_sort.append(m)
    lista_to_sort.sort()
    for _ in range(q):
        x = int(input())
        t = bisect.bisect_left(lista_to_sort, x)
        if t < len(lista_to_sort) and lista_to_sort[t] == x:
            print(f'{x} found at {t+1}')
        else:
            print(f'{x} not found')