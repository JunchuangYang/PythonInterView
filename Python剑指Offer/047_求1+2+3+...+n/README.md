### 题目描述

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。



```python
from functools import reduce

__author__ = 'lenovo'
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case
等关键字及条件判断语句（A?B:C）。
"""
def solution1(n):
    try:
        1 % n # 为什么递归会在1%0退出，但是不走except
        return n+solution1(n-1)
    except:
        return 0

def solution2(n):
    return reduce(lambda x,y:x+y,range(1,n+1))

def solution3(n):
    return sum(range(1,n+1))

if __name__ == "__main__":
    print(solution1(100))
    print(solution2(100))
    print(solution3(100))

```

