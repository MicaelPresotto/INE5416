n,m = [int(x) for x in input().split()]
lista = [0] * n
for _ in range(m):
    p,d = [int(x) for x in input().split()]
    t = p
    lista[p-1] = 1
    while t <= len(lista):
        lista[t-1] = 1
        t += d
    while p >= 1:
        lista[p-1] = 1
        p -= d
for i in lista:
    print(i)