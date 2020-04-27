### 题目描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

### 思路

二叉搜索树性质有：

- 没有相同结点
- 值：左<根<右

因此我们需要，中序遍历中：

- pre.right = curr
- curr.left = pre

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pre = None
        
    def Convert(self, root):
        # write code here
        if not root: 
            return None
        self.helper(root)
        while root.left:
            root = root.left
        return root

    def helper(self, cur):
        if not cur: 
            return None
        self.helper(cur.left)
        cur.left = self.pre
        if self.pre:
            self.pre.right = cur
        self.pre = cur
        self.helper(cur.right)
```

