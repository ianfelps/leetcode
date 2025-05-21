# 19. Remove Nth Node From End of List
[LeetCode Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

### Example:

```python
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

# Comentários

Gostei muito da implementação. Criamos um nó auxiliar para facilitar o tratamento de casos especiais (como a remoção do primeiro nó). Em seguida, dois ponteiros (`ahead` e `behind`) são inicializados no nó auxiliar, e o ponteiro `ahead` é movido `n + 1` posições à frente. Isso cria uma distância de `n` nós entre os dois ponteiros. Em seguida, ambos os ponteiros são movidos juntos até que `ahead` atinja o final da lista. Nesse momento, `behind` estará imediatamente antes do nó a ser removido, que é então excluído ajustar o ponteiro para pular esse nó. Por fim, retornamos o início atualizado da lista.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux = ListNode() # cria um nó auxiliar
        aux.next = head # o nó auxiliar recebe o head (inicio da lista)
        behind = ahead = aux # o behind recebe o auxiliar e o ahead recebe o auxiliar

        for _ in range(n + 1): # percorre a lista n + 1 vezes
            ahead = ahead.next # o ahead recebe o proximo nó

        # behind e ahead possuem n nós de distancia

        while ahead: # enquanto o ahead nao for nulo (fim da lista)
            behind = behind.next # o behind recebe o proximo nó
            ahead = ahead.next # o ahead recebe o proximo nó

        behind.next = behind.next.next # o proximo nó do behind recebe o proximo do proximo nó ("pulando" o n-esimo nó)
        return aux.next # retorna o inicio da lista
```