### 题目描述

输入一棵二叉树，判断该二叉树是否是平衡二叉树。

### 思路

思路1：非剪枝

递归查看每棵子树是否满足平衡二叉树，o(nlogn)复杂度。

```python
def getDeep(x):
    if x is None:
        return 0
    return 1 + max(getDeep(x.left), getDeep(x.right))

def IsBalanced_Solution(self, pRoot):
	# write code here
	if not pRoot:
		return 1
	return abs(getDeep(pRoot.left)-getDeep(pRoot.right)) <= 1 \
                and IsBalanced_Solution(pRoot.left) \
                and IsBalanced_Solution(pRoot.right) 
```



思路2：剪枝

看子树是否是平衡二叉树，如果不是返回-1，如果是返回长度。



```python
    def IsBalanceTree(self,node):
        if not node:
            return 0
        left = self.IsBalanceTree(node.left)
        if left == -1 :
            return -1
        right = self.IsBalanceTree(node.right)
        if right == -1:
            return -1

        return -1 if abs(right - left)>1 else (1 + max(left,right))
```

