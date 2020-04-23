### 题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

### 思路

用辅助栈存储当前data的最小值，辅助栈头即为min值。

```python
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
```

