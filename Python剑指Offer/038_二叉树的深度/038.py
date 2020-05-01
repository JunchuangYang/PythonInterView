from collections import deque

__author__ = 'lenovo'

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

if __name__ == "__main__":
    t = Tree()
    root = t.construct_tree([1,2,3,4,5,6,])
    print(Tree.solution1(root),Tree.solution2(root))