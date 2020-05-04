__author__ = 'lenovo'

"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加
"""
def solution(alist,target):
    left = 0
    right = len(alist) - 1
    while left < right:
        sum = alist[left] + alist[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else :
            return alist[left],alist[right]

if __name__ == '__main__':
    test = [-4, 0, 1, 2, 4, 6, 8, 10, 12, 15, 18]
    s = 12
    print (solution(test, s))