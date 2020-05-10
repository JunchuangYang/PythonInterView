__author__ = 'lenovo'

class LinkNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Soultion(object):
    def __init__(self):
        self.root=None

    def construct_link(self,vals):
        if not vals:
            return None

        self.root = LinkNode(vals[0])
        node = self.root
        for item in vals[1:]:
            temp = LinkNode(item)
            node.next = temp
            node = temp

        return self.root, node

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

if __name__ == "__main__":
    s=Soultion()
    root, end = s.construct_link([1,2,3,4,5,6,7,8,9,0])

    # 设置入环点
    import  random
    a=random.randint(1,9)
    temp = root
    for _ in range(a-1):
        temp=temp.next

    end.next = temp
    print(s.check_ring(root))
    print(a)