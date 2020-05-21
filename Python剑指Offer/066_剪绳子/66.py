# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-



"""
2 1
3 2  1,2
4 4  2,2
5 6  2,3
6 9  3,3
7 12   3,2,2
8 18     2,3,3
9 27     3,3,3
10  36 3,3,2,2
11  54   3,3,3,2
"""
class Solution:
    def cutRope(self, number):
        if number==2:
            return 1
        elif number==3:
            return 2
        elif number==4:
            return 4
        else:
            if number%3==1:
                a = number//3-1
                b = (number-3*a)//2
                return pow(3,a)*pow(2,b)
            else:
                a = number//3
                b = (number-3*a)//2
                return pow(3,a)*pow(2,b)
if __name__ =="__main__":
    s = Solution()
    for i in range(2,61):
        print(s.cutRope(i))