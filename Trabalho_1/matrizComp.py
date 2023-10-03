# gera matriz de comparacao

matrix = [9,2,4,8,7,3,1,6,5,
     1,8,5,2,6,4,7,9,3,
     3,6,7,9,1,5,8,4,2,
     4,9,3,7,5,2,6,8,1,
     7,5,8,6,4,1,3,2,9,
     6,1,2,3,8,9,4,5,7,
     2,4,9,1,3,8,5,7,6,
     8,3,6,5,2,7,9,1,4,
     5,7,1,4,9,6,2,3,8]

matrix_comparation = []

for i in range(81):
    element = []
    if i%27 <=8:
        element.append(-1)
    elif i//9 > 0:
        element.append(1) if matrix[i] > matrix[i-9] else element.append(0)
    else:
        element.append(-1)

    if i%3 == 2:
        element.append(-1)
    elif i%9 < 8:
        element.append(1) if matrix[i] > matrix[i+1] else element.append(0)
    else:
        element.append(-1)

    if i%27 >= 18:
        element.append(-1)
    elif i//9 < 8:
        element.append(1) if matrix[i] > matrix[i+9] else element.append(0)
    else:
        element.append(-1)
    
    if not i%3:
        element.append(-1)
    elif i%9 > 0:
        element.append(1) if matrix[i] > matrix[i-1] else element.append(0)
    else:
        element.append(-1)
    matrix_comparation.append(element)

# cima direita baixo esquerda
print(matrix_comparation)