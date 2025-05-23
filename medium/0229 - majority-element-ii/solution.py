from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [] # criar lista para resultado
        hashmap = {} # criar um dicionario para contar as ocorrencias dos numeros
        n = len(nums) # calcular tamanho da lista
        for num in nums: # percorrer a lista de numeros
            if num not in hashmap: # se o numero ainda nao foi contabilizado
                hashmap[num] = 1 # atribuir com valor 1
            else: # se ja foi contabilizado
                hashmap[num] += 1 # incrementar 1
        k = n // 3 # calculo de ⌊ n/3 ⌋
        for key, val in hashmap.items(): # percorrer elementos no hashmap (numero, frequencia)
            if val > k: # se a frequencia foi maior que k (⌊ n/3 ⌋)
                res.append(key) # adicione a lista de resultados
        return res # retorna a lista com os resultados