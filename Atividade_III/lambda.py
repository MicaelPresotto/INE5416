# Crie uma expressão Lambda que receba dois valores inteiros (x e y) e retorne o resultado da soma dos
# dois valores. Leia os valores x e y do teclado
soma = lambda x,y: x + y
print(soma(2,5))
# Crie uma expressão Lambda que receba três notas de um aluno (a, b, c), calcule a média e retorne se o
# aluno foi aprovado ou reprovado. Para um aluno ser aprovado, ele deve possuir nota igual ou superior a
# 6. Leia as notas dos alunos do teclado.
a,b,c = [int(x) for x in input().split()]
media = lambda a,b,c: 'aprovado' if a+b+c/3 > 7 else "reprovado"
print(media(a,b,c))
# Crie uma expressão Lambda que resolva uma equação de segundo grau da forma ax2 + bx + c utilizando
# a fórmula de Bhaskara. Leia os coeficientes a, b e c do teclado
a,b,c = [int(x) for x in input().split()]
bhaskara = lambda a, b, c: (
    (-b + (b**2 - 4*a*c)**0.5) / (2*a),
    (-b - (b**2 - 4*a*c)**0.5) / (2*a)
)
r1, r2 = bhaskara(a,b,c)
print(r1,r2)

# Crie uma expressão Lambda que dados dois pontos no espaço 3D, (x1, y1, z1) e (x2, y2, z2), compute a
# distância entre eles. Leia as posições dos pontos do teclado.
x1,y1,z1,x2,y2,z2 = [float(x) for x in input().split()]
a, b = (x1,y1,z1), (x2,y2,z2)
distancia = lambda a,b: (
    ((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)**0.5
)
print(distancia(a,b))


#  Crie uma expressão Lambda que receba 3 valores numéricos (a, b, c) e retorne o maior deles. Não utilize
# nenhuma forma de ordenação. Leia os valores a, b, c do teclado
maior = lambda a,b,c: max(a,b,c)
a,b,c = [int(x) for x in input().split()]
print(maior(a,b,c))
