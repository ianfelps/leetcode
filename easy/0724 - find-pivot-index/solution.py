from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) # soma todos os numeros
        leftsum = 0 # armazena a soma dos numeros da esquerda
        for i, n in enumerate(nums): # percorre a lista (indice, numero)
            if leftsum == total - n - leftsum: # se o total da esquerda for igual ao total, menos o numero atual, menos o total da esquerda
                return i # retorna o indice
            leftsum += n # se nao, adiciona o numero atual ao total da esquerda
        return -1 # se nao encontrar, retorna -1