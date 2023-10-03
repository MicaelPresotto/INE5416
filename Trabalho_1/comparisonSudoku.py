import time

def is_a_valid_move(matrix, row, col, num, matrix_comparation):
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
    position = row * 9 + col

    #comparacoes da celula para ver as possibilidades
    if matrix_comparation[position][0] == 1:
        #nesse caso a celula de cima eh maior que a atual, caso nao for retorna false 
        if num < matrix[row-1][col] and matrix[row-1][col]:
            return False
    elif matrix_comparation[position][0] == 0:
        #nesse caso a celula de cima eh menor que a atual, caso nao for retorna false
        if num > matrix[row-1][col] and matrix[row-1][col]:
            return False
    if matrix_comparation[position][1] == 1:
        #nesse caso a celula da direita eh maior que a atual, caso nao for retorna false
        if num < matrix[row][col+1] and matrix[row][col+1]:
            return False
    elif matrix_comparation[position][1] == 0:
        #nesse caso a celula da direita eh menor que a atual, caso nao for retorna false
        if num > matrix[row][col+1] and matrix[row][col+1]:
            return False
    if matrix_comparation[position][2] == 1:
        #nesse caso a celula de baixo eh maior que a atual, caso nao for retorna false
        if num < matrix[row+1][col] and matrix[row+1][col]:
            return False
    elif matrix_comparation[position][2] == 0:
        #nesse caso a celula de baixo eh menor que a atual, caso nao for retorna false
        if num > matrix[row+1][col] and matrix[row+1][col]:
            return False
    if matrix_comparation[position][3] == 1:
        #nesse caso a celula da esquerda eh maior que a atual, caso nao for retorna false
        if num < matrix[row][col-1] and matrix[row][col-1]:
            return False
    elif matrix_comparation[position][3] == 0:
        #nesse caso a celula da esquerda eh menor que a atual, caso nao for retorna false
        if num > matrix[row][col-1] and matrix[row][col-1]:
            return False

    return True

def limits(position, matrix_comp, visited, lim):
    #fazendo dfs para ver quantos numeros sao menores ou maiores que a celula atual
    #dessa forma eu nao preciso iterar de 1 ate 9 toda a vez para achar a celula ideal
    #a ideia eh se o numero foi maior que alguma celula e aquela celula for maior que outra, entao ele eh pelo menos 3, e assim segue a ideia
    #se ele for menor que alguma celula e aquela celula for menor que outra, entao ele eh pelo menos 7, e assim segue a ideia
    total = 1
    visited.append(position)
    if matrix_comp[position][0] == lim and position-9 not in visited:
        total += limits(position-9, matrix_comp, visited, lim)
    if matrix_comp[position][1] == lim and position+1 not in visited:
        total += limits(position+1, matrix_comp, visited, lim)
    if matrix_comp[position][2] == lim and position+9 not in visited:
        total += limits(position+9, matrix_comp, visited, lim)
    if matrix_comp[position][3] == lim and position-1 not in visited:
        total += limits(position-1, matrix_comp, visited, lim)

    return total




def solve(matrix, possibilities_matrix, matrix_comp):
    for row in range(9):
        for col in range(9):
            #so vejo celulas vazias
            if matrix[row][col] == 0:
                for num in possibilites_matrix[row*9+col]:
                    #testo todos os numeros de 1 a 9
                    # e vejo se eh valido
                    if is_a_valid_move(matrix, row, col, num, matrix_comp):
                        #caso for adiciono ele
                        matrix[row][col] = num
                        #chamo a funcao recursivamente para a proxima celula
                        if solve(matrix, possibilities_matrix, matrix_comp):
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

def get_possibilities_matrix(matrix_comp):
    matrix = []
    for i in range(81):
        element = []
        #vejo as possibilidade de cada celula seguindo a ideia explicada nos limites
        #naquele caso exemplo que coloquei comentando, aqui iteraria por 3 ate 8(pois precisa contar o 7)
        for j in range(limits(i, matrix_comp, [], 1), 11-limits(i, matrix_comp, [], 0)):
            element.append(j)
        matrix.append(element)
    return matrix

if __name__ == '__main__':
    start = time.time()
    matrix = [[0 for j in range(9)]for i in range(9)]
    #matriz de comparacao
    matrix_comp = [[-1, 1, 1, -1], [-1, 0, 0, 0], [-1, -1, 0, 1], [-1, 1, 1, -1], [-1, 1, 1, 0], [-1, -1, 0, 0], [-1, 0, 0, -1], [-1, 1, 0, 1], [-1, -1, 1, 0], [0, 0, 0, -1], [1, 1, 1, 1], [1, -1, 0, 0], [0, 0, 0, -1], [0, 1, 1, 1], [1, -1, 0, 0], [1, 0, 0, -1], [1, 1, 1, 1], [0, -1, 1, 0], [1, 0, -1, -1], [0, 0, -1, 1], [1, -1, -1, 1], [1, 1, -1, -1], [0, 0, -1, 0], [1, -1, -1, 1], [1, 1, -1, -1], [0, 1, -1, 0], [0, -1, -1, 0], [-1, 0, 0, -1], [-1, 1, 1, 1], [-1, -1, 0, 0], [-1, 1, 1, -1], [-1, 1, 1, 0], [-1, -1, 1, 0], [-1, 0, 1, -1], [-1, 1, 1, 1], [-1, -1, 0, 0], [1, 1, 1, -1], [0, 0, 1, 0], [1, -1, 1, 1], [0, 1, 1, -1], [0, 1, 0, 0], [0, -1, 0, 0], [0, 1, 0, -1], [0, 0, 0, 0], [1, -1, 1, 1], [0, 1, -1, -1], [0, 0, -1, 0], [0, -1, -1, 1], [0, 0, -1, -1], [1, 0, -1, 1], [1, -1, -1, 1], [1, 0, -1, -1], [1, 0, -1, 1], [0, -1, -1, 1], [-1, 0, 0, -1], [-1, 0, 1, 1], [-1, -1, 1, 1], [-1, 0, 0, -1], [-1, 0, 1, 1], [-1, -1, 1, 1], [-1, 0, 0, -1], [-1, 1, 1, 1], [-1, -1, 1, 0], [1, 1, 1, -1], [0, 0, 0, 0], [0, -1, 1, 1], [1, 1, 1, -1], [0, 0, 0, 0], [0, -1, 1, 1], [1, 1, 1, -1], [0, 0, 0, 0], [0, -1, 0, 1], [0, 0, -1, -1], [1, 1, -1, 1], [0, -1, -1, 0], [0, 0, -1, -1], [1, 1, -1, 1], [0, -1, -1, 0], [0, 0, -1, -1], [1, 0, -1, 1], [1, -1, -1, 1]]
    possibilites_matrix = get_possibilities_matrix(matrix_comp)
    if solve(matrix, possibilites_matrix, matrix_comp):
        for i in matrix:
            print(i)
        end = time.time()
        print(f'Total execution time: {end - start}s')
    else:
        print('There is no solution')