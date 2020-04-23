### 题目描述

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：

  1     2     3    4

 5     6     7    8

 9    10   11  12

 13  14   15  16

 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

### 思路

模拟

```python
def print_matrix(mat):
    rows = len(mat)#行
    cols = len(mat[0]) if mat else 0#列
    start = 0
    ret = []
    # 每次循环打印一圈
    while start * 2 < rows and start * 2 < cols:
        circle_matrix(mat,start,rows,cols,ret)
        start += 1
    return ret

def circle_matrix(mat,start,rows,cols,ret):
    row = rows-start#最后一行
    col = cols-start#最后一列
    # left->right
    for i in range(start,col):
        ret.append(mat[start][i])
    # top->bottom
    if start<row-1:
        for i in range(start+1,row):
            ret.append(mat[i][col-1])
    # right->left
    if start<row-1  and start<col-1:
        for i in range(col-1,start,-1):
            ret.append(mat[row-1][i-1])
    # bottom->top
    if start<row-1  and start<col-1:
        for i in range(row-1,start+1,-1):
            ret.append(mat[i-1][start])

if __name__ == "__main__":
    """
    mat = [[1, 2, 3],
           [5, 6, 7],
           [9, 10, 11]]
    mat = [[]]
    mat = [[1]]
    mat = [[1, 2, 3, 4]]
    mat = [[1], [2], [3], [4]]
    """
    mat = [[1],
           [2],
           [3],
           [4]]
    print(print_matrix(mat))
```

