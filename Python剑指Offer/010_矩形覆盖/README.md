### 题目描述

我们可以用 2 * 1 的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

### 思路

我们可以用2\*1的小矩形横着或者竖着去覆盖更大的矩形。请问用number个2*1的小矩形无重叠地覆盖一个2\*number的大矩形，总共有多少种方法？

分析：我们化繁为简，从下面的示例说起（设该问题的处理函数为rectCover）。

由于小矩形的尺寸是2×1，所以有大矩形为2×*number*的存在，**那么我们第一步就可以有两种处理方式：**

第一步如果选择竖方向填充，那么该问题的规模就缩减为对于剩余的2×（*number*-1）的大矩形的填充。

![img](./picture/1.png)

　　**如果，第一步如果选择横方向的填充，则第二排的前面两个小矩形也只能如此填充，**那么该问题的规模就缩减为对于剩余的2×（*number*-2）的大矩形的填充.

![img](./picture/2.png)

　　结合上述分析，很容易得到递推的关系： rectCover(number)=rectCover(number-1)+rectCover(number-2)。当然此处也要注意递归跳出条件的判定。

来源：<https://www.cnblogs.com/csbdong/p/5689674.html>

```python
__author__ = 'lenovo'

def rectCover(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return rectCover(num-1) + (num-2)

if __name__ == '__main__':
    print(rectCover(3))
    print(rectCover(4))
    print(rectCover(5))
```

