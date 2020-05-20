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