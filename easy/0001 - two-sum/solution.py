from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # cria um dicionario (hashmap)
        for i in range(len(nums)): # percorre a lista
            diff = target - nums[i] #! calcula a diferenca entre o valor alvo e o valor da lista
            if diff in seen: # se a diferenca ja estiver no dicionario
                return [seen[diff], i] # retorna os indices
            else: # se nao
                seen[nums[i]] = i # adiciona o valor da lista ao dicionario