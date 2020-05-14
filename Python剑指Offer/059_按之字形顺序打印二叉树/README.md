### 题目描述

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

### 思路

层序打印即可。

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        num = 1
        list_node = [pRoot]
        res = []
        while True:
            length = len(list_node)
            if length ==0:
                break
            temp = []
            for _ in range(length):
                node = list_node.pop(0)
                temp.append(node.val)
                if node.left:
                    list_node.append(node.left)
                if node.right:
                    list_node.append(node.right)
            res.append(temp[::-1] if num%2==0 else temp[:])
            num += 1
        return res
                   
```

## 题目描述

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

### 思路

同上

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        num = 1
        list_node = [pRoot]
        res = []
        while True:
            length = len(list_node)
            if length ==0:
                break
            temp = []
            for _ in range(length):
                node = list_node.pop(0)
                temp.append(node.val)
                if node.left:
                    list_node.append(node.left)
                if node.right:
                    list_node.append(node.right)
            res.append(temp[::-1] if num%2==0 else temp[:])
        return res
```

