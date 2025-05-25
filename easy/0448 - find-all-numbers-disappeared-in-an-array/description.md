# 448. Find All Numbers Disappeared in an Array
[LeetCode Link](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

# Example:

```python
Input: nums = [4,3,2,7,8,2,3,1]

Output: [5,6]
```

# Comentários

Primeiro criamos um conjunto com os elementos da lista. Depois retornamos uma lista com os números de 1 até `n` (tamanho da lista) que não estão presentes no conjunto. Bem simples!

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # cria um conjunto com os elementos da lista
        s = set(nums)
        # retorna uma lista com os numeros de 1 a n (tamanho da lista) que nao estao presentes no conjunto
        return [i for i in range(1, len(nums)+1) if i not in s]
```