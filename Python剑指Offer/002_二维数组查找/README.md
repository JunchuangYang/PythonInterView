### 题目描述

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

### 分治解题思路

 从左下角上角开始查找：

- 如果target更大，指针右移
- 如果target更小，指针上移

从右上角开始查找：

- 如果target更大，指针下移

- 如果target更小，指针左移

  ------

  ---

  ---


```python
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
```

