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