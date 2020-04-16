__author__ = 'lenovo'

def fib(n):
    if n<=1:
        return n
    a , b = 0 , 1
    for _ in range(n):
        a , b = b , a+b
    return a

def fib2(n):
    if n<=1:
        return n
    return fib2(n-1) + fib2(n-2)
print(fib(10))
print(fib2(10))