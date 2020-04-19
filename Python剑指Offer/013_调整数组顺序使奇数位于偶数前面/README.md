### 题目描述

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。

### 思路

使用两个指针，前后各一个，一个检测奇数，一个检测偶数，然后连个相互换。注意要head < tail（代码中加*号的部分）

为了更好的扩展性，可以把判断奇偶部分抽取出来

```python
def alist_order(alist):
    head = 0
    tail = len(alist) - 1
    while head<=tail:
        while not is_even(alist[head]):
            head += 1
        while is_even(alist[tail]) :
            tail -= 1
        if head < tail:#**********
            alist[head] , alist[tail] = alist[tail], alist[head]

    return alist

def is_even(num):
    return (num & 1) == 0

if __name__ == '__main__':
    alist = [2,4,6,8,10,1,3,5,7,9]
    print(alist_order(alist))
    #output
    [9, 7, 5, 3, 1, 10, 8, 6, 4, 2]
```

### 题目描述

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。**并保证奇数和奇数，偶数和偶数之间的相对位置不变。**

### 思路

1.从前往后遍历，如果是第一个偶数，记住这个偶数的下标。偶数长度+1。在遇到偶数的时候长度+1，不记下标。

2.当遇到奇数的时候，判断其前面有没有偶数，如果有，则将前面的连续的多个偶数，顺序往后移动一位，然后将奇数插入第一个偶数位置。

```python
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
    print(alist_order2(alist))
    print(alist_order2([2,3,4,5]))
```

