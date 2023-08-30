contador = 1
while True:
    v = int(input())
    if v == 0:
        break
    cedulas = [50, 10, 5, 1]
    cont_cedulas = [0] * 4
    for i in range(len(cedulas)):
        while v >= cedulas[i]:
            v -= cedulas[i]
            cont_cedulas[i] += 1
    print(f'Teste {contador}')
    contador += 1
    i,j,k,l = cont_cedulas
    print(i,j,k,l)
    print()