### 题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

### 思路

递归

```python
# 合并有序链表，递归
def merge_link(node1,node2):
    if not node1:
        return node2
    if not node2:
        return node1

    if node1.val <= node2.val:
        ret = node1
        ret.next = merge_link(node1.next,node2)
    else:
        ret = node2
        ret.next = merge_link(node1,node2.next)
    return ret
```

