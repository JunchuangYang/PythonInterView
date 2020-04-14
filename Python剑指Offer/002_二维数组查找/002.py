#__author__ = 'lenovo'

def find(target,array):
    n = len(array)
    m = len(array[0])
    i = n-1
    j = 0
    # 从二维数组左下角开始搜索
    while i>=0 and j<m:
        if target == array[i][j]:
            return True
        elif target > array[i][j]:
            j += 1
        elif target < array[i][j]:
            i -= 1
    return False

print(find(15,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))