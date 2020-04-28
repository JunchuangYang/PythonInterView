## 题目

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

## 输入输出示例

- {3，32，321} ----> 321323
- {3，333332，3334} ----> 33333233334

## 思路

显而易见，要重新定义两个数的大小，排好序之后按顺序将字符串拼接起来即可。

如何定义两个数的大小，不太容易立刻想到。其实很简单，为了方便，先将所有的数字转换成字符串，想要比较字符串`a`和字符串`b`的大小，就是比较拼接之后的字符串`ab`和字符串`ba`的大小。如果`ab < ba`，则`a<b`。



```python
import functools
def cmp(a , b):
    "自定义排序规则"
    sa = str(a)
    sb = str(b)
    if sa+sb > sb+sa:
        return 1
    elif sa+sb == sb+sa:
        return 0
    else:
        return -1

def solution(nums):
    return ''.join([str(item) for item in sorted(nums,key = functools.cmp_to_key(cmp))])

if __name__ == "__main__":
    print(solution([3,32,321]))
```

```
"""
一般的 sorted 排序函数 都有相应的 cmp函数，用来定制化排序的比较方法。
然而 python 3中的 sorted( ) 除去的cmp 参数，推荐使用 key。
Python中有相应的函数 支持将 cmp函数转化为key的值。
cmp指定一个定制的比较函数，这个函数接收两个参数（iterable的元素），
如果第一个参数小于第二个参数，返回一个负数；
如果第一个参数等于第二个参数，返回零；
如果第一个参数大于第二个参数，返回一个正数。默认值为None
"""
```

