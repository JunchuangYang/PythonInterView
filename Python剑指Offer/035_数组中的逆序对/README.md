### 题目描述

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007 输入描述: 题目保证输入的数组中没有的相同的数字

数据范围：

```
对于%50的数据,size<=10^4

对于%75的数据,size<=10^5

对于%100的数据,size<=2*10^5
```

示例1 输入 1,2,3,4,5,6,7,0 输出 7

### 思路

暴力法时间复杂度是o(n^2)，超时。

考虑一下，逆序是说a[i]>a[j]，i<j。那么在排序的过程中，会把a[i]和a[j]交换过来，这个交换的过程，每交换一次，就是一个逆序对的“正序”过程。

**排序每个数，归并排序。**

```python
__author__ = 'lenovo'

count = 0

def merge_sort(alist):
    length = len(alist)
    if length == 1:
        return alist
    mid = length // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return sort(left,right)

def sort(left,right):
    left_length = len(left)
    right_length = len(right)
    l , r = 0,0
    res = []
    while l<left_length and r<right_length:
        if  left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            global count
            count += left_length-l
            res.append(right[r])
            r += 1
    res+=left[l:]
    res+=right[r:]
    return res

if __name__ == "__main__":
    alist = [1,2,3,4,5,6,7,0]
    print(merge_sort(alist))
    print(count)
```

