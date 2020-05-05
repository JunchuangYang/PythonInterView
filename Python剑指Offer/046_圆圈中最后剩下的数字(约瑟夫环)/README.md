## 题目

题目：有`n`个人,围成一个环，编号为 0、1、2、3、、、n-1，从第一个人开始循环报数(从`1`开始)，假设数到`m`的那个人出列，然后从下一个人继续数数，数到`m`出列，以此循环，最后那个人为胜利者，求胜利者的编号。

这其实就是有名的约瑟夫问题。

## 输入示例

- n=4, m=3 result=0
- n=50, m=20 result=33
- n=100, m=37 result=44

### 思路

使用链表模拟，将链表尾节点连到头结点，构成单链表的循环

```python
__author__ = 'lenovo'

class LinkNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Link(object):
    def __init__(self):
        self.root = None

    def construct_tree(self,n):
        if n < 1:
            return None
        self.root = LinkNode(0)
        node = self.root
        for i in range(1,n):
            temp = LinkNode(i)
            node.next = temp
            node = temp
        node.next = self.root
        return self.root

def solution(node,n,m):
    while n:
        if n == 1:
            return node.val
        # 特别判断m=1时的情形
        if m == 1:
            for _ in range(n-1):
                node = node.next
            return node.val

        for _ in range(m-2):
            node = node.next

        temp = node.next.next
        node.next = temp
        node = temp
        n -= 1

if __name__ == "__main__":
    link = Link()
    n=50
    m=20
    print(solution(link.construct_tree(n),n,m)) #33
    n=4
    m=3
    print(solution(link.construct_tree(n),n,m)) #0
    n=100
    m=37
    print(solution(link.construct_tree(n),n,m)) #44
```

