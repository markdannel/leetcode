class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right= sortedArrayToBST(nums[mid+1:])
    return root

nums = [-10,-3,0,5,9]
r = sortedArrayToBST(nums)
print(r.val,r.left.val,r.right.val, r.left.left.val)
print(r.right.right, r.right.left.val)