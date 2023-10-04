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
        # Verificando se o número já existe na linha ou na coluna
        if matrix[row][i] == num or matrix[i][col] == num:
            return False

    row_start, col_start = 3 * (row // 3), 3 * (col // 3)

    # Verificando se o número já existe no bloco
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if matrix[i][j] == num:
                return False

    position = row * 9 + col

    # Comparando a célula para ver as possibilidades
    # 1 significa que a célula é maior que a atual
    # 0 significa que a célula é menor que a atual
    # -1 significa que a célula não faz comparação naquela direção
    if nodes[position].up == 1:
        # Nesse caso, a célula de cima é maior que a atual, caso não for, retorna False
        if num < matrix[row - 1][col] and matrix[row - 1][col]:
            return False
    elif nodes[position].up == 0:
        # Nesse caso, a célula de cima é menor que a atual, caso não for, retorna False
        if num > matrix[row - 1][col] and matrix[row - 1][col]:
            return False

    if nodes[position].right == 1:
        # Nesse caso, a célula da direita é maior que a atual, caso não for, retorna False
        if num < matrix[row][col + 1] and matrix[row][col + 1]:
            return False
    elif nodes[position].right == 0:
        # Nesse caso, a célula da direita é menor que a atual, caso não for, retorna False
        if num > matrix[row][col + 1] and matrix[row][col + 1]:
            return False

    if nodes[position].down == 1:
        # Nesse caso, a célula de baixo é maior que a atual, caso não for, retorna False
        if num < matrix[row + 1][col] and matrix[row + 1][col]:
            return False
    elif nodes[position].down == 0:
        # Nesse caso, a célula de baixo é menor que a atual, caso não for, retorna False
        if num > matrix[row + 1][col] and matrix[row + 1][col]:
            return False

    if nodes[position].left == 1:
        # Nesse caso, a célula da esquerda é maior que a atual, caso não for, retorna False
        if num < matrix[row][col - 1] and matrix[row][col - 1]:
            return False
    elif nodes[position].left == 0:
        # Nesse caso, a célula da esquerda é menor que a atual, caso não for, retorna False
        if num > matrix[row][col - 1] and matrix[row][col - 1]:
            return False

    return True


def limits(position, nodes, visited, lim):
    # Fazendo DFS para ver quantos números são menores ou maiores que a célula atual
    # Dessa forma, não é necessário iterar de 1 até 9 toda vez para encontrar a célula ideal
    # A ideia é se o número foi maior que alguma célula e aquela célula for maior que outra, então ele é pelo menos 3, e assim segue a ideia
    # Se ele for menor que alguma célula e aquela célula for menor que outra, então ele é pelo menos 7, e assim segue a ideia
    total = 1
    visited.append(position)
    if nodes[position].up == lim and position - 9 not in visited:
        total += limits(position - 9, nodes, visited, lim)

    if nodes[position].right == lim and position + 1 not in visited:
        total += limits(position + 1, nodes, visited, lim)

    if nodes[position].down == lim and position + 9 not in visited:
        total += limits(position + 9, nodes, visited, lim)

    if nodes[position].left == lim and position - 1 not in visited:
        total += limits(position - 1, nodes, visited, lim)

    return total


def set_nodes(result_matrix):
    # Criando os nós
    nodes = []
    for i in range(81):
        nodes.append(Node.create_node())

    # Configurando os valores de cada nó
    for i in range(81):
        # Caso o elemento for da primeira linha ou for alguma borda de cima da região, então ele não tem célula acima
        if i % 27 <= 8 or i // 9 == 0:
            nodes[i].up = -1
        # Caso contrário, ele tem célula acima e vejo se ela é maior ou menor que a atual
        else:
            nodes[i].up = 1 if result_matrix[i] > result_matrix[i - 9] else 0

        # Caso o elemento for borda direita de alguma região ou estiver na última coluna, então ele não tem célula a direita
        if i % 3 == 2 or i % 9 == 8:
            nodes[i].right = -1
        # Caso contrário, ele tem célula a direita e vejo se ela é maior ou menor que a atual
        else:
            nodes[i].right = 1 if result_matrix[i] > result_matrix[i + 1] else 0

        # Caso o elemento for borda de baixo de alguma região ou estiver na última linha, então ele não tem célula abaixo
        if i % 27 >= 18 or i // 9 == 8:
            nodes[i].down = -1
        # Caso contrário, ele tem célula abaixo e vejo se ela é maior ou menor que a atual
        else:
            nodes[i].down = 1 if result_matrix[i] > result_matrix[i + 9] else 0

        # Caso o elemento for borda esquerda de alguma região ou estiver na primeira coluna, então ele não tem célula a esquerda
        if not i % 3 or not i % 9:
            nodes[i].left = -1
        # Caso contrário, ele tem célula a esquerda e vejo se ela é maior ou menor que a atual
        else:
            nodes[i].left = 1 if result_matrix[i] > result_matrix[i - 1] else 0

    return nodes


def solve(matrix, possibilities_matrix, nodes):
    for row in range(9):
        for col in range(9):
            # Só vejo celulas vazias
            if matrix[row][col] == 0:
                for num in possibilities_matrix[row * 9 + col]:
                    # Testo todos os números de 1 a 9 e vejo se é válido
                    if is_a_valid_move(matrix, row, col, num, nodes):
                        # Caso seja válido, adiciono o número
                        matrix[row][col] = num
                        # Chamo a função recursivamente para a próxima célula
                        if solve(matrix, possibilities_matrix, nodes):
                            # Caso ele consiga resolver todas as recursões, retorna True
                            return True
                        # Caso contrário, ele retrocede uma recursão na stack colocando 0 na célula
                        # e busca o próximo número possível dentro do loop de 1 a 9
                        matrix[row][col] = 0
                # Se testar todos os números e não conseguir achar nenhum válido
                # quer dizer que não há solução possível
                return False
    return True


def get_possibilities_matrix(nodes):
    matrix = []
    for i in range(81):
        element = []
        # Vejo as possibilidades de cada célula seguindo a ideia explicada nos limites
        # Naquele caso exemplo que coloquei comentando, aqui iteraria por 3 até 8 (pois precisa contar o 7)
        for j in range(limits(i, nodes, [], 1), 11 - limits(i, nodes, [], 0)):
            element.append(j)
        matrix.append(element)

    return matrix


if __name__ == '__main__':
    start = time.time()
    matrix = [[0 for j in range(9)] for i in range(9)]
    result_matrix = [9, 2, 4, 8, 7, 3, 1, 6, 5,
                     1, 8, 5, 2, 6, 4, 7, 9, 3,
                     3, 6, 7, 9, 1, 5, 8, 4, 2,
                     4, 9, 3, 7, 5, 2, 6, 8, 1,
                     7, 5, 8, 6, 4, 1, 3, 2, 9,
                     6, 1, 2, 3, 8, 9, 4, 5, 7,
                     2, 4, 9, 1, 3, 8, 5, 7, 6,
                     8, 3, 6, 5, 2, 7, 9, 1, 4,
                     5, 7, 1, 4, 9, 6, 2, 3, 8]

    nodes = set_nodes(result_matrix)
    possibilities_matrix = get_possibilities_matrix(nodes)
    if solve(matrix, possibilities_matrix, nodes):
        for i in matrix:
            print(i)
        end = time.time()
        print(f'Total execution time: {end - start}s')
    else:
        print('There is no solution')

   
