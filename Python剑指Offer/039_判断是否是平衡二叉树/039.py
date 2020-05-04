__author__ = 'lenovo'
from collections import deque

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self,values):
        if not values:
            return None

        self.root = TreeNode(values[0])
        n = len(values)
        i = 1
        q = deque([self.root])
        while i < n:
            node = q.popleft()
            if node:
                node.left = TreeNode(values[i]) if values[i] else None
                q.append(node.left)
                if i+1<n:
                    node.right = TreeNode(values[i+1]) if values[i+1] else None
                    q.append(node.right)
                    i += 1
                i += 1
        return self.root

    def IsBalanceTree(self,node):
        if not node:
            return 0
        left = self.IsBalanceTree(node.left)
        if left == -1 :
            return -1
        right = self.IsBalanceTree(node.right)
        if right == -1:
            return -1

        return -1 if abs(right - left)>1 else (1 + max(left,right))


if __name__ == "__main__":
    T = Tree()
    root = T.construct_tree([1,2,None,3,4,None,None,5,])
    print(False if T.IsBalanceTree(root)==-1 else True)