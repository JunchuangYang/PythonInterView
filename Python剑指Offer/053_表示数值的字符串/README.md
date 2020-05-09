### 题目描述

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

### 思路

判断一个字符串是否为数字分为4种情况：

- 0-9出现的数字
- e或者E（指数），不能出现在末尾；e（E）后面如果有正负号，则不能有小数点
- 表示正负，不能在末尾出现，正负号如果在中间，那么前一个是e或者E,后一个是0—9的数字 比如 -1e-16
- 小数点只能有一个 比如 1.2.3

```python
__author__ = 'lenovo'

class Solution(object):
    def isNumber(self,str):
        # 三个标记，分别表示是否出现过+-号，小数点，和E
        sign, point, hasE = False,False,False
        for i in range(len(str)):
            # 判断出现e的非法情况
            if str[i].lower() == 'e':
                # 只能出现一次e
                if hasE:
                    return False
                # e不能在最后一位
                if i == len(str)-1:
                    return False
                hasE = True
            elif str[i] == '+' or str[i] == '-':
                # 出现第二个正负号，且正负号前不为e
                if sign and str[i-1].lower() != 'e':
                    return False
                # 如果正负号在中间且正负号前不为e
                if not sign and i>0 and str[i-1].lower()!='e':
                    return False
                sign = True
            elif str[i] == '.':
                # 只能出现一次小数点，且E后不能有小数点
                if hasE or point:
                    return False
                point = True
            # 判断字符的非法情况
            elif ord(str[i]) < ord('0') or ord(str[i])>ord('9'):
                return False
            
        return True

```

