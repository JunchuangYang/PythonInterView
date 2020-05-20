__author__ = 'lenovo'
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left)  + self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        self.flag += 1
        slist = s.split(',')
        if self.flag >= len(slist):
            return None
        node = None
        if slist[self.flag]!='#':
            node = TreeNode(int(slist[self.flag]))
            node.left = self.Deserialize(s)
            node.right = self.Deserialize(s)
        return node