__author__ = 'lenovo'

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
"""

"""
在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False ，即：

not None == not False == not '' == not 0 == not [] == not {} == not ()
"""

def stack_check(push_order,pop_order):

    stack1 = []
    for item in push_order:

        stack1.append(item)

        while stack1[-1] == pop_order[0]:
            stack1.pop()
            pop_order.pop(0)
            if  not pop_order:
                break

    return  True if not pop_order  else False

if __name__ == "__main__":
    push_order = [1,2,3,4,5]
    pop_order = [4,3,5,2,1]
    print(stack_check(push_order,pop_order))