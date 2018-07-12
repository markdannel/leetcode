class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find(node1, node2):
    if node1 == None and node2 == None:
        return True
    elif node1 == None or node2 == None:
        return False
    if node1.val != node2.val:
        return False
    l = find(node1.left, node2.right)
    r = find(node1.right, node2.left)
    return l and r

root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(2)
root.right.left = TreeNode(4)
root.right.right= TreeNode(6)
root.left.left = TreeNode(6)
root.left.right= TreeNode(4)
root.left.right.right= TreeNode(4)

if root == None: print("err 1")#return True
if root.left == None and root.right == None: print("err 2")#return True
print("err 3", find(root.left, root.right))
