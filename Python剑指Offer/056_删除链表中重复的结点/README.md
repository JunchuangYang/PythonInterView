



### 题目描述

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5



- 注意全部重复的情况

```python
    def check_duplicate(self,root):
        # 设置头结点，防止根节点有重复
        head = LinkNode(root.val-1)
        head.next = root
        # 当前节点的前节点
        pre = head
        node = root
        while node:
            if node.next and node.val == node.next.val:
                temp = node.next
                while temp and node.val == temp.val:
                    temp = temp.next

                pre.next = temp
                node = temp
                continue
            pre = node
            node = node.next
        return head.next.val if head.next else None
```

