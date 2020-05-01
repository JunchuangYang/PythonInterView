### 题目描述

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

### 思路

1、递归。

2、层序遍历。

```python
    @staticmethod
    def solution1(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return 1 + max(Tree.solution1(node.left) , Tree.solution1(node.right))

    @staticmethod
    def solution2(node):
        n = 0
        q = deque([node])
        while q:
            m = len(q)
            for _ in range(m):
                node1 = q.popleft()
                if node1 and node1.left:
                    q.append(node1.left)
                if node1 and node1.right:
                    q.append(node1.right)
            n += 1
        return n
```

