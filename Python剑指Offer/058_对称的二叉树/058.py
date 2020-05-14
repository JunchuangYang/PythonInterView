from collections import deque

__author__ = 'lenovo'
# -*- coding:utf-8 -*-
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
if __name__ == "__main__":
    T = Solution()
    T.construct_tree([5,5,5,5,'#','#',5,5,'#',5])
    print(T.isSymmetrical(T.root))