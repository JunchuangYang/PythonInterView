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
    随机选取的扑克牌数： [1, 2, 5, 6, 0]
    False
    """