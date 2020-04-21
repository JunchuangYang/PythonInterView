### 题目描述

操作给定的二叉树，将其变换为源二叉树的镜像。 输入描述:

```
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
```

### 思路

左右交换

```python
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


"""二叉树的镜像:递归，改变原来的树结构"""
def mirror(node):
    if node is None:
        return

    temp = node.left
    node.left = node.right
    node.right = temp
    mirror(node.left)
    mirror(node.right)

```

