## 题目描述

地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？



注意深浅拷贝

```python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = 0
    @staticmethod
    def cal(threshold,rows,cols):
        num = 0
        while rows:
            num+=rows%10
            rows//=10
        while cols:
            num+=cols%10
            cols//=10
        return True if threshold >= num else False

    def dfs(self,threshold,i,j,rows,cols):
        if i>=0 and i<rows and j>=0 and j<cols and Solution.cal(threshold,i,j) and self.flag[i][j]==0:
            self.res+=1
            self.flag[i][j]=1
            print(i,j)
            Solution.dfs(self,threshold,i+1,j,rows,cols)
            Solution.dfs(self,threshold,i,j+1,rows,cols)
            Solution.dfs(self,threshold,i-1,j,rows,cols)
            Solution.dfs(self,threshold,i,j-1,rows,cols)

    def movingCount(self, threshold, rows, cols):
        self.flag = []
        for i in range(rows):
            c = []
            for j in range(cols):
                c.append(0)
            self.flag.append(c[:])
        Solution.dfs(self,threshold,0,0,rows,cols)
        return self.res

if __name__=='__main__':
    S = Solution()
    print(S.movingCount(10,1,100))
```

