### 题目描述

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

```python
def solution(str):
    dic = {}
    for i in range(len(str)):
        dic[str[i]] = dic.get(str[i],0) +1
    for i in range(len(str)):
        if dic[str[i]] == 1:
            return i
    return -1
if __name__=="__main__":
    print(solution("aaaaaaaaaaaaaaab"))
```

