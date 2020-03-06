# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        n = preorder.pop(0)
        node = TreeNode(n)
        x = inorder.index(n)
        
        node.left = self.buildTree(preorder[:x], inorder[:x])
        node.right = self.buildTree(preorder[x+1:], inorder[x+1:])
        return node
