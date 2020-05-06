from functools import reduce

__author__ = 'lenovo'
def solution(alist):
    if not alist:
        return 0
    str = list(filter(lambda x:x.isdigit(),alist))
    print(str)
    res = reduce(lambda x,y:x*10+y,str)
    if len(str) == len(alist):
        return res
    elif len(str) + 1 == len(alist):
        if alist[0] == '-':
            return res*(-1)
        elif alist[0] == '+':
            return res
        else:
            return 0
    return 0
if __name__ == "__main__":
    print(solution("1234"))
    print(solution("-1234"))
    print(solution("+1234"))
    print(solution("0001234"))