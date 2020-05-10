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