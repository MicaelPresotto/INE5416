cor(amarelo).
cor(azul).
cor(branca).
cor(verde).
cor(vermelho).

motorista(anderson).
motorista(fabio).
motorista(luciano).
motorista(pietro).
motorista(yuri).

limpeza(completa).
limpeza(cristalizacao).
limpeza(enceramento).
limpeza(polimento).
limpeza(simples).

tipo(crossover).
tipo(hatch).
tipo(pickup).
tipo(sedan).
tipo(suv).

placa(aaa1111).
placa(bbb2222).
placa(ccc3333).
placa(ddd4444).
placa(eee5555).

chaveiro(abridor).
chaveiro(bola).
chaveiro(coracao).
chaveiro(foto).
chaveiro(guitarra).

%X está à ao lado de Y
aoLado(X,Y,Lista) :- nextto(X,Y,Lista);nextto(Y,X,Lista).
                       
%X está à esquerda de Y (em qualquer posição à esquerda)
aEsquerda(X,Y,Lista) :- nth0(IndexX,Lista,X), 
                        nth0(IndexY,Lista,Y), 
                        IndexX < IndexY.
                        
%X está à direita de Y (em qualquer posição à direita)
aDireita(X,Y,Lista) :- aEsquerda(Y,X,Lista). 

%X está no canto se ele é o primeiro ou o último da lista
noCanto(X,Lista) :- last(Lista,X).
noCanto(X,[X|_]).

todosDiferentes([]).
todosDiferentes([H|T]) :- not(member(H,T)), todosDiferentes(T).

