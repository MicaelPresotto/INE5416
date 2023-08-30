n = int(input())
for _ in range(n):
    cont_diamantes = 0
    m = input()
    pilha = []
    for i in m:
        if i == '<':
            pilha.append(i)
        if i == '>':
            if len(pilha):
                pilha.pop()
                cont_diamantes += 1
    print(cont_diamantes)