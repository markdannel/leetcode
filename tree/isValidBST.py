class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
arr = []
def find2(node):
    if node == None:
        return
    find2(node.left)
    arr.append(node.val)
    find2(node.right)


def find(node, val, isLeft, first=False):
    # 当前节点为空？
    if node:
        lf = rf = True
        # 左子节点?
        if node.left:
            # 当前节点为其父节点的左节点
            if isLeft:
                # 当前值 vs 左子节点值
                if node.val <= node.left.val:
                    lf = False
            # 右节点
            else:
                if node.val <= node.left.val:
                    lf = False
                # 当前节点为其父节点的右节点，其子节点要与“爷爷”节点比较
                else:
                    if val >= node.left.val:
                        lf = False
                        
        if node.right:
            if isLeft:
                if node.val >= node.right.val:
                    rf = False
                else:
                    # first 为清除根节点没有父节点的影响
                    if val <= node.right.val and first == False:
                        rf = False
            else:
                if node.val >= node.right.val:
                    rf = False
                
        clf = find(node.left, node.val, True)
        crf = find(node.right, node.val, False)
        return lf and rf and clf and crf
    else:
        return True


node = TreeNode(5)
node.left = TreeNode(1)
node.right= TreeNode(4)
node.right.left = TreeNode(3)
node.right.right= TreeNode(6)
find2(node)
l = len(arr)
i = 1
while i < l:
    if arr[i-1] >= a[i]:
        return False
    i += 1
return True
print(arr)
#if node == None: return True
#print("ff = ", find(node, node.val, True, True))