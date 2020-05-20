## 题目描述

给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

### 思路

对于二叉搜索树来说，中序遍历正好为数列的升序序列。（- 注意k可能大于二叉树节点个数）

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.res = []
    def KthNode(self, pRoot, k):
        self.dfs(pRoot,k)
        return self.res[k-1] if 0<k<=len(self.res) else None
    def dfs(self, pRoot, k):
        # write code here
        if pRoot:
            self.dfs(pRoot.left,k)
            self.res.append(pRoot)
            self.dfs(pRoot.right,k)
```

