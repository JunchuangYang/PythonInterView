### 题目描述

LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....

LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。

LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

### 思路

模拟：将扑克牌从排序，找出最大的数，依次减一；如果data中没有，有0的话用0代替，否则return False。

```python
import random

__author__ = 'lenovo'


def solution(data,n):
    print("随机选取的扑克牌数：",data)
    length = len(data)
    zero = data.count(0)
    data.sort()

    num = data[-1]
    index = length-2 # 倒数第二个数
    n-=1
    while n:
        if data[index] == num - 1:
            index -= 1
            num -= 1
        elif zero >0:
            zero -= 1
            num -= 1
        else:
            return False
        n-=1
    return True

if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            0, 0, 0, 0]
    t = 5
    data = [random.choice(test) for _ in range(t)]
    print(solution(data, t))
    print(solution([0,0,1,0,0], t))
    print(solution([2,4,1,3,5], t))
    print(solution([12,9,10,0,13], t))
    print(solution([7,8,9,0,0], t))
    print(solution([7,0,9,0,0], t))
    print(solution([1,2,5,6,7], t))

    """
    随机选取的扑克牌数： [3, 8, 8, 13, 5]
    False
    随机选取的扑克牌数： [0, 0, 1, 0, 0]
    True
    随机选取的扑克牌数： [2, 4, 1, 3, 5]
    True
    随机选取的扑克牌数： [12, 9, 10, 0, 13]
    True
    随机选取的扑克牌数： [7, 8, 9, 0, 0]
    True
    随机选取的扑克牌数： [7, 0, 9, 0, 0]
    True
    随机选取的扑克牌数： [1, 2, 5, 6, 7]
    False
    """
```

