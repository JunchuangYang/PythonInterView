### 题目描述

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:

> 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

### 思路

设置flag标记，flag[i]==0为未使用，加入s排列字符串。等一次dfs之后在把标记改回来

```python
__author__ = 'lenovo'
#全排列库函数
from itertools import permutations


class Solution(object):

    @staticmethod
    def my_permutation(str):
        ret = []
        length = len(str)
        flag = [0]*length
        def dfs(s):
            if len(s) == length:
                ret.append(''.join(s[:]))
                return None

            for i in range(length):
                if flag[i] == 0:
                    s.append(str[i])
                    flag[i] = 1
                    dfs(s)
                    flag[i] = 0
                    s.pop()
        dfs([])
        return ret
if __name__ == '__main__':
    s = 'aabc'
    print (Solution.my_permutation(s))
    print ([''.join(p) for p in permutations(s)])
```



另一种方法：

```python
def helper(s):
    if len(s) == 1:
        return s[0]
    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])
        for j in l:
            res.append(s[i] + j)

    return res

def Permutation(ss):
    # write code here
    if not ss: return []
    words = list(ss)
    return list(sorted(set(helper(words))))

print(Permutation('aa'))
```

