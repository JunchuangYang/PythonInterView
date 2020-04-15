#__author__ = 'lenovo'

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # 模拟队列的压入操作
    def push(self,val):
        self.stack1.append(val)

    # 模拟队列的弹出操作
    def pop(self):
        # 当stack2全部弹出时，然后将stack1的值再全部压入
        if self.stack2 :
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else "队列已空！"

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.pop())
    q.push(3)
    print(q.pop())
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())