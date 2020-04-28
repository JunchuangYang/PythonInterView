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