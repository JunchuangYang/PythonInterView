### 题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。 输出描述: 对应每个测试案例，输出两个数，小的先输出。

### 思路

左右指针，和大于target，右指针左移，和小于target，左指针右移。

```python
"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加
"""
def solution(alist,target):
    left = 0
    right = len(alist) - 1
    while left < right:
        sum = alist[left] + alist[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else :
            return alist[left],alist[right]

if __name__ == '__main__':
    test = [-4, 0, 1, 2, 4, 6, 8, 10, 12, 15, 18]
    s = 12
    print (solution(test, s))
```