solucao(ListaSolucao) :- 
    ListaSolucao = [
        carro(Cor1, Motorista1, Limpeza1, Tipo1, Placa1, Chaveiro1),
        carro(Cor2, Motorista2, Limpeza2, Tipo2, Placa2, Chaveiro2),
        carro(Cor3, Motorista3, Limpeza3, Tipo3, Placa3, Chaveiro3),
        carro(Cor4, Motorista4, Limpeza4, Tipo4, Placa4, Chaveiro4),
        carro(Cor5, Motorista5, Limpeza5, Tipo5, Placa5, Chaveiro5)
    ],
    
    %A chave do carro Azul está presa no chaveiro que é um Bola.
    member(carro(azul, _, _, _, _, bola), ListaSolucao),

    %O carro Azul está em algum lugar entre o carro do Fábio e o carro que está fazendo 
    %a limpeza Completa, nessa ordem.
    aDireita(carro(azul, _, _, _, _, _), carro(_, fabio, _, _, _, _), ListaSolucao),
    aEsquerda(carro(azul, _, _, _, _, _), carro(_, _, completa, _, _, _), ListaSolucao),

    %Na terceira posição está o carro que tem um Abridor como chaveiro.
    Chaveiro3 = abridor,

    %O Hatch está ao lado do carro que está fazendo o Enceramento.
    aoLado(carro(_, _, _, hatch, _, _), carro(_, _, enceramento, _, _, _), ListaSolucao),

    %O carro Amarelo está em algum lugar à esquerda do carro Verde.
    aEsquerda(carro(amarelo, _, _, _, _, _), carro(verde, _, _, _, _, _), ListaSolucao),

    %O carro de placa EEE-5555 está ao lado do carro que tem uma Foto no chaveiro.
    aoLado(carro(_, _, _, _, eee5555, _), carro(_, _, _, _, _, foto), ListaSolucao),

    %O Hatch está ao lado do carro de placa EEE-5555.
	aoLado(carro(_, _, _, hatch, _, _), carro(_, _, _, _, eee5555, _), ListaSolucao),

    %O carro do Pietro está em algum lugar entre o carro de placa AAA-1111 e o carro do Luciano, nessa ordem.
    aDireita(carro(_, pietro, _, _, _, _), carro(_, _, _, _, aaa1111, _), ListaSolucao),
    aEsquerda(carro(_, pietro, _, _, _, _), carro(_, luciano, _, _, _, _), ListaSolucao),

    %A limpeza Simples está sendo feita no carro de placa BBB-2222.
    member(carro(_, _, simples, _, bbb2222, _), ListaSolucao),

    %O Crossover está em algum lugar à direita do carro Verde.
    aDireita(carro(_, _, _, crossover, _, _), carro(verde, _, _, _, _, _), ListaSolucao),

    %A Cristalização está sendo feita no carro que tem uma Bola como chaveiro.
    member(carro(_, _, cristalizacao, _, _, bola), ListaSolucao),

    %Na primeira posição está o carro de placa DDD-4444.
    Placa1 = ddd4444,

    %Anderson optou por fazer uma limpeza Simples no carro dele.
    member(carro(_, anderson, simples, _, _, _), ListaSolucao),

    %O carro de placa CCC-3333 está exatamente à esquerda do carro que tem um chaveiro em formato de Guitarra.
    aEsquerda(carro(_, _, _, _, ccc3333, _), carro(_, _, _, _, _, guitarra), ListaSolucao),
    aoLado(carro(_, _, _, _, ccc3333, _), carro(_, _, _, _, _, guitarra), ListaSolucao),

    %O carro que tem um Coração como chaveiro está ao lado do carro que tem uma Bola como chaveiro.
    aoLado(carro(_, _, _, _, _, coracao), carro(_, _, _, _, _, bola), ListaSolucao),

    %O Sedan está na quarta posição.
    Tipo4 = sedan,

    %A SUV está exatamente à esquerda do carro que tem uma Foto como chaveiro.
    aEsquerda(carro(_, _, _, suv, _, _), carro(_, _, _, _, _, foto), ListaSolucao),
    aoLado(carro(_, _, _, suv, _, _), carro(_, _, _, _, _, foto), ListaSolucao),
   
    %O carro de placa AAA-1111 está exatamente à direita do carro Vermelho.
    aDireita(carro(_, _, _, _, aaa1111, _), carro(vermelho, _, _, _, _, _), ListaSolucao),

    %O Polimento está sendo feito no carro de uma das pontas.
    noCanto(carro(_, _, polimento, _, _, _), ListaSolucao),

    %O carro do chaveiro que é um Abridor está exatamente à esquerda do carro que tem uma Foto como chaveiro.
    aEsquerda(carro(_, _, _, _, _, abridor), carro(_, _, _, _, _, foto), ListaSolucao),
    aoLado(carro(_, _, _, _, _, abridor), carro(_, _, _, _, _, foto), ListaSolucao),
    
    %Testa todas as possibilchaveiros...
    cor(Cor1), cor(Cor2), cor(Cor3), cor(Cor4), cor(Cor5), 
    todosDiferentes([Cor1, Cor2, Cor3, Cor4, Cor5]), 
    
    motorista(Motorista1), motorista(Motorista2), motorista(Motorista3), motorista(Motorista4), motorista(Motorista5),
    todosDiferentes([Motorista1, Motorista2, Motorista3, Motorista4, Motorista5]),
    
    limpeza(Limpeza1), limpeza(Limpeza2), limpeza(Limpeza3), limpeza(Limpeza4), limpeza(Limpeza5),
    todosDiferentes([Limpeza1, Limpeza2, Limpeza3, Limpeza4, Limpeza5]),
    
    tipo(Tipo1), tipo(Tipo2), tipo(Tipo3), tipo(Tipo4), tipo(Tipo5),
    todosDiferentes([Tipo1, Tipo2, Tipo3, Tipo4, Tipo5]),
    
    placa(Placa1), placa(Placa2), placa(Placa3), placa(Placa4), placa(Placa5),
    todosDiferentes([Placa1, Placa2, Placa3, Placa4, Placa5]),

    chaveiro(Chaveiro1), chaveiro(Chaveiro2), chaveiro(Chaveiro3), chaveiro(Chaveiro4), chaveiro(Chaveiro5),
    todosDiferentes([Chaveiro1, Chaveiro2, Chaveiro3, Chaveiro4, Chaveiro5]).
