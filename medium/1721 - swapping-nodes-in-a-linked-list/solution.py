# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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