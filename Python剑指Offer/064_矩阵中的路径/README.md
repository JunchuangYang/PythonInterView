## 题目描述

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个

深搜：

```python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import copy
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        m = []
        c = []
        for i in range(1,rows*cols+1):
            if i%cols==0:
                c.append(matrix[i-1])
                m.append(c[:])
                c=[]
            else:
                c.append(matrix[i-1])
        for i in range(rows):
            for j in range(cols):
                if m[i][j] == path[0]:
                    flag = copy.deepcopy(m)
                    print(flag)
                    if Solution.dfs(self,flag,i,j,path):
                        return True

        return False

    def dfs(self,matrix,i,j,path):
        matrix = matrix[:]
        if not path:
            return True
        if i>=0 and i<len(matrix) and j>=0 and j<len(matrix[0]) and matrix[i][j] == path[0]:
            matrix[i][j]="#"
            return Solution.dfs(self,matrix,i+1,j,path[1:]) or Solution.dfs(self,matrix,i,j+1,path[1:]) or \
                   Solution.dfs(self,matrix,i-1,j,path[1:]) or Solution.dfs(self,matrix,i,j-1,path[1:])
        return False
if __name__=='__main__':
    matrix = "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
    path = "SGGFIECVAASABCEHJIGQEM"
    s = Solution()
    print(s.hasPath(matrix,5,8,path))
```

