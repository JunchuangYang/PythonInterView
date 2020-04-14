#__author__ = 'lenovo'

from collections import deque

# 定义二叉树结点
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    '''
    二叉树
    '''
    def __init__(self):
        self.root = None

    #前序遍历
    def pre_traversal(self):

        ret = []

        def traversal(root):
            if root:
                ret.append(root.val)
                traversal(root.left)
                traversal(root.right)

        traversal(self.root)
        return  ret

    #中序遍历
    def in_traversal(self):

        ret = []

        def traversal(root):
            if root:
                traversal(root.left)
                ret.append(root.val)
                traversal(root.right)

        traversal(self.root)
        return  ret

    # 后序遍历
    def post_traversal(self):

        ret = []

        def traversal(root):
            if root:
                traversal(root.left)
                traversal(root.right)
                ret.append(root.val)

        traversal(self.root)
        return  ret

    # 二叉树的广度优先搜索
    def bfs(self):
        ret = []

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return ret


def construct_tree(preorder,inorder):
    '''
    根据前序遍历与中序遍历构建二叉树
    '''
    if not preorder or not inorder:
        return None
    # 根节点在中序遍历中的索引
    inorder_index = inorder.index(preorder[0])
    # 根据根节点将中序遍历分作左右两颗子树
    inorder_left = inorder[0:inorder_index]
    inorder_right = inorder[inorder_index+1:]
    # 新建根节点
    root = TreeNode(preorder[0])
    # 根据中序遍历中左右子树中元素的个数查找前序遍历序列
    root.left = construct_tree(preorder[1:len(inorder_left)+1],inorder_left)
    root.right = construct_tree(preorder[-(len(inorder_right)):],inorder_right)
    return root

if __name__ == '__main__':
    root = construct_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    t = Tree()
    t.root = root
    print("二叉树前序遍历",t.pre_traversal())
    print("二叉树中序遍历",t.in_traversal())
    print("二叉树后序遍历",t.post_traversal())
    print("二叉树广度优先搜索",t.bfs())