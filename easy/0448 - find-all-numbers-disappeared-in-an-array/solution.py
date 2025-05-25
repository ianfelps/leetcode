from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        # cria um conjunto com os elementos da lista
        s = set(nums)
        # retorna uma lista com os numeros de 1 a n (tamanho da lista) que nao estao presentes no conjunto
        return [i for i in range(1, len(nums)+1) if i not in s]