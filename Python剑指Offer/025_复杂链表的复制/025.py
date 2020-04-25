import random

__author__ = 'lenovo'
"""
复杂链表的复制
链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
分为三步完成：
一复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
二为每个新结点设置random_node指针:
    循环链表，每一个原始结点的rando_node指针的下一个结点就是复制结点的random_node所指向的结点
三把复制后的结点链表拆开
"""

class LinkNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random_node = None


class Link(object):

    @staticmethod
    def construct_nodes(values):
        """构造一个简单的复杂链表"""
        if not values:
            return None

        root = LinkNode(values[0])
        node = root
        # 所有的链表结点
        nodes = [None,node]
        for i in range(1,len(values)):
            temp = LinkNode(values[i])
            nodes.append(temp)
            node.next = temp
            node = temp

        node = root
        while node:
            # 从链表结点中随机选取一个
            node.random_node = random.choice(nodes)
            node = node.next

        return root

    @staticmethod
    def clone_node(node):
        """复制链表"""
        root = node
        while node:
            temp = LinkNode(node.val)
            temp.next = node.next
            node.next = temp
            node = temp.next
        return root

    @staticmethod
    def set_node(node):
        """设置随机结点"""
        root = node

        while node:
            temp = node.next
            temp_random = node.random_node
            if temp_random:
                temp.random_node = temp_random.next
            node = temp.next
        return root

    @staticmethod
    def reconstruct_node(node):
        """拆分链表，得到复制链表"""
        root = node.next if node else None
        node2 = root

        while node2:
            temp = node2.next
            if temp:
                node2.next = temp.next
                node2 = temp.next
            else:
                break
        return root

    @staticmethod
    def print_node(node):
        # 打印结点值，结点other的值，用来比较
        ret = []
        while node:
            temp = [node.val]
            if node.random_node:
                temp.append(node.random_node.val)
            ret.append(temp)
            node = node.next
        print (ret)

if __name__ == "__main__":
    node = Link.construct_nodes([1, 2, 3, 4, 5])
    Link.print_node(node)
    # 复制链表
    clone_node = Link.clone_node(node)
    # 设置随机结点
    clone_nodes = Link.set_node(clone_node)
    # 拆分链表
    clone_nodess = Link.reconstruct_node(clone_nodes)
    # 打印列表
    Link.print_node(clone_nodess)