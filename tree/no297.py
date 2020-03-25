# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 示例: 
# 你可以将以下二叉树：
#     1
#    / \
#   2   3
#      / \
#     4   5(d, 2*(r-1)+1)2**d
# 序列化为 "[1,2,3,null,null,4,5]"
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        self.encode_dfs(root, res, 0, 0)
        return ",".join(list(map(str, res)))

    def encode_dfs(self, root, res, deep, offset):
        if not root:
            return 
        if len(res) < (2**(deep+1)-1):
            res += ['null']*(2**deep)
        res[2**deep+offset-1] = root.val

        self.encode_dfs(root.left, res, deep+1, 2*offset)
        self.encode_dfs(root.right, res, deep+1, 2*offset+1)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        lst = data[1:-1].split(",")
        root = self.decode_dfs(lst, 0, 0)
        return root

    def decode_dfs(self, data, deep, offset):
        pos = 2**deep+offset
        if len(data) < pos:
            return None
        if data[pos-1] == 'null':
            return None
        node = TreeNode(data[pos-1])
        node.left = self.decode_dfs(data, deep+1, 2*offset)
        node.right = self.decode_dfs(data, deep+1, 2*offset+1)
        return node

codec = Codec()
data = "[1,2,3,null,null,4,5,null,null,null,null,6,7,null,9]"
root = codec.deserialize(data)
res = codec.serialize(root)
print(res)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))