__author__ = 'lenovo'

"""
求数值的整数次方
需要考虑mi为正数、负数和0
浮点数不能直接用==比较
"""

def equal_zero(base):
    if abs(base - 0.0) < 0.0000001:
        return True
    return False

def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    res = power(base, exponent>>1)
    res *= res
    # 奇数
    if exponent & 1:
        res *= base
    return res

def power(base, exponent):
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError
    res = power_value(base, abs(exponent))
    return res if exponent > 0 else 1.0/res

if __name__ =='__main__':
    #print(power(0,-1))
    print(power(-2,-6))
    print(power(-2,2))
    print(power(-2,0))