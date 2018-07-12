class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

data = []
def find(root, deep):
    if root == None:
        return
    if len(data) < deep+1:
        data.append([])
    data[deep].append(root.val)
    deep += 1
    find(root.left, deep)
    find(root.right, deep)
    deep -= 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(2)
root.right.left = TreeNode(4)
root.right.right= TreeNode(6)
root.left.left = TreeNode(6)
root.left.right= TreeNode(4)
root.left.right.right= TreeNode(4)

find(root, 0)
print(data)