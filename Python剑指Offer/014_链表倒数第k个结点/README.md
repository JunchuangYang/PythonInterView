### 题目描述

输入一个链表，输出该链表中倒数第k个结点。

### 思路

用快慢指针，快指针比慢指针快k步，到尾结点了慢指针就是倒数第k个结点。

```python
__author__ = 'lenovo'

# 定义结点
class LinkNode(object):
    def __init__(self,value):
        self.val = value
        self.next = None

# 定义链表
class Link(object):
    def __init__(self,values):
        self.node = self.set_link(values)

    # 返回链表头结点
    def get_link(self):
        return self.node
    # 设置链表
    def set_link(self,values):
        head = LinkNode(0)
        move = head
        try:
            for val in values:
                node = LinkNode(val)
                move.next = node
                move = node
        except Exception as  e:
            print(e)
        return head.next

# 求列表倒数第k个结点
def last_kth(node,k):
    # 判断链表是否为空或k=0两种特殊情况
    if node is None or k==0:
        return None
    #设置快慢指针，快指针比慢指针快k步
    fast_p = slow_p = node
    while k:
        fast_p = fast_p.next
        k -= 1
    while fast_p:
        fast_p = fast_p.next
        slow_p = slow_p.next
    return slow_p.val
if __name__ == '__main__':
    node = Link((1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 22))
    link = node.get_link()
    print(last_kth(link,2)) #20
    print(last_kth(link,4)) #8
    print(last_kth(link,6)) #6
    print(last_kth(link,8)) #4
```

