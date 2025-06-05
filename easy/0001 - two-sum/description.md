# 1. Two Sum
[LeetCode Link](https://leetcode.com/problems/two-sum/description/)

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example:

```python
Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

# Comentários

Para resolver o problema percorrendo a lista apenas uma vez, utilizamos hashmap. Primeiro criamos um dicionário (hashmap) e percorremos a lista calculando a diferença entre o valor alvo e o valor da lista. Se a diferença já estiver no dicionário, retornamos os índices (do valor alvo e do atual valor da lista). Caso contrario, adicionamos o valor da lista ao dicionário e continuamos percorrendo a lista.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # cria um dicionario (hashmap)
        for i in range(len(nums)): # percorre a lista
            diff = target - nums[i] #! calcula a diferenca entre o valor alvo e o atual valor da lista
            if diff in seen: # se a diferenca ja estiver no dicionario
                return [seen[diff], i] # retorna os indices
            else: # se nao
                seen[nums[i]] = i # adiciona o valor da lista ao dicionario
```