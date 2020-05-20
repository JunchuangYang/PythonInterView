## 题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

- 常规解法

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
    def Insert(self, num):
        # write code here
        self.res.append(num)
    def GetMedian(self,n=None):
        # write code here
        self.res.sort()
        length = len(self.res)
        return (self.res[length//2]+self.res[length//2-1])/2.0 if length%2==0 else self.res[length//2]
```

- 在牛客网上看到有人用大顶堆和小顶堆，顺便复习一下堆的写法

  https://www.nowcoder.com/questionTerminal/9be0172896bd43948f8a32fb954e1be1?f=discussion

  来源：牛客网

  思路： 

     为了保证插入新数据和取中位数的时间效率都高效，这里使用大顶堆+小顶堆的容器，并且满足： 

     1、两个堆中的数据数目差不能超过1，这样可以使中位数只会出现在两个堆的交接处； 

     2、大顶堆的所有数据都小于小顶堆，这样就满足了排序要求。


```python
链接：https://www.nowcoder.com/questionTerminal/9be0172896bd43948f8a32fb954e1be1?f=discussion
来源：牛客网

class Solution:
    def __init__(self):
        self.minNums=[]
        self.maxNums=[]
 	# 大顶堆插入
    def maxHeapInsert(self,num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i - 1) // 2]:
                t = self.maxNums[(i - 1) // 2]
                self.maxNums[(i - 1) // 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) // 2
            else:
                break
    # 大顶堆删除
    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return  t
 	# 小顶堆插入
    def minHeapInsert(self,num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) // 2]:
                t = self.minNums[(i - 1) // 2]
                self.minNums[(i - 1) // 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) // 2
            else:
                break
 	# 小顶堆删除
    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def Insert(self, num):
        if (len(self.minNums)+len(self.maxNums))&1==0:
            if len(self.maxNums)>0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums)>0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)

    def GetMedian(self,n=None):
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen ==0:
            return -1
        if allLen &1==1:
            return self.minNums[0]
        else:
            #return (self.maxNums[0] + self.minNums[0]+0.0)//2
            return self.maxNums[0]
 
t = Solution()
t.Insert(5)
print t.GetMedian()
t.Insert(2)
print t.GetMedian()
t.Insert(3)
print t.GetMedian()
t.Insert(4)
print t.GetMedian()
t.Insert(1)
print t.GetMedian()
t.Insert(6)
print t.GetMedian()
t.Insert(7)
print t.GetMedian()
t.Insert(0)
print t.GetMedian()
t.Insert(8)
print t.GetMedian()
```

