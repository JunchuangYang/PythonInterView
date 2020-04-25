import copy

__author__ = 'lenovo'
"""

"""

from collections import deque

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    # 根据二叉树层次遍历创建二叉树
    def construct_tree(self,values=None):
        if not values:
            return None

        self.root = TreeNode(values[0])
        queue = deque([self.root])
        length = len(values)
        nums = 1
        while nums<length:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < length:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    def find(self,node,target_sum,current_sum,path):
        ret = []

        def find_path(node,target_sum,current_sum,path):

            current_sum += node.val
            path.append(node.val)

            if current_sum == target_sum and node.left is None and node.right is None:
                ret.append(copy.copy(path))

            if node.left:
                find_path(node.left,target_sum,current_sum,path)

            if node.right:
                find_path(node.right,target_sum,current_sum,path)
            path.pop()
        find_path(node,target_sum,current_sum,path)
        return ret
if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 1,2,1,1,2,2,2,2])
    path = []

    print(t.find(t.root, 5, 0,path))