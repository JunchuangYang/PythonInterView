### 题目描述

请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

### 输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。



- 使用Python3中的字典。说Python中字典序为无序，但默认情况下，Python3中的字典序为“顺序”

```python
__author__ = 'lenovo'

class Solution(object):
    def __init__(self):
        self.charDict = {}

    def FirstApperingOnce(self):
        for key in self.charDict.keys():
            if self.charDict[key] == 1:
                return key
        return '#'

    def Insert(self, char):
        # 虽说Python中字典序为无序，但默认情况下，Python3中的字典序为“顺序”
        self.charDict[char] = self.charDict[char] + 1 if char in self.charDict.keys() else 1

if __name__ == "__main__":
    s = Solution()
    for c in ['g','o','o','g','l','e','a']:
        s.Insert(c)
        print(s.FirstApperingOnce())
```

- filter

```python
class Solution2(object):
    def __init__(self):
        self.charlist = []
    def FirstApperingOnce(self):
        res = list(filter(lambda x:self.charlist.count(x)==1,self.charlist))
        return res[0] if res else "#"
    def Insert(self,char):
        self.charlist.append(char)

if __name__ == "__main__":
    s = Solution2()
    for c in ['g','o','o','g','l','e','a']:
        s.Insert(c)
        print(s.FirstApperingOnce())
```

