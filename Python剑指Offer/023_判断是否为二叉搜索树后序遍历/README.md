### 题目描述

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

### 思路

二叉搜索树有：

- 结点值:左<根<右
- 左右子树都是搜索树

后序遍历顺序为：左->右->根

- 最后一个数为根结点，通过根节点值切割左右子树。
- 判断左右子树是否二叉搜索树

```
整数数组中不包含重复值
整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树
```

对于[4,8,6,12,16,14,10]

```
    10
 6     14  
4 8  12   16
```



```python
def postorder_check(order):
    if not order:
        return False
    if len(order) <= 1:
        return True
    root = order[-1]
    # 左子树
    for i in range(len(order)):
        if order[i] > root:
            break
    # 右子树，大于根
    for j in range(i,len(order)-1):
        if order[j] < root:
            return False
    return postorder_check(order[:i]) and postorder_check(order[i:-1])
```

