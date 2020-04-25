### 题目描述

输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到**叶结点**所经过的结点形成一条路径。

### 思路

DFS：

- 每次访问一个节点，那么就将当前权值求和
- 如果当前权值和与期待的和一致，那么说明我们找到了一个路径，保存或者输出
- 每次深度遍历到底部，回退一个点

```python
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
```

