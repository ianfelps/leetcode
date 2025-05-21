from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for m in range(len(matrix)): # percorrer a matriz no eixo x (linhas)
            for n in range(len(matrix[0])): # percorrer a matriz no eixo y (colunas)
                if matrix[m][n] == 0: # se o valor da celula for igual a 0
                    self.aux(matrix, m - 1, n, "C") # pegue a celula de cima
                    self.aux(matrix, m + 1, n, "B") # pegue a celula de baixo
                    self.aux(matrix, m, n - 1, "E") # pegue a celula da esquerda
                    self.aux(matrix, m, n + 1, "D") # pegue a celula da direita
        
        for m in range(len(matrix)): # percorrer a matriz no eixo x (linhas)
            for n in range(len(matrix[0])): # percorrer a matriz no eixo y (colunas)
                if matrix[m][n] == "*": # se o valor da celula for igual a um "*"
                    matrix[m][n] = 0 # substitui o valor por 0

        return matrix # retorna a matriz

    # funcao auxiliar para inserir asteriscos e passar para as proximas celulas
    def aux(self, matrix, m, n, direction):
        if (0 <= m < len(matrix)) and (0 <= n < len(matrix[0])) and matrix[m][n] != 0: # verifica se nao ultrapassou o limite da matriz e se o valor nao é igual a 0
            matrix[m][n] = "*" # substitui o valor por um asterisco

            if direction == "C": # se a direcao foi para cima
                self.aux(matrix, m - 1, n, "C") # pega a proxima celula de cima
            elif direction == "B": # se a direcao foi para baixo
                self.aux(matrix, m + 1, n, "B") # pega a proxima celula de baixo
            elif direction == "E": # se a direcao foi para esquerda
                self.aux(matrix, m, n - 1, "E") # pega a proxima celula da esquerda
            elif direction == "D": # se a direcao foi para direita
                self.aux(matrix, m, n + 1, "D") # pega a proxima celula da direita