### 题目描述

输入一个链表，反转链表后，输出新链表的表头。

```python
# 反转链表
def link_reverse(node):
    if node is None or node.next is None:
        return  None
    temp_next = node.next#保存当前结点的下一个结点信息
    node.next = None #第一个节点的下一个节点指NOne
    temp = node # 保存当前节点信息
    node = temp_next # 进行下一个结点操作
    while node:
        temp_next = node.next
        node.next = temp
        temp = node
        if temp_next is None:
            break
        node = temp_next
    return node
```

