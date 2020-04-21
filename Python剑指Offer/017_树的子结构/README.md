### 题目描述

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）



```python
# 判断二叉树Tree2是否是Tree1的子树
def sub_tree(Tree1,Tree2):
    if Tree1 and Tree2 :

        if Tree1.val == Tree2.val:
            return sub_tree(Tree1.left,Tree2.left) and sub_tree(Tree1.right, Tree2.right)

        else:
            return sub_tree(Tree1.left,Tree2) or sub_tree(Tree1.right,Tree2)

    if Tree1 is None and Tree2:
        return False

    return True
```

