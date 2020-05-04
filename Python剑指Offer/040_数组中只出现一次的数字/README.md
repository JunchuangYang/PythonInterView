### 题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

### 思路

直接将里面的每个数字映射到字典里，然后作为索引，出现次数作为值，最后取出值为一的索引值。

异或版本不太会.

```python
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        map = {}
        res = []
        for n in array:
            map[n] = map.get(n, 0) + 1
        for n in array:
            if map[n] == 1:
                res.append(n)
        return res

```

