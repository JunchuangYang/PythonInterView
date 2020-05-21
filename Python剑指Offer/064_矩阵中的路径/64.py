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
        print(m)
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