### 题目描述

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

### 思路

　　**思路一：数字次数超过一半，则说明：排序之后数组中间的数字一定就是所求的数字。**

　　利用partition()函数获得某一随机数字，其余数字按大小排在该数字的左右。若该数字下标刚好为n/2，则该数字即为所求数字；若小于n/2，则在右边部分继续查找；反之，左边部分查找。

　　**思路二：数字次数超过一半，则说明：该数字出现的次数比其他数字之和还多**

　　遍历数组过程中保存两个值：一个是数组中某一数字，另一个是次数。遍历到下一个数字时，若与保存数字相同，则次数加1，反之减1。若次数=0，则保存下一个数字，次数重新设置为1。由于要找的数字出现的次数比其他数字之和还多，那么要找的数字肯定是最后一次把次数设置为1的数字。

　　也可以这样理解：

```
　采用阵地攻守的思想：
　　第一个数字作为第一个士兵，守阵地；count = 1；
　　遇到相同元素，count++;
　　遇到不相同元素，即为敌人，同归于尽,count--；当遇到count为0的情况，又以新的i值作为守阵地的士兵，继续下去，到最后还留在阵地上的士兵，**有可能是**主元素。
　　再加一次循环，记录这个士兵的个数看是否大于数组一般即可。
```

**两种方法的时间复杂度均为O(n)。**

<https://www.cnblogs.com/yongh/p/9938889.html>

```python
__author__ = 'lenovo'

class Solution(object):
    @staticmethod
    def check_num(nums,str):
        n = 0
        for i in str:
            if i == nums:
                n+=1
        if n*2 <= len(str):
            return 0
        return nums


    @staticmethod
    def solution1(str):
        def partition(str,start,end):
            pivot = str[start]

            while start<end:
                while start<end and pivot<=str[end]:
                    end -= 1
                str[start] = str[end]

                while start<end and str[start]<=pivot:
                    start += 1
                str[end] = str[start]
            str[start] = pivot
            return start

        def helper(str,start,end):
            length = len(str)
            index = partition(str,start,end)
            if index == (length>>1):
                return str[index]
            elif index<(length>>1):
                return helper(str,index+1,end)
            else:
                return helper(str,start,index-1)
        # 获取到中位数
        num = helper(str,0,len(str)-1)
        # 判断中位数是否超过数组长度一半
        print(Solution.check_num(num,str))

    @staticmethod
    def solution2(str):
        res = None
        sum = 0
        for i in str:
            if sum == 0:
                res = i
                sum += 1
            elif res == i:
                sum += 1
            else:
                sum -= 1

        print(Solution.check_num(res,str))
if __name__ == "__main__":
    Solution.solution1([1, 2, 3,3,3,3])
    Solution.solution2([1, 2, 3,3,3,3])
```

