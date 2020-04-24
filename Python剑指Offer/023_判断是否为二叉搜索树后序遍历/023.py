__author__ = 'lenovo'
"""
判断给定的整数数组是不是二叉搜索树的后序遍历序列:
整数数组中不包含重复值
整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树
"""

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

if __name__ == "__main__":
    print(postorder_check([4,8,6,12,16,14,10]))
    print(postorder_check([9,6,7]))
