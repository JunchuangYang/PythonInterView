__author__ = 'lenovo'
"""
连续子数组的最大和
动态规划问题
"""
def max_sum(nums):
    if not nums:
        return None
    ret = float("-inf")
    sum = 0
    for i in nums:
        if sum <= 0:
            sum = i

        else:
            sum += i

        ret = max(ret , sum)

    return ret

if __name__ == "__main__":
    test = [1, 2, -2, 3, 6, 0, -2]
    print (max_sum(test))