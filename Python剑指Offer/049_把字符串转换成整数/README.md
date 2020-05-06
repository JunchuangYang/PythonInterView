### 题目描述

将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

输入描述: 输入一个字符串,包括数字字母符号,可以为空

输出描述: 如果是合法的数值表达则返回该数字，否则返回0

```python
__author__ = 'lenovo'
def solution(alist):
    if not alist:
        return 0
    str = list(filter(lambda x:x.isdigit(),alist))
    res = int("".join(str))
    if len(str) == len(alist):
        return res
    elif len(str) + 1 == len(alist):
        if alist[0] == '-':
            return res*(-1)
        elif alist[0] == '+':
            return res
        else:
            return 0
    return 0
if __name__ == "__main__":
    print(solution("1234"))
    print(solution("-1234"))
    print(solution("+1234"))
    print(solution("0001234"))
```



```python
class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0
        flag = 1
        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                continue
            elif i == 0 and s[i] == '-':
                flag = -1
                continue
            n = ord(s[i]) - ord('0')
            if n>=0 and n<=9:
                res = 10 * res + n
            else:
                return False
        return res * flag

print(Solution().StrToInt('-1234'))
```

