### 题目描述

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。 n<=39

### 思路

f(n)=f(n-1)+f(n-2)

```python
'''
实现斐波那契数列
'''

# 1.迭代循环
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return [0,1]
    f = [0,1]
    for i in range(2,n):
        f.append(f[i-2]+f[i-1])
    return f

# 2.递归
def fib2(n):
    def dfs(i):
        if i<=1:
            return i
        return dfs(i-1) + dfs(i-2)
    f = []

    for i in range(n):
        f.append(dfs(i))
    return f

# 3.迭代循环
def fib3(n):
    def fib(i):
        a , b = 0 , 1
        for _ in range(i):
            a , b = b , a+b
        return a

    f = []

    for i in range(n):
        f.append(fib(i))
    return f

# 4. 迭代器方式
class fib4(object):
    def __init__(self, length):
        self.a = 0
        self.b = 1
        self.length = length
        self.index = 0

    def __iter__(self):
        '''返回自身'''
        return self

    def __next__(self):
        # 返回的值
        self.num = self.a
        while True:
            if self.index == self.length:
                raise StopIteration
            self.a , self.b= self.b , self.a+self.b
            self.index += 1
            return self.num


# 5. yield方式
def fib5(n):
    def fib(i):
        a , b = 0 , 1
        for _ in range(i):
            yield a
            a , b = b , a+b

    f = []
    for i in fib(n):
        f.append(i)

    return f
```

