#__author__ = 'lenovo'

'''
倒序打印列表
1.reverse_links_1使用栈
2.reverse_links_2递归
'''
class LinkNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Link(object):

    # 使用静态方法生成链表
    @staticmethod
    def link(values):
        # 头指针不存放任何信息
        head = LinkNode(0)
        move = head
        try :
            for value in values:
                temp = LinkNode(value)
                move.next = temp
                move = move.next
        except Exception as e:
            print(e)
        # 返回链表头
        return head.next

def reverse_links_1(links):
    link_stack = []
    link_reverse = []
    while links:
        link_stack.append(links.val)
        links = links.next
    while link_stack:
        link_reverse.append(link_stack.pop())
    print(link_reverse)

link_reverse = []
def reverse_links_2(links):
    if links:
        reverse_links_2(links.next)
        link_reverse.append(links.val)
    return link_reverse
if __name__ == "__main__":
    links = Link.link([1,2,3,4,5,6,7])
    reverse_links_1(links)
    print(reverse_links_2(links))