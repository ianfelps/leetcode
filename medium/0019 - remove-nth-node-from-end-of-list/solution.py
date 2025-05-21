from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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