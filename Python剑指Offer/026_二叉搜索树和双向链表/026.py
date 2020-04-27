__author__ = 'lenovo'

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self):
        self.root = None
    """
    非二叉搜索树，建树的时候values中的顺序需要注意
    之后有时间会改成二叉搜索树
    """
    def construct_tree(self, values=None):
        # 结点值不存在的话，values中用None表示
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1


def convert_link(node,node_pre):
    if not node:
        return None
    if node.left:
        node_pre = convert_link(node.left,node_pre)
    if node_pre:
        node_pre.right = node
    node.left = node_pre
    node_pre = node
    if node.right:
        node_pre = convert_link(node.right,node_pre)
    return node_pre

def convert(node):
    if not node:
        return None
    last = convert_link(node,None)
    while last and last.left:
        last = last.left
    return last

if __name__=="__main__":
    t = Tree()
    t.construct_tree([5, 3, 6, 2, 4, None, 7, 1])
    root = convert(t.root)
    while root:
        print(root.val,"->",end="")
        root=root.right