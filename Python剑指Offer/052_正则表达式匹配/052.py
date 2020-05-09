__author__ = 'lenovo'

"""Runtime: 1612 ms"""
def solution(s,p):
    s_length = len(s)
    p_length = len(p)
    if s_length == 0 and p_length == 0:
        return True
    if s_length != 0 and p_length == 0:
        return False

    if p_length > 1 and p[1] == '*':
        if s_length > 0  and (p[0] == s[0] or p[0] == '.'):
            return solution(s[:],p[2:]) or solution(s[1:],p[:])
        else:
            return solution(s[:],p[2:])


    if s_length > 0 and (s[0] == p[0] or p[0] == '.'):
        return solution(s[1:],p[1:])
    return False
if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    print(solution(s,p))

