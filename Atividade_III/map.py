# 6. Pesquise sobre a função map na linguagem Python. O que ela faz? Crie um programa Python que
# exemplifica seu uso e utilize conceitos de cálculo lambda em seu exemplo.

# Resposta: Em Python, a função map() é uma função embutida que permite aplicar uma determinada função a cada item de uma sequência (como uma lista, tupla ou conjunto) e retorna um iterador que contém os resultados. 
# Ela é usada para transformar elementos de uma sequência de acordo com a função fornecida, criando uma nova sequência com os resultados das transformações.
# Entrada da funcao map eh uma funcao e um iteravel
#Exemplo:
numeros = [1,2,3,4]
resultad = map(lambda x: x*2, numeros)
print(list(resultad))

# 7. Pesquise sobre a função filter na linguagem Python. O que ela faz? Crie um programa Python que
# exemplifica seu uso e utilize conceitos de cálculo lambda em seu exemplo.

# Resposta: A função filter() em Python é outra função embutida que permite filtrar elementos de uma sequência (como uma lista, tupla ou conjunto) com base em uma função de teste. 
# Ela cria um iterador que contém apenas os elementos da sequência para os quais a função de teste retorna True.
# Entrada da funcao eh uma funcao e um iteravel
#Exemplo:

numeros = [1,2,3,4]
resultado = filter(lambda x: x > 2, numeros)
print(list(resultado))

# 8. Crie uma expressão Lambda que compute o n-ésimo número de Fibonacci. Leia n do teclado.
n = int(input())
# Definição do Combinador Y
def Y(f):
    return (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))


def fibo(f):
    return lambda n: 1 if n <= 1 else f(n-2) + f(n - 1)

fibonacci = Y(fibo)
print(fibonacci(n))