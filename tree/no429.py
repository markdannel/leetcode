# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 例如，给定一个 3叉树 :
#      1
#    / | \
#   3  2  4
#  / \
# 5   6
# 返回其层序遍历:
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
# 说明:
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue, res = [(root,0)], []
        ## BFS
        # while queue:
        #     cur, d = queue.pop(0)
        #     for ch in cur.children:
        #         queue.append((ch, d+1))
        #     if len(res) == d:
        #         res.append([cur.val])
        #     else:
        #         res[d].append(cur.val)
        
        ## DFS
        def dfs(root, depth):
            if not root:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            for ch in root.children:
                self.dfs(ch, depth+1)
        dfs(root, 0)
        return res