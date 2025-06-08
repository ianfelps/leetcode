# 897. Increasing Order Search Tree
[LeetCode Link](https://leetcode.com/problems/increasing-order-search-tree/description/)

Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

### Example:

```python
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

# Comentários

Achei um pouco confuso, mas depois de insistir consegui entender melhor, utilizando a recursividade fica bem simples. Primeiro, verificamos se a raiz da árvore é nula, se for, retornamos o `tail` (que representa o próximo nó na sequência in-order). Caso contrário, aplicamos a recursão na sub-árvore esquerda para encontrar o menor nó, que será o novo início da estrutura reorganizada. Em seguida, removemos a ligação da raiz com seu filho esquerdo (a estrutura final não possui filhos esquerdos) e utilizamos a recursão na sub-árvore direita, conectando o resultado ao ponteiro direito da raiz atual. Por fim, retornamos o menor nó encontrado, garantindo que todos os nós estejam ligados apenas à direita e em ordem crescente.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
```