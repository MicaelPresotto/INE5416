:-  use_module(library(clpfd)).

matrizComparacoes(MatrizComparacoes) :-
    MatrizComparacoes = [[[-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1], [-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1], [-1, 0, 0, -1], [-1, 0, 1, 1], [-1, -1, 1, 1]], 
    [[0, 1, 1, -1], [1, 0, 1, 0], [1, -1, 0, 1], [0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 1, 0], [1, 1, 0, -1], [0, 1, 0, 0], [0, -1, 0, 0]],
    [[0, 1, -1, -1], [0, 0, -1, 0], [1, -1, -1, 1], [1, 1, -1, -1], [0, 1, -1, 0], [0, -1, -1, 0], [1, 0, -1, -1], [1, 1, -1, 1], [1, -1, -1, 0]],
    [[-1, 0, 1, -1], [-1, 1, 0, 1], [-1, -1, 0, 0], [-1, 1, 1, -1], [-1, 1, 0, 0], [-1, -1, 0, 0], [-1, 0, 0, -1], [-1, 1, 1, 1], [-1, -1, 0, 0]], 
    [[0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 1, 0], [0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 0, 0], [1, 1, 0, -1], [0, 0, 0, 0], [1, -1, 1, 1]], 
    [[1, 0, -1, -1], [0, 1, -1, 1], [0, -1, -1, 0], [1, 0, -1, -1], [0, 1, -1, 1], [1, -1, -1, 0], [1, 1, -1, -1], [1, 1, -1, 0], [0, -1, -1, 0]], 
    [[-1, 1, 0, -1], [-1, 1, 0, 0], [-1, -1, 0, 0], [-1, 0, 0, -1], [-1, 0, 1, 1], [-1, -1, 1, 1], [-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1]], 
    [[1, 1, 1, -1], [1, 0, 1, 0], [1, -1, 1, 1], [1, 1, 0, -1], [0, 0, 0, 0], [0, -1, 0, 1], [0, 0, 0, -1], [1, 0, 0, 1], [1, -1, 0, 1]], 
    [[0, 0, -1, -1],[0, 1, -1, 1], [0, -1, -1, 0], [1, 1, -1, -1], [1, 1, -1, 0], [1, -1, -1, 0], [1, 0, -1, -1], [1, 0, -1, 1], [1, -1, -1, 1]]].



atLista(0, [H|_], H).
atLista(I, [_|T], X) :- I2 is I - 1, atLista(I2, T, X).

atMatriz(I, J, Lista, X) :- atLista(I, Lista, R), atLista(J, R, X).

define_comparacao(_, _, _, _, -1). %Se for -1 é irrelevante -> Não tem regra
define_comparacao(Num1, Sudoku, I, J, 1) :- atMatriz(I, J, Sudoku, Num2), Num1 #> Num2. %Se for 1, Num1 > Num2
define_comparacao(Num1, Sudoku, I, J, 0) :- atMatriz(I, J, Sudoku, Num2), Num1 #< Num2. %Se for 0, Num1 < Num2

define_comparacao(Num, I, J, Sudoku, Comparacoes) :- 
    atLista(0, Comparacoes, Comp0),
    atLista(1, Comparacoes, Comp1),
    atLista(2, Comparacoes, Comp2),
    atLista(3, Comparacoes, Comp3),

    Cima is I - 1,
    Direita is J + 1,
    Baixo is I + 1,
    Esquerda is J - 1,

    define_comparacao(Num, Sudoku, Cima, J, Comp0),
    define_comparacao(Num, Sudoku, I, Direita, Comp1),
    define_comparacao(Num, Sudoku, Baixo, J, Comp2),
    define_comparacao(Num, Sudoku, I, Esquerda, Comp3).


define_comparacoes_sudoku(_, _, 9, _).
define_comparacoes_sudoku(Sudoku, MatrizComparacoes, I, 9) :- N is I + 1, define_comparacoes_sudoku(Sudoku, MatrizComparacoes, N, 0).
define_comparacoes_sudoku(Sudoku, MatrizComparacoes, I, J) :- 
    atMatriz(I, J, Sudoku, Num),
    atMatriz(I, J, MatrizComparacoes, Comparacoes),
    define_comparacao(Num, I, J, Sudoku, Comparacoes),
    N is J + 1,
    define_comparacoes_sudoku(Sudoku, MatrizComparacoes, I, N).

repeteLinha(Sudoku) :-
    maplist(all_distinct, Sudoku).

repeteColuna(Sudoku) :-
    transpose(Sudoku, Colunas),
    maplist(all_distinct, Colunas).

repeteRegiao([]).
repeteRegiao([LinhaA,LinhaB,LinhaC|LinhaCauda]) :-
    repeteRegiao2(LinhaA,LinhaB,LinhaC),
    repeteRegiao(LinhaCauda).

repeteRegiao2([],[],[]).
repeteRegiao2([LinhaA1,LinhaA2,LinhaA3|LinhaACauda],[LinhaB1,LinhaB2,LinhaB3|LinhaBCauda],[LinhaC1,LinhaC2,LinhaC3|LinhaCCauda]) :-
    all_distinct([LinhaA1,LinhaA2,LinhaA3,LinhaB1,LinhaB2,LinhaB3,LinhaC1,LinhaC2,LinhaC3]),
    repeteRegiao2(LinhaACauda,LinhaBCauda,LinhaCCauda).

resolve(Sudoku) :-
    length(Sudoku, 9), % O tabuleiro tem 9 linhas
    maplist(same_length(Sudoku), Sudoku), % Cada linha 9 colunas
    append(Sudoku, Possiblidades), % Concatena todos os números do tabuleiro em Possiblidades
    Possiblidades ins 1..9, % O tabuleiro tem apenas números entre 1 e 9

    matrizComparacoes(MatrizComparacoes),
    
    define_comparacoes_sudoku(Sudoku, MatrizComparacoes, 0, 0),
    
    repeteLinha(Sudoku),
    repeteColuna(Sudoku),
    repeteRegiao(Sudoku).
