### 题目描述

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

### 思路

二叉树层次遍历，用队列存储每层结点，再依次弹出。

```python
def bfs(tree):
    if not tree:
        return None
    stack = [tree]
    ret = []
    while stack:
        node = stack.pop(0)
        ret.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret
```

[详见：](<https://github.com/JunchuangYang/PythonInterView/blob/master/Python%E5%89%91%E6%8C%87Offer/018_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%95%9C%E5%83%8F/018.py>)

