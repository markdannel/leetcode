# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#中序遍历 inorder = [9,3,15,20,7]
#后序遍历 postorder = [9,15,7,20,3]
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        n = postorder.pop()
        node = TreeNode(n)
        x = inorder.index(n)

        node.left = self.buildTree(inorder[:x], postorder[:x])
        node.right = self.buildTree(inorder[x+1:], postorder[x:])
        return node