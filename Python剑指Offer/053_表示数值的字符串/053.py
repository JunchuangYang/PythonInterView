__author__ = 'lenovo'

class Solution(object):
    def isNumber(self,str):
        # 三个标记，分别表示是否出现过+-号，小数点，和E
        sign, point, hasE = False,False,False
        for i in range(len(str)):
            # 判断出现e的非法情况
            if str[i].lower() == 'e':
                # 只能出现一次e
                if hasE:
                    return False
                # e不能在最后一位
                if i == len(str)-1:
                    return False
                hasE = True
            elif str[i] == '+' or str[i] == '-':
                # 出现第二个正负号，且正负号前不为e
                if sign and str[i-1].lower() != 'e':
                    return False
                # 如果正负号在中间且正负号前不为e
                if not sign and i>0 and str[i-1].lower()!='e':
                    return False
                sign = True
            elif str[i] == '.':
                # 只能出现一次小数点，且E后不能有小数点
                if hasE or point:
                    return False
                point = True
            # 判断字符的非法情况
            elif ord(str[i]) < ord('0') or ord(str[i])>ord('9'):
                return False

        return True
