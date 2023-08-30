while True:
    H1, M1, H2, M2 = (int(x) for x in input().split())
    
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    
    minutos_atuais = H1 * 60 + M1
    minutos_do_alarme = H2 * 60 + M2

    if minutos_do_alarme > minutos_atuais:
        tempo_dormido = minutos_do_alarme - minutos_atuais
    else:
        if minutos_do_alarme == minutos_atuais:
            tempo_dormido = 24 * 60
        else:
            tempo_dormido = (24 * 60 - minutos_atuais) + minutos_do_alarme
    
    print(tempo_dormido)