### 题目描述

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

### 思路

一个栈用来存储 pop时弹出stack2，stack2为空，pop出stack1存储在stack2中

```python
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
```

