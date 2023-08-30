x = int(input())
lista_notas = [100, 50, 20, 10, 5, 2, 1]
qntd_notas = [0, 0, 0, 0, 0, 0, 0]
print(x)
for i, nota in enumerate(lista_notas):
    while x >= nota:
        x -= nota
        qntd_notas[i] += 1
    print(f'{qntd_notas[i]} nota(s) de R$ {lista_notas[i]},00')