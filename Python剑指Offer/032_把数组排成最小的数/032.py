__author__ = 'lenovo'

"""
一般的 sorted 排序函数 都有相应的 cmp函数，用来定制化排序的比较方法。
然而 python 3中的 sorted( ) 除去的cmp 参数，推荐使用 key。
Python中有相应的函数 支持将 cmp函数转化为key的值。
cmp指定一个定制的比较函数，这个函数接收两个参数（iterable的元素），
如果第一个参数小于第二个参数，返回一个负数；
如果第一个参数等于第二个参数，返回零；
如果第一个参数大于第二个参数，返回一个正数。默认值为None
"""
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