__author__ = 'lenovo'
"""
调整数组顺序使奇数位于偶数前面
使用两个指针，前后各一个，为了更好的扩展性，可以把判断奇偶部分抽取出来
"""
def alist_order(alist):
    head = 0
    tail = len(alist) - 1
    while head<=tail:
        while not is_even(alist[head]):
            head += 1
        while is_even(alist[tail]) :
            tail -= 1
        if head < tail:
            alist[head] , alist[tail] = alist[tail], alist[head]

    return alist

def alist_order2(alist):
    index_odd = -1
    index_even = -1
    length_odd = 0
    i = 0
    while i < len(alist):
        if is_even(alist[i]) and length_odd==0:
            index_odd = i
        if is_even(alist[i]):
            length_odd+=1

        if not is_even(alist[i]) and length_odd!=0:
            even_temp = alist[i]
            # 偶数整体后移
            for j in range(length_odd,0,-1):
                alist[index_odd+j] =alist[index_odd+j-1]
            alist[index_odd] = even_temp
            index_odd = i
        i+=1

    return alist



def is_even(num):
    return (num & 1) == 0

if __name__ == '__main__':
    alist = [2,4,6,8,10,1,3,5,7,9]
    print(alist_order(alist))
    print(alist_order2(alist))
    print(alist_order2([2,3,4,5]))