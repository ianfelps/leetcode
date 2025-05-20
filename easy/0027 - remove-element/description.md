# 27. Remove Element
[LeetCode Link](https://leetcode.com/problems/remove-element/description/)

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:
- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

# Comentários

Meu primeiro LeetCode! Um problema bem simples utilizando um loop para percorrer uma lista e uma validação para verificar se o número atual da lista é igual ao número que eu preciso remover, se for, eu removo ele da minha lista, se não, eu apenas incremento o contador.

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # inicializar o contador para percorrer a lista de numeros
        while i < len(nums): # percorrer a lista de numeros
            if nums[i] == val: # se o numero da lista for igual ao valor
                nums.pop(i) # remover o numero
            else: # se nao
                i += 1 # seguir para o proximo numero
```