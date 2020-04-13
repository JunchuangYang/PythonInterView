### 题目描述

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

### 思路

先遍历找到多少个空格，然后开辟数组填充

一、使用Python中的replace函数，并加上装饰器计算时间差。

```python
#__author__ = 'lenovo'
import datetime

def timeti(func):

    def jishi(str):
        start = datetime.datetime.now()
        func(str)
        end = datetime.datetime.now()
        print("run: ", end - start)

    return jishi

@timeti
def rep1(str):
    str =  str.replace(' ','%20')
    print(str)

print(rep1("We Are Happy"))
# output
We%20Are%20Happy
run:  0:00:00
None
```

二、使用正则表达式

```python

import re
ret = re.compile(' ')
ret.sub('20%', "We Are Happy")
```



三、先遍历找到多少个空格，然后开辟数组填充（剑指offer上的方法）

```python
def rep2(str):
    num = 0
    for s in str:
        if s == ' ':
           num += 1
    new_str = [' ']*(len(str)+2*num)

    j = 0
    for i in range(len(str)):
        if str[i] == ' ':
            new_str[j] = '%'
            new_str[j+1] = '2'
            new_str[j+2] = '0'
            j += 3
        else:
            new_str[j] = str[i]
            j += 1
    print(''.join(new_str))

print(rep2("We Are Happy"))
```



