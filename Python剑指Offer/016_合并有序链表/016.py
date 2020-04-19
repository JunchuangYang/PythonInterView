__author__ = 'lenovo'
"""
合并有序链表，满足单调不递减规则
"""
# 定义结点
class LinkNode(object):
    def __init__(self,value):
        self.val = value
        self.next = None

# 定义链表
class Link(object):
    def __init__(self,values):
        self.node = self.__set_link(values)

    # 返回链表头结点
    def get_link(self):
        return self.node
    # 设置链表
    def __set_link(self,values):
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

    @staticmethod
    def print_link(link=None):
        count = 1
        while link:
            if count == 1:
                print (link.val)
            elif count % 5 == 0:
                print ('->', link.val)
            else:
                print ('->', link.val)
            count += 1
            link = link.next

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

if __name__ == '__main__':
    node1 = Link((2, 4, 6, 8, 20, 22))
    link1 = node1.get_link()
    node2 = Link((1,3,5,7,8))
    link2 = node2.get_link()
    Link.print_link(merge_link(link1,link2))