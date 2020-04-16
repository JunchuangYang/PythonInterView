#__author__ = 'lenovo'

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

if __name__ == '__main__':
    print(fib1(10))
    print(fib2(10))
    print(fib3(10))
    fib = fib4(10)
    print([i for i in fib])
    print(fib5(10))