# 1721. Swapping Nodes in a Linked List
[LeetCode Link](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/)

You are given the `head` of a linked list, and an integer `k`.

Return the head of the linked list after **swapping** the values of the `k'th` node from the beginning and the `k'th` node from the end (the list is **1-indexed**).

### Example:

```python
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

# Comentários

Semelhante com o problema 0019, mas agora trocando valores. Primeiro temos que encontrar os nós que serão trocados, o n-ésimo nó encontramos percorrendo a lista `k - 1` vezes, e o n-ésimo nó (de trás para frente) encontramos com ponteiros auxiliares, entendendo que a distância do n-ésimo nó para o começo da lista é a mesma distância do n-ésimo nó para o fim da lista, ou seja, criamos dois ponteiros, `left` e `right`, e colocamos `k - 1` de distância entre eles, então percorremos a lista até `right` chegar ao fim, matematicamente encontrando o n-ésimo nó. Ao encontrar os dois nós, trocamos os valores entre eles e retornamos a cabeça da lista.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head # o nó atual recebe a cabeca da lista
        # encontrar o n-esimo nó
        for i in range(k - 1): # percorre a lista k - 1 vezes
            current = current.next # o nó atual recebe o proximo nó
        # encontrar o n-esimo nó (de trás para frente)
        left = current # o nó esquerdo recebe o n-esimo nó (nó atual)
        right = head # o nó direito recebe a cabeca da lista
        while current.next: # enquanto o próximo nó do nó atual não for nulo
            current = current.next # o nó atual recebe o proximo nó
            right = right.next # o nó direito recebe o proximo nó
        # trocar os valores
        left.val, right.val = right.val, left.val # troca o valor do nó esquerdo com o valor do nó direito
        return head # retorna a cabeca da lista
```