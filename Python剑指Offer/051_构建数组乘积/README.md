## 题目

给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法

## 思路

画图，详见<https://www.cnblogs.com/yongh/p/9971936.html>

```python
__author__ = 'lenovo'

def solution(A):
    length = len(A)
    B = [1] * length
    for i in range(2,length):
        B[i] = B[i-1] * A[i-1]

    temp = 1
    for i in range(length-2,0,-1):
        temp *= A[i+1]
        B[i] *= temp
    return B

```



