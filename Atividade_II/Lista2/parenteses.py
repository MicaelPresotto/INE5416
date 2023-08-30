while True:
    try:
        expression = input()
    except:
        break
    pilha = []
    for i in expression:
        if i == '(':
            pilha.append(i)
        if i ==')':
            try:
                pilha.pop(-1)
            except IndexError:
                print('incorrect')
                break
    else:
        if len(pilha) == 0:
            print('correct')
        else:
            print('incorrect')
