__author__ = 'lenovo'

"""
包含min函数的栈
栈的push，pop，min操作的时间复杂度都是O(1)
使用一个辅助栈保存最小值
"""
class MyStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,val):
        self.stack.append(val)
        if self.min_stack:
            if self.min_stack[-1]<val:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            return None

    def min(self):
        return self.min_stack[-1] if self.min_stack[-1] else None

if __name__ == "__main__":
    s = MyStack()
    s.push(2)
    s.push(1)
    s.push(3)
    print(s.stack)
    print (s.min())
    s.pop()
    s.pop()
    print(s.stack)
    print(s.min())


