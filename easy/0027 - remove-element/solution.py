from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # inicializar o contador para percorrer a lista de numeros
        while i < len(nums): # percorrer a lista de numeros
            if nums[i] == val: # se o numero da lista for igual ao valor
                nums.pop(i) # remover o numero
            else: # se nao
                i += 1 # seguir para o proximo numero