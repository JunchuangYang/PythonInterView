# -*- coding:utf-8 -*-
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def construct_tree(self,values):
        '''
        根据二叉树的层次遍历顺序构建二叉树
        '''
        if values is None:
            return None

        self.root = TreeNode(values[0])
        queue = deque([self.root])
        length = len(values)
        num = 1
        while num < length:
            node = queue.popleft()
            if node :
                node.left = TreeNode(values[num])
                queue.append(node.left)
                if num + 1 < length:
                    node.right = TreeNode(values[num+1])
                    queue.append(node.right)
                    num += 1
                num += 1
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
if __name__=="__main__":
    S=Solution.construct_tree([8,6,10,5,7,9,11])
    print(S.Print(S.root))
                   