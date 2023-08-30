def verifica_expressao(palavra):
    pilha = []
    for i in palavra:
        if i in ('(', '{', '['):
            pilha.append(i)
        if i in (')', ']', '}'):
            if len(pilha):
                if i == ')' and pilha[-1] == '(' or i == ']' and pilha[-1] == '[' or i == '}' and pilha[-1] == '{':
                    pilha.pop()
                else:
                    return ['f']
            else:
                return ['eduardo']
    return pilha
n = int(input())
for _ in range(n):
    m = input()
    pilha = verifica_expressao(m)
    print('N') if len(pilha) else print("S")