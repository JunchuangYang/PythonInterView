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
    n=1
    m=1
    print(solution(link.construct_tree(n),n,m)) #44