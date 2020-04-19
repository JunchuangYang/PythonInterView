__author__ = 'lenovo'
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

# 反转链表
def link_reverse(node):
    if node is None or node.next is None:
        return  None
    temp_next = node.next
    node.next = None
    temp = node
    node = temp_next
    while node:
        temp_next = node.next
        node.next = temp
        temp = node
        if temp_next is None:
            break
        node = temp_next
    return node

if __name__ == '__main__':
    node = Link((1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 22))
    link = node.get_link()
    rev = link_reverse(link)
    while rev:
        print(rev.val)
        rev = rev.next