# 229. Majority Element II
[LeetCode Link](https://leetcode.com/problems/majority-element-ii/)

Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times.

### Example:

```python
Input: nums = [3,2,3]
Output: [3]
```

# Comentários

Para começar, criamos uma lista para armazenar o resultado, um dicionario para contar as ocorrencias dos numeros e um variavel para armazenar o tamanho da lista. Em seguida percorremos a lista com os numeros e verificamos se o numero ainda nao foi contabilizado. Se nao, atribuimos o numero como chave com o valor 1. Caso contrario, incrementamos 1 na contagem. Para a validação final, armazenamos o calculo de `⌊ n/3 ⌋` em uma variavel (`k`) e percorremos o dicionario verificando se a frequencia foi maior que `k`. Se sim, adicionamos o numero a lista de resultados. Por fim, retornamos a lista com todos os resultados.

```python
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
```