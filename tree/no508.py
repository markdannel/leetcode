class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def lastorder(node):
            if not node:
                return 0
            le = lastorder(node.left)
            ri = lastorder(node.right)
            node.val += le + ri
            return node.val
        lastorder(root)
        return self.findMode(root)

    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        counter = collections.Counter()
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder(node.right)
            counter[node.val] += 1
        inorder(root)
        res = []
        maxx = max(counter.values())
        for k,v in counter.items():
            if v==maxx:
                res.append(k)
        return res;