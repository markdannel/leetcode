# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 案例 1:
# 输入: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# 输出: True
# 案例 2:
# 输入: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 28
# 输出: False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        listt = self.inorder(root)
        le, ri = 0, len(listt)-1
        if k > 2*listt[ri]:
            return False
        lemin = 0
        while le < ri:
            summ = listt[le] + listt[ri]
            if summ < k:
                le += 1
                lemin = min(lemin, le)
            elif summ > k:
                ri -= 1
                le = lemin
            else:
                return True
        return False
    
    def inorder(self, root):
        if not root:
            return None
        res = []
        if root.left:
            res += self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res += self.inorder(root.right)
        return res

s = Solution()
root = TreeNode(12)
root.left = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)

root.right = TreeNode(18)
root.right.left = TreeNode(15)
root.right.right = TreeNode(20)
root.right.right.left = TreeNode(19)

k=11
res = s.findTarget(root,k)
print(res)