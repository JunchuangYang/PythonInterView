### 题目描述

输入两个链表，找出它们的第一个公共结点。

### 思路

倒序看，p1和p2两个链表的第一个公共结点到尾结点的长度一定相同。因此我们先对齐两个链表，再一起往后走找到第一个公共结点即可。

- 找出两个链表长度，n1和n2，长的链表先走n1-n2步。
- 一起往后走，找到第一个公共结点。

```python
def get_first_common_node(link1, link2):
    if not link1 or not link2:
        return None
    length1 = length2 = 0
    move1, move2 = link1, link2
    while move1:  # 获取链表长度
        length1 += 1
        move1 = move1.next
    while move2:
        length2 += 1
        move2 = move2.next
    while length1 > length2:  # 长链表先走多的长度
        length1 -= 1
        link1 = link1.next
    while length2 > length1:
        length2 -= 1
        link2 = link2.next
    while link1:  # 链表一起走
        if link1 == link2:
            return link1
        link1, link2 = link1.next, link2.next
    return None
```

