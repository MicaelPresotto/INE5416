import time

class Node:
    def __init__(self):
        self.up = None
        self.right = None
        self.down = None
        self.left = None
    
    @classmethod
    def create_node(cls):
        return cls()

def is_a_valid_move(matrix, row, col, num, nodes):
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
    if nodes[position].up == 1:
        #nesse caso a celula de cima eh maior que a atual, caso nao for retorna false 
        if num < matrix[row-1][col] and matrix[row-1][col]:
            return False
    elif nodes[position].up == 0:
        #nesse caso a celula de cima eh menor que a atual, caso nao for retorna false
        if num > matrix[row-1][col] and matrix[row-1][col]:
            return False
        
    if nodes[position].right == 1:
        #nesse caso a celula da direita eh maior que a atual, caso nao for retorna false
        if num < matrix[row][col+1] and matrix[row][col+1]:
            return False
        
    elif nodes[position].right == 0:
        #nesse caso a celula da direita eh menor que a atual, caso nao for retorna false
        if num > matrix[row][col+1] and matrix[row][col+1]:
            return False
        
    if nodes[position].down == 1:
        #nesse caso a celula de baixo eh maior que a atual, caso nao for retorna false
        if num < matrix[row+1][col] and matrix[row+1][col]:
            return False
        
    elif nodes[position].down == 0:
        #nesse caso a celula de baixo eh menor que a atual, caso nao for retorna false
        if num > matrix[row+1][col] and matrix[row+1][col]:
            return False
        
    if nodes[position].left == 1:
        #nesse caso a celula da esquerda eh maior que a atual, caso nao for retorna false
        if num < matrix[row][col-1] and matrix[row][col-1]:
            return False
        
    elif nodes[position].left == 0:
        #nesse caso a celula da esquerda eh menor que a atual, caso nao for retorna false
        if num > matrix[row][col-1] and matrix[row][col-1]:
            return False

    return True

def limits(position, nodes, visited, lim):
    #fazendo dfs para ver quantos numeros sao menores ou maiores que a celula atual
    #dessa forma eu nao preciso iterar de 1 ate 9 toda a vez para achar a celula ideal
    #a ideia eh se o numero foi maior que alguma celula e aquela celula for maior que outra, entao ele eh pelo menos 3, e assim segue a ideia
    #se ele for menor que alguma celula e aquela celula for menor que outra, entao ele eh pelo menos 7, e assim segue a ideia
    total = 1
    visited.append(position)
    if nodes[position].up == lim and position-9 not in visited:
        total += limits(position-9, nodes, visited, lim)

    if nodes[position].right == lim and position+1 not in visited:
        total += limits(position+1, nodes, visited, lim)

    if nodes[position].down == lim and position+9 not in visited:
        total += limits(position+9, nodes, visited, lim)

    if nodes[position].left == lim and position-1 not in visited:
        total += limits(position-1, nodes, visited, lim)

    return total

def set_nodes(result_matrix):
    #criando os nos
    nodes = []
    for i in range(81):
        nodes.append(Node.create_node())
    
    #setando os valores de cada no
    for i in range(81):
        if i%27 <=8 or i//9 == 0:
            nodes[i].up = -1
        else:
            nodes[i].up = 1 if result_matrix[i] > result_matrix[i-9] else 0

        if i%3 == 2 or i%9 == 8:
            nodes[i].right = -1
        else:
            nodes[i].right = 1 if result_matrix[i] > result_matrix[i+1] else 0
        if i%27 >= 18 or i//9 == 8:
            nodes[i].down = -1
        else:
            nodes[i].down = 1 if result_matrix[i] > result_matrix[i+9] else 0
        
        if not i%3 or not i%9:
            nodes[i].left = -1
        else:
            nodes[i].left = 1 if result_matrix[i] > result_matrix[i-1] else 0

    return nodes






def solve(matrix, possibilities_matrix, nodes):
    for row in range(9):
        for col in range(9):
            #so vejo celulas vazias
            if matrix[row][col] == 0:
                for num in possibilites_matrix[row*9+col]:
                    #testo todos os numeros de 1 a 9
                    # e vejo se eh valido
                    if is_a_valid_move(matrix, row, col, num, nodes):
                        #caso for adiciono ele
                        matrix[row][col] = num
                        #chamo a funcao recursivamente para a proxima celula
                        if solve(matrix, possibilities_matrix, nodes):
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

def get_possibilities_matrix(nodes):
    matrix = []
    for i in range(81):
        element = []
        #vejo as possibilidade de cada celula seguindo a ideia explicada nos limites
        #naquele caso exemplo que coloquei comentando, aqui iteraria por 3 ate 8(pois precisa contar o 7)
        for j in range(limits(i, nodes, [], 1), 11-limits(i, nodes, [], 0)):
            element.append(j)
        matrix.append(element)

    return matrix

if __name__ == '__main__':
    start = time.time()
    matrix = [[0 for j in range(9)]for i in range(9)]
    result_matrix = [9,2,4,8,7,3,1,6,5,
        1,8,5,2,6,4,7,9,3,
        3,6,7,9,1,5,8,4,2,
        4,9,3,7,5,2,6,8,1,
        7,5,8,6,4,1,3,2,9,
        6,1,2,3,8,9,4,5,7,
        2,4,9,1,3,8,5,7,6,
        8,3,6,5,2,7,9,1,4,
        5,7,1,4,9,6,2,3,8]
    nodes = set_nodes(result_matrix)
    possibilites_matrix = get_possibilities_matrix(nodes)
    if solve(matrix, possibilites_matrix, nodes):
        for i in matrix:
            print(i)
        end = time.time()
        print(f'Total execution time: {end - start}s')
    else:
        print('There is no solution')