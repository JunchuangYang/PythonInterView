### 题目描述

**在一个长度为n的数组里的所有数字都在0到n-1的范围内。** 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

### 思路

<https://blog.csdn.net/weixin_43508555/article/details/105175469?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2>

**a[index] = index，使数组中下标对应的数字为该下标。**

```python
__author__ = 'lenovo'
"""
长度为10的数组,0~9的数字无序且可重复,找出重复的数字,要求:时间复杂度O(n),空间复杂度O(1);
其实就是位图的思想
"""

def solution(alist):

    length = len(alist)
    i = 0
    while i<length:
        index = alist[i]
        # 如果当前数字与下标相同，或当前数字被标记为-1（说明该数字重复且已经输出）
        # 程序继续
        #print(alist)
        if index == i or index == -1:
            i += 1
            continue
        elif index != alist[index] and alist[index] != -1:
            # 将下标对象的数字修改为与下标相同
            alist[i] , alist[index] = alist[index] , alist[i]
            i-=1
        elif index == alist[index]:
            print(index,' ',end="") # 重复数字
            alist[index] = -1 # 标记为-1，防止重复输出重复数字

        i += 1
if __name__ == "__main__":
    solution([0,1,1,1,2,4,4,6,6,6])
```