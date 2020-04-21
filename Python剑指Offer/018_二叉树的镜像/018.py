__author__ = 'lenovo'

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

        # 判断二叉树Tree2是否是Tree1的子树
    def sub_tree(self,Tree1,Tree2):
        if Tree1 and Tree2 :

            if Tree1.val == Tree2.val:
                return self.sub_tree(Tree1.left,Tree2.left) and self.sub_tree(Tree1.right, Tree2.right)

            else:
                return self.sub_tree(Tree1.left,Tree2) or self.sub_tree(Tree1.right,Tree2)

        if Tree1 is None and Tree2:
            return False

        return True

    """二叉树的镜像:从右到左"""
    def mirror_bfs(root):
        ret = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.right)
                queue.append(node.left)
        return ret

    """二叉树的镜像:递归"""
    def mirror_pre(root):
        ret = []

        def traversal(root):
            if root:
                ret.append(root.val)
                traversal(root.right)
                traversal(root.left)
        traversal(root)
        return ret


"""二叉树的镜像"""
def mirror(node):
    if node is None:
        return

    temp = node.left
    node.left = node.right
    node.right = temp
    mirror(node.left)
    mirror(node.right)


if __name__ == '__main__':
    t1 = Tree()
    t1.construct_tree([1, 2, 3, 4, 5,6,7])
    print (t1.bfs())
    mirror(t1.root)
    print(t1.bfs())
