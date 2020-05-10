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

        return self.root

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

if __name__ == "__main__":
    s=Soultion()
    root = s.construct_link([3,3,3,3])
    print(s.check_duplicate(root))
    while root:
        print("{0}->".format(root.val),end="")
        root = root.next