### 题目描述

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

### 思路

思路1：

- 最小堆建立(需要o(n)时间复杂度)
- 取出前k个数(每次取需要用logn时间重建堆)。时间复杂度为o(n)+o(k*logn)

思路2:

- 用快排partition划分，一直划中第k个数最差情况o(kn)

```python
class Solution(object):
    # 调整堆
    def adjust(self,str,m):
        length = len(str)
        left = 2*m + 1
        right = 2*m + 2

        if left>=length:
            return
        # 寻找左右子节点的最小值
        min_m = left
        if right<length and str[left]>str[right]:
            min_m = right

        # 与父节点相比交换最小值
        if str[m] > str[min_m]:
            str[m] , str[min_m] = str[min_m] , str[m]
            # 递归
            self.adjust(str,min_m)
    # 建堆
    def build_heap(self,str):
        length = len(str)
        #从最后节点的父亲节点开始调整
        for i in range(length//2,-1,-1):
            self.adjust(str,i)

        return str

    # 思路一：最小堆
    def solution1(self,str,k):
        if k > len(str):
            return None
        # 建立最小堆
        heap = self.build_heap(str)
        res = []

        # 取出最小堆的前k个元素
        # 对于最小堆和最大堆而言，删除是针对于根节点而言。
        # 对于删除操作，将二叉树的最后一个节点替换到根节点，然后自向下，递归调整。
        for _ in range(k):
            heap[0] , heap[-1] = heap[-1] , heap[0]
            res.append(heap[-1])
            heap.pop()
            self.adjust(heap,0)

        return res

    # 思路二：快排
    def solution2(self,str,start,end,k):
        pos = self.partition(str,start,end)

        if pos+1 == k:
            return str[:k]
        elif pos+1 > k:
            return self.solution2(str,start,pos-1,k)
        else:
            return self.solution2(str,pos+1,end,k)

    def partition(self,str,start,end):
        pivot = str[start]

        while start<end:
            while start<end and pivot<=str[end]:
                end -= 1
            str[start] = str[end]

            while start<end and str[start] < pivot:
                start += 1

            str[end] = str[start]

        str[start] = pivot
        return start
```

