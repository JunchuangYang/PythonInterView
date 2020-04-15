# __author__ = 'lenovo'

def find_min(nums):
    if not nums:
        return False

    length = len(nums)
    left , right = 0, length-1

    # (1)如果数列第一个元素不大于等于最后一个元素，则第一个元素为最小
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        mid = (left+right)/2

        # (2)如果第一个元素和中间元素和最后一个元素相等，无法使用二分法判断最小值
        if nums[left] == nums[mid] == nums[right]:
            return min(nums)

        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid

    return nums[0]

if __name__ == '__main__':
    # 正常情况
    print(find_min([2, 2, 4, 5, 6, 2]))
    print(find_min([1, 0, 0, 1]))

    # 对应第一种情况
    print(find_min([0, 1, 2, 3, 4]))

    # 对应第二种情况
    print(find_min([1, 0, 1, 1, 1, 1]))