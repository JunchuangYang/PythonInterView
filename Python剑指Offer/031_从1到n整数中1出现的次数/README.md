### 题目

求出1~13的整数中1出现的次数,并算出1~1300的整数中1出现的次数？

为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现5次,但是对于后面问题他就没辙了。

ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

### 思路

在分析之前，首先需要知道一个规律：

- 从 1 至 10，在它们的个位数中，数字1出现了 1 次。
- 从 1 至 100，在它们的十位数中，数字1出现了 10 次。
- 从 1 至 1000，在它们的百位数中，数字1出现了 100 次。
  依此类推，从 1 至 10i，在它们右数第二位中，数字1出现了10 ^ (i - 1)次。

考虑从个位开始计算1出现的次数，个位上每10个数就会出现一个1，所以计算十位数之后出现1的次数即n模10的余数为a。假如个位数为0，那么a就为个位上1出现的次数；若等于1，那么还应该再加上1，也就是个位数为1所有数字的个数；若大于1，则a应该再加上1，即十位数出现的次数为a+1.同样的思想依次向左考虑十位数、百位数一直到最高位。

总结一下以上的算法，可以看到，当计算右数第 i 位包含的 1 的个数时：

1. 取第 i 位左边（高位）的数字，乘以 10^(i−1)，得到基础值 a。
2. 取第 i 位数字，计算修正值：

- 如果大于 1，则结果为 a+10^(i−1)。
- 如果小于 1，则结果为 a。
- 如果等于 1，则取第 i 位右边（低位）数字，设为 b，最后结果为 a+b+1。

<https://www.cnblogs.com/wmx24/p/8901808.html>

<https://www.cnblogs.com/aimi-cn/p/11510770.html>

```python
__author__ = 'lenovo'

def NumberOf1Between1AndN(num):
    if num < 1:
        return 0

    mult , sums = 1 , 0

    while num // mult:
        # div 高位数字（i+1位） ， curmod 低位(i-1位)数字
        div , mod = divmod(num , mult*10)
        curnum , curmod = divmod(mod , mult)
        if mod == 1:
            sums += div * mult + curmod + 1
        elif mod > 1:
            sums += div * mult + 1
        else:
            sums += div * mult

        mult *= 10
    return sums

if __name__ == '__main__':
    test = 100
    print(NumberOf1Between1AndN(test))
```

