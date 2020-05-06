## 树的层序遍历
BFS利用queue，从根节点开始存每层的点，此时恰好可以按照层序顺序取到所有节点，在保存进节点时同时保存树高，可以得到结果
# N叉树非递归时，取栈第0个就是层序遍历，取栈最后一个就是深度遍历
如no429
BFS实现框架：
```
queue, res = [(root,0)], []
while queue:
    cur, d = queue.pop(0)
    for ch in cur.children:
        queue.append((ch, d+1))
    if len(res) == d:
        res.append([cur.val])
    else:
        res[d].append(cur.val)
```

DFS实现：
```
def dfs(root, depth):
    if not root:
        return None
    if len(res) <= depth:
        res.append([])
    res[depth].append(root.val)
    for ch in root.children:
        self.dfs(ch, depth+1)
```
