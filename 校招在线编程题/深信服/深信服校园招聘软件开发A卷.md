# 深信服校园招聘c/c 软件开发A卷

<https://www.nowcoder.com/test/question/2242f11982e44881b749d9d188f0ccf5?pid=23090658&tid=33515484>

### 1、围棋遍历

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

函数calc计算围棋中位置(x,y)处连成一片的棋子个数。所谓连成一片，即沿着棋盘横竖线往任意方向遍历，遍历过程允许转弯，不允许走斜线，中间未出现对方棋子或空子。

##### **输入描述:**

```
第1-19行数据是棋盘上棋子的颜色数据。0表示未落子，1表示白子，2表示黑子。 第1行最左边位置的坐标是(0,0)，第1行第2列的坐标是(1,0)，第2行第1列的坐标是(0,1)，依此类推。 第20行数据是起始坐标(x,y)
```

##### **输出描述:**

```
与坐标(X,Y)连成一片的棋子数目
```

##### **输入例子1:**

```
0000000000000000000
0000011000000000000
0000001111000000000
0000001021000000000
0000001010100000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
0000000000000000000
5,1
```

##### **输出例子1:**

```
9
```

**深搜，注意给出的x,y值是颠倒的**

```python
__author__ = 'lenovo'


def dfs(res,x,y,val):
    global result
    if x>=0 and x<len(res) and y>=0 and y<len(res[0]) and res[x][y]==val:
        res[x][y]=0
        result += 1
        dfs(res,x+1,y,val)
        dfs(res,x,y+1,val)
        dfs(res,x-1,y,val)
        dfs(res,x,y-1,val)
    return

res = []
result = 0
for i in range(20):
    line = input()
    if i != 19:
        res.append(list(map(lambda x:int(x),line[:])))
    else:
        x,y = str(line).split(',')
        val = res[int(y)][int(x)]
        if res[int(y)][int(x)] != 0:
            dfs(res,int(y),int(x),val)
            print(result)
        else:
            print(0)
```

### 2、单链表排序

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

请实现list_sort，使用冒泡法将head指向的链表按val值大小排成升序

##### **输入描述:**

```
第一行为数据个数 第二行为输入的数据，以空格进行分隔
```

##### **输出描述:**

```
输出head指向的链表数据，以空格分隔
```

##### **输入例子1:**

```
12
10 22 2 5 9 8 1 33 4 6 7 9
```

##### **输出例子1:**

```
1 2 4 5 6 7 8 9 9 10 22 33
```



```python
__author__ = 'lenovo'


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkNode(object):
    def __init__(self):
        self.head = None

    def construct_Link(self,vals):
        if not vals:
            return None
        self.head = Node(vals[0])
        node = self.head
        for i in range(1,len(vals)):
            temp = Node(vals[i])
            node.next = temp
            node = temp

        return self.head

    def list_sort(self,head,length):

        current = head
        for i in range(length):
            temp = current
            for j in range(i+1,length):
                temp = temp.next
                if temp.val<current.val:
                    temp.val ,current.val = current.val,temp.val
            current = current.next

        return head

if __name__ == "__main__":
    n = int(input())
    vals = list(map(lambda x:int(x),input().split()))
    LN = LinkNode()
    head = LN.construct_Link(vals)
    head = LN.list_sort(head,n)
    while head:
        print(head.val,"",end="")
        head = head.next
```

### 3、出栈顺序

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

```
`已知某一个字母序列，把序列中的字母按出现顺序压入一个栈，在入栈的任意过程中，允许栈中的字母出栈，求所有可能的出栈顺序`
```

##### **输入描述:**

```
字符串，如：abc
```

##### **输出描述:**

```
可能的出栈顺序，每行一种顺序
```

##### **输入例子1:**

```
abc
```

##### **输出例子1:**

```
abc
acb
bac
bca
cba
```

**思路：**
**遍历序列中的每一个字母，先把当前字母入栈，这个时候，栈中肯定有字母，你可以选择继续遍历序列，也可以在这个时候把栈中的字母一个一个出栈，**
**最后，遍历完序列后，再把栈中的所有字母顺序出栈，这样子就可以得到所有合法的序列；**

<https://www.cnblogs.com/hotsnow/p/12856239.html>

```python
__author__ = 'lenovo'

class Solution(object):

    @staticmethod
    def my_permutation(s_input,res,i,temp,s_stack):
        # 将temp 和 s_stack 保存问当前递归层次状态
        temp = temp[:]
        s_stack = s_stack[:]

        if len(temp) == len(s_input):
            res.append(temp[:])
            return
        if i>=len(s_input):
            return
        s_stack.append(s_input[i])
        # 1.入栈
        Solution.my_permutation(s_input,res,i+1,temp,s_stack)

        # 2.弹出当前栈中字符
        while s_stack:
            temp.append(s_stack[-1])
            s_stack.pop()
            Solution.my_permutation(s_input,res,i+1,temp,s_stack)


if __name__ == '__main__':
    s_input = input()
    res = []
    """
    s_input:原始字符串
    res：最终的结果
    i：当前字符
    temp：保存弹出的字符
    s_tack：栈
    """
    Solution.my_permutation(s_input,res,0,[],[])
    res.sort()
    for items in res:
        print("".join(items))

```




  