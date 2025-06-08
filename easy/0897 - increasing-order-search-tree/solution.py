from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root, tail = None):
        if not root: return tail # se a raiz for nula, retorna o tail
        res = self.increasingBST(root.left, root) # chama a funcao recursivamente busando o menor nó da esquerda
        root.left = None # o nó da esquerda recebe nulo (ao final, não teremos mais filhos da esquerda)
        root.right = self.increasingBST(root.right, tail) # chama a funcao recursivamente busando o menor nó da direita e associando ao nó da esquerda
        return res # retorna o menor nó