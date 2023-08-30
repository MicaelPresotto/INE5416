a,b,c = [int(x) for x in input().split()]
cont = 0
while a >= 2 and b >= 3 and c >= 5:
    a -= 2
    b -= 3
    c -= 5
    cont += 1
print(cont)