# 1367. Linked List in Binary Tree

Given a binary tree `root` and a linked list with `head` as the first node. 

Return True if all the elements in the linked list starting from the `head` correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

### Example:

```python
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
```
Explanation: Nodes from the list form a subpath in the binary Tree.  

# Comentários

Nesse problema a solução de *Brute Force* foi muito eficiente e muito simples, a ideia principal é utilizar da recursividade para percorrer a **árvore binária** e a **lista encadeada** ao mesmo tempo.  
Primeiro, criamos uma função auxiliar (`helper()`) para verificar se a partir de um determinado nó da árvore é possível seguir um caminho descendente que corresponda à sequência de valores da lista . A função compara o valor atual da lista com o valor atual da árvore e, se forem iguais, continua a verificação recursivamente nos filhos da esquerda e da direita da árvore com o próximo nó da lista. Se a lista for completamente percorrida, significa que encontramos um caminho correspondente e retornamos `True`.  
A função principal (`isSubPath()`) verifica se esse caminho pode começar a partir da raiz atual ou de qualquer outro nó da árvore (sub-árvores esquerda e direita), garantindo assim que todos os possíveis pontos de partida sejam considerados.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.helper(head, root): # se a funcao auxiliar retornar True
            return True # a lista pertence a arvore
        if not root: # se a arvore for vazia
            return False # retorna False
        return (self.isSubPath(head, root.left) or # chama a funcao recursivamente para a sub-árvore esquerda
                self.isSubPath(head, root.right)) # chama a funcao recursivamente para a sub-árvore direita

    # função auxiliar para percorrer a lista e a arvore
    def helper(self, list_node, tree_node):
        if not list_node: # se o nó da lista for vazio
            return True # retorna True
        if not tree_node or list_node.val != tree_node.val: # se o nó da árvore for vazio ou o nó da lista for diferente do nó da árvore
            return False # retorna False
        return (self.helper(list_node.next, tree_node.left) or # chama a funcao recursivamente para o próximo nó da lista e o filho esquerdo da árvore
                self.helper(list_node.next, tree_node.right)) # chama a funcao recursivamente para o próximo nó da lista e o filho direito da árvore
```