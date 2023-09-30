def is_a_valid_move(matrix, row, col, num):
    for i in range(9):
        #verificando se o numero ja existe na linha ou na coluna
        if matrix[row][i] == num or matrix[i][col] == num:
            return False
    
    row_start, col_start = 3 * (row // 3), 3 * (col // 3)
    #vericando se o numero ja existe no bloco
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if matrix[i][j] == num:
                return False
    #fazer agora a comparacao da celula para ver as possibilidades

    return True

def solve(matrix):
    for row in range(9):
        for col in range(9):
            #so vejo celulas vazias
            if matrix[row][col] == 0:
                for num in range(1,10):
                    #testo todos os numeros de 1 a 9
                    # e vejo se eh valido
                    if is_a_valid_move(matrix, row, col, num):
                        #caso for adiciono ele
                        matrix[row][col] = num
                        #chamo a funcao recursivamente para a proxima celula
                        if solve(matrix):
                            # caso ele conseguir resolver
                            # todas as recursoes, retorna true
                            return True
                        # caso nao, ele retrocede uma recursao na stack colocando 0 na celula
                        # e busca o proximo numero possivel dentro do loop de 1 a 9
                        matrix[row][col] = 0
                # se testar todos os numeros e nao conseguir achar nenhum valido
                # quer dizer que nao ha solucao possivel
                return False
    return True

if __name__ == '__main__':
    matrix = [[0 for j in range(9)]for i in range(9)]
    solve(matrix)
    for i in matrix:
        print(i)