### 题目

**给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。**

**'.' 匹配任意单个字符**
**'*' 匹配零个或多个前面的那一个元素**
**所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。**

**说明:**

**s 可能为空，且只包含从 a-z 的小写字母。**
**p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。**

```
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```



**还是百度吧，时间复杂度太高，我自己也是写的迷迷糊糊的**，果然不是搞算法的料。

```python
__author__ = 'lenovo'

"""Runtime: 1612 ms"""
def solution(s,p):
    s_length = len(s)
    p_length = len(p)
    if s_length == 0 and p_length == 0:
        return True
    if s_length != 0 and p_length == 0:
        return False

    if p_length > 1 and p[1] == '*':
        if s_length > 0  and (p[0] == s[0] or p[0] == '.'):
            return solution(s[:],p[2:]) or solution(s[1:],p[:])
        else:
            return solution(s[:],p[2:])


    if s_length > 0 and (s[0] == p[0] or p[0] == '.'):
        return solution(s[1:],p[1:])
    return False
if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    print(solution(s,p))


```

单元测试：

这些例子过了差不多算法就能过了。

```python
__author__ = 'lenovo'
import unittest
from Python_Offer import xxxx

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertFalse(xxxx.solution(s = "mississippi",p = "mis*is*p*."))
        self.assertFalse(xxxx.solution(s = "aa",p = "a"))
        self.assertTrue(xxxx.solution(s = "aa",p = "a*"))
        self.assertTrue(xxxx.solution(s = "aab",p = "c*a*b"))
        self.assertTrue(xxxx.solution(s = "ab",p = ".*"))
        self.assertTrue(xxxx.solution(s = "a",p = "ab*"))
        self.assertFalse(xxxx.solution(s = "ab",p = ".*c"))
        self.assertTrue(xxxx.solution(s = "bbbba",p=".*a*a"))
        self.assertTrue(xxxx.solution(s = "aaaaaaaaaaaaab",p="a*a*a*a*a*a*a*a*a*a*c"))

if __name__ == "__main__":
    t = UnitTest()
    t.test()
```



