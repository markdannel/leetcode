def find(node, deep):
    mdeep = deep
    if node:
        deep += 1
        ldeep = find(node.left, deep)
        rdeep = find(node.right, deep)
        deep -= 1
        mdeep = max(mdeep, ldeep, rdeep)
        return mdeep
    else:
        return deep
deep = 0
deep = find(root, 0)
return deep