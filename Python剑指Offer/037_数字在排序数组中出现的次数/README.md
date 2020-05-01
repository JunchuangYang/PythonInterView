### 题目描述

统计一个数字在排序数组中出现的次数。例如输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4。

### 思路

整体用二分法，找到头和尾。

**因为data中都是整数，所以可以稍微变一下，不是搜索k的两个位置，而是搜索k-0.5和k+0.5**

这两个数应该插入的位置，然后相减即可。

```python
__author__ = 'lenovo'
def biSearch(alist,k):
    right = len(alist) - 1
    left= 0
    while left <= right:
        mid = (right+left)//2
        if alist[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return right

def GetNumberOfK(alist, k):
    if not alist: return 0
    return biSearch(alist, k+0.5) - biSearch(alist, k-0.5)

if __name__ == "__main__":
    print(GetNumberOfK([1,2,3,3,5,5,5,7],5))
```

暴力解法的时间复杂度为O(n)，还有更优的解法，运用二分查找，时间复杂度为O(logn)：

1.先找出第一次出现的下标值，设left，mid，right分别代表数组的起始，中间，结束的下标。

若数组中间的数a[mid]大于k，则right = mid -1;

若数组中间的数a[mid]小于k，则left = mid+1;

若数组中间的数a[mid]等于k，判断a[mid-1] 是否等于k，若不等于，说明是第一次出现的下标，返回mid下标；若等于，则说明第一次出现的下标还在mid的左边，right = mid -1;

递归重复以上过程。

2.再找出最后出现的下标，原理同上。

***练习手写二分***

```python
__author__ = 'lenovo'
def get_first_k(alist,k):
    right = len(alist) - 1
    left= 0
    while left <= right:
        mid = (right+left)//2
        if alist[mid] < k:
            left = mid + 1
        elif alist[mid] > k:
            right = mid - 1
        else:
            if mid == 0 or alist[mid-1] != k:
                return mid
            right = mid - 1
    return -1

def get_last_k(alist,k):
    right = len(alist) - 1
    left = 0
    while left <= right:
        mid = (left+right) // 2
        if alist[mid] < k:
            left = mid + 1
        elif alist[mid] > k:
            right = mid - 1
        else:
            if mid == len(alist)-1 or alist[mid+1] != k:
                return mid
            left = mid + 1
    return -1

def solution(alist,k):
    return get_last_k(alist,k) - get_first_k(alist,k) + 1

if __name__ == "__main__":
    print(solution([1,2,3,3,5,5,5,7],2))
```

