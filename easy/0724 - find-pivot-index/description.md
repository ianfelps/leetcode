# 724. Find Pivot Index
[LeetCode Link](https://leetcode.com/problems/find-pivot-index/description/)

Given an array of integers `nums`, calculate the pivot index of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return `-1`.

### Example:

```python
Input: nums = [1,7,3,6,5,6]
Output: 3
```

```python
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```

# Comentários

Um exemplo de **Prefix-Sum**. Pegamos a soma total da lista e iniciamos a variável para os números da esquerda. Percorrendo a lista (com índice e o número) e verificamos se o total da esquerda é igual ao total da lista, menos o número atual, menos o total da esquerda. Se sim, retornamos o índice. Se não, adicionamos o número atual ao total da esquerda, assim não precisamos recalcular o total da esquerda para cada iteração. Se não encontrar o pivô, retornamos -1.

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) # soma todos os numeros
        leftsum = 0 # armazena a soma dos numeros da esquerda
        for i, n in enumerate(nums): # percorre a lista (indice, numero)
            if leftsum == total - n - leftsum: # se o total da esquerda for igual ao total, menos o numero atual, menos o total da esquerda
                return i # retorna o indice
            leftsum += n # se nao, adiciona o numero atual ao total da esquerda
        return -1 # se nao encontrar, retorna -1
```