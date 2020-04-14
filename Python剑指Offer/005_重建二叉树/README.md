### 题目描述

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中**都不含重复的数字**。例如，输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

### 思路

- 用前序遍历找到根结点
- 用根结点在中序遍历中切开左右子树，递归重建二叉树

```python
# 定义二叉树结点
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


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
```

