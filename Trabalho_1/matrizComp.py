# gera matriz de comparacao

m = [9,2,4,8,7,3,1,6,5,
     1,8,5,2,6,4,7,9,3,
     3,6,7,9,1,5,8,4,2,
     4,9,3,7,5,2,6,8,1,
     7,5,8,6,4,1,3,2,9,
     6,1,2,3,8,9,4,5,7,
     2,4,9,1,3,8,5,7,6,
     8,3,6,5,2,7,9,1,4,
     5,7,1,4,9,6,2,3,8]

r = []

for i in range(81):
    e = []
    if i%27 <=8:
        e.append(-1)
    elif i//9 > 0:
        e.append(1) if m[i] > m[i-9] else e.append(0)
    else:
        e.append(-1)

    if i%3 == 2:
        e.append(-1)
    elif i%9 < 8:
        e.append(1) if m[i] > m[i+1] else e.append(0)
    else:
        e.append(-1)

    if i%27 >= 18:
        e.append(-1)
    elif i//9 < 8:
        e.append(1) if m[i] > m[i+9] else e.append(0)
    else:
        e.append(-1)
    
    if not i%3:
        e.append(-1)
    elif i%9 > 0:
        e.append(1) if m[i] > m[i-1] else e.append(0)
    else:
        e.append(-1)
    r.append(e)

# cima direita baixo esquerda
print(r)