from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
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