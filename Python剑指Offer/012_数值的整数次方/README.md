### 题目描述

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

### 思路

指数幂的所有边界包括:

- 指数为0的情况，不管底数是多少都应该是1
- 指数为负数的情况，求出的应该是其倒数幂的倒数
- 指数为负数的情况下，底数不能为0

如果输入的指数exponent=32，我们则需要在函数中循环做31次乘法。

但我们换一种思路考虑：我们的目标是求出一个数字的32次方，如果们知道了它的16次方，那么只要在16次方的基础上再平方一次就可以了。而16次方是8次方的平方。这样以此类推，我们求32次方只需要做5次乘法：先求平方，在平方的基础上求4次方，在4次方的基础上求8次方，在8次方的基础上求16次方，最后在16次方的基础上求32次方。

a^n = a^(n/2) * a^(n/2)  n为偶数

a^n = a^(n-1)/2 * a^(n-1)/2 n为奇数

```python
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
```

