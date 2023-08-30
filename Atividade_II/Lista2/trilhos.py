while True:
    n = int(input())
    if not n:
        break
    entrada = [i+1 for i in range(n)]
    while True:
        vag = input()
        if vag == '0': break
        vagoes = [int(x) for x in vag.split()]
        pilha = []
        j = k = 0
        while j < n:
            tenho = entrada[j]
            quero = vagoes[k]
            if tenho == quero:
                 j+=1
                 k+=1
            elif len(pilha) and pilha[-1] == quero:
                pilha.pop()
                k += 1
            else:
                pilha.append(tenho)
                j += 1
        possible = True
        while len(pilha):
            if pilha[-1] == vagoes[len(vagoes) - len(pilha)]:
                pilha.pop()
            else:
                possible = False
                break
        print('Yes') if possible else print("No")
    print()