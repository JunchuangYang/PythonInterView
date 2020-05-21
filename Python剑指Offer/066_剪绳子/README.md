## 题目描述

给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

## 输入描述:

```
输入一个数n，意义见题面。（2 <= n <= 60）
```

## 输出描述:

```
输出答案。
```

示例1

## 输入

复制

```
8
```

## 输出

复制

```
18
```

找规律：

```python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-



"""
2 1
3 2  1,2
4 4  2,2
5 6  2,3
6 9  3,3
7 12   3,2,2
8 18     2,3,3
9 27     3,3,3
10  36 3,3,2,2
11  54   3,3,3,2
"""
class Solution:
    def cutRope(self, number):
        if number==2:
            return 1
        elif number==3:
            return 2
        elif number==4:
            return 4
        else:
            if number%3==1:
                a = number//3-1
                b = (number-3*a)//2
                return pow(3,a)*pow(2,b)
            else:
                a = number//3
                b = (number-3*a)//2
                return pow(3,a)*pow(2,b)
if __name__ =="__main__":
    s = Solution()
    for i in range(2,61):
        print(s.cutRope(i))
```

