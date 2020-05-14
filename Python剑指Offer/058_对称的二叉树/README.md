## 题目描述

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

### 思路

一. 两种中序遍历

- 1. 左->根->右
- 1. 右->根->左

```python
    def isSymmetrical(self, pRoot):
        res1 = self.inorder1(pRoot)
        res2 = self.inorder2(pRoot)
        print(res1,res2)
        if res1 == res2:
            return True
        return False
    #左根右
    def inorder1(self,root):

        res = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res
    # 右根左
    def inorder2(self,root):

        res = []
        def dfs(node):
            if node.right:
                dfs(node.right)
            res.append(node.val)
            if node.left:
                dfs(node.left)
        dfs(root)
        return res
```



二、同时进行中左右 和中右左的遍历，并在遍历的时候比较节点

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isS(pRoot.left,pRoot.right)
    
    def isS(self,nodel,noder):
        if not nodel and not noder:
            return True
        if not nodel or not noder:
            return False
        if nodel.val != noder.val:
            return False
        return self.isS(nodel.left,noder.right) and self.isS(nodel.right,noder.left)

```

