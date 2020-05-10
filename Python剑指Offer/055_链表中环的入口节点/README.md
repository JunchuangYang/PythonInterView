### 题目描述

​	给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

### 思路

<https://www.cnblogs.com/fankongkong/p/7007869.html>

```python
    def check_ring(self,node):
        slow = node
        fast = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 快慢指针相等，快指针从头开始，直到两个指针再次相遇则为入环点
            if slow == fast:
                fast = node
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return fast.val

        return None
```

