# 深信服校园招聘c/c 软件开发B卷

### 1. 位对齐

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

编写函数align_n，将size的低n位（即：0到n-1位）清零，如果清零前size的低n位不为全零，则在第n位上加1。n满足32>n>0。

align_n的函数原型：

unsigned int align_n(unsigned int size, int n);

##### **输入描述:**

```
size（十六进制）,n（十进制）
```

##### **输出描述:**

```
align_n的运算结果（十六进制）
```

##### **输入例子1:**

```
0x7,3
```

##### **输出例子1:**

```
0x8
```

##### **输入例子2:**

```
0x8,3
```

##### **输出例子2:**

```
0x8
```

##### **输入例子3:**

```
0x1,3
```

##### **输出例子3:**

```
0x8
```

**思路：用了Python的一些进制转换函数，如果不让用这些函数这题还是比较难得**

```python
# 十进制转换成二进制
num = 8
v = bin(num)
print(v)   ------0b1000------

# 十进制转换成八进制
num = 8
v = oct(num)
print(v)    ------0o10------

# 十进制转换成十六进制
num = 8
v = hex(num)
print(v)   ------0x8------

# 二进制转换成十进制
v1 = '0b1111'
result = int(v1,base=2)
print(result)   ------15------

# 八进制转换成十进制
v1 = '0o1111'
result = int(v1,base=8)
print(result)   ------585------

# 十六进制转换成十进制
v1 = '0x1111'
result = int(v1,base=16)
print(result)    ------4369------
```

**最后有一个数字超出整型范围的情况，用Python应该不会超，c/c++应该会超范围，最后的结果也是给出的超超范围的结果，所以用Python的最好判断以下。**

```python
__author__ = 'lenovo'

class Solution(object):
    def solution(self,s,n):
        s_hex = int(s,16) # 16->10
        s_bin = bin(s_hex) # 10->2
        s_bin = list(str(s_bin)[::-1])
        flag = 0
        #print("*"*3,s_bin)
        n1 = min(len(s_bin)-2,n)
        for i in range(n1):
            if s_bin[i]!="0":
                s_bin[i]="0"
                flag=1
        m=0
        if flag:
            m = 2**(n)
        #print("*"*3,s_bin)
        #print("*"*3,m)
        s_bin= s_bin[::-1]
        res = int("".join(item for item in s_bin),2)+m
        if res >= 2**32:
            res = 0
        print(hex(res))

if __name__ == '__main__':
    s , n = input().split(",")
    sou = Solution()
    sou.solution(s,int(n))

```

### 2.堆排序

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

函数heap_sort使用堆排序方法对数组arr进行排序，排序后数据为降序。相关代码如下，请补充缺失部分。



void heap_arrange(int arr[], int cur, int cnt)  //调整为小顶堆

{

​    int heaptop_val = arr[cur]; //堆顶的值

​    while (cur < cnt) {

​        int left = 2 * cur + 1;

​        int right = 2 * cur + 2;

​        int min = -1;

​        int min_val = ______; 

​        if (left < cnt && arr[left] < min_val) { //检查是否比左节点大

​            min = left;

​            min_val = arr[left];

​        }

​        if (right < cnt && arr[right] < min_val) {//检查是否比右节点大

​            min = right;

​        }

​        if (min == ______) 

​            break;

​        arr[cur] = ______; 

​        cur = ______; 

​    }

​    arr[cur] = ______;

}

void heap_sort(int arr[], int cnt)

{

​    int i;

​    for (i = cnt / 2 - 1; i >= 0; --i) {

​        heap_arrange(arr, i, cnt);

​    }

​    for (i = cnt - 1; i > 0; --i) {

​        int tmp;

​        tmp = arr[0];

​        arr[0] = arr[i];

​        arr[i] = tmp;

​        heap_arrange(arr, 0, i);

​    }

}



##### **输入描述:**

```
第一行为数据个数 第二行为输入数据
```

##### **输出描述:**

```
排序过程的中间数据，及已经排好序的数据
```

##### **输入例子1:**

```
10
100 32 3 6 24 86 23 90 78 3
```

##### **输出例子1:**

```
origin:
100 
 32   3 
  6  24  86  23 
 90  78   3 

make heap:
  3 
  6   3 
 78  24  86  23 
 90 100  32 

sort i=9
 32 
  6   3 
 78  24  86  23 
 90 100   3 

  3 
  6  23 
 78  24  86  32 
 90 100   3 

sort i=8
100 
  6  23 
 78  24  86  32 
 90   3   3 

  6 
 24  23 
 78 100  86  32 
 90   3   3 

sort i=7
 90 
 24  23 
 78 100  86  32 
  6   3   3 

 23 
 24  32 
 78 100  86  90 
  6   3   3 

sort i=6
 90 
 24  32 
 78 100  86  23 
  6   3   3 

 24 
 78  32 
 90 100  86  23 
  6   3   3 

sort i=5
 86 
 78  32 
 90 100  24  23 
  6   3   3 

 32 
 78  86 
 90 100  24  23 
  6   3   3 

sort i=4
100 
 78  86 
 90  32  24  23 
  6   3   3 

 78 
 90  86 
100  32  24  23 
  6   3   3 

sort i=3
100 
 90  86 
 78  32  24  23 
  6   3   3 

 86 
 90 100 
 78  32  24  23 
  6   3   3 

sort i=2
100 
 90  86 
 78  32  24  23 
  6   3   3 

 90 
100  86 
 78  32  24  23 
  6   3   3 

sort i=1
100 
 90  86 
 78  32  24  23 
  6   3   3 

100 
 90  86 
 78  32  24  23 
  6   3   3 

sorted:
100 
 90  86 
 78  32  24  23 
  6   3   3
```

堆排序

```python
def heap_adjust(arr,start,end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child+1 <= end and arr[child] > arr[child+1]:
            child += 1

        if arr[root] > arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
 
def heap_sort(arr):
    first=len(arr) // 2 - 1
    for start in range (first, -1, -1):
        heap_adjust(arr, start, len(arr)-1)
    print("make heap:")
    fprint(arr)

    for end in range (len(arr)-1, 0, -1):
        print("sort i=%d"%end)
        arr[0], arr[end] = arr[end], arr[0]
        fprint(arr)
        heap_adjust(arr, 0, end-1)
        fprint(arr)

def fprint(arr):
    flag = 0
    index = pow(2,flag)
    k = 1
    for i in range(len(arr)):
        if k == index:
            print("%3d"%arr[i])
            flag+=1
            index = pow(2,flag)
            k=0
        else:
            print("%3d"%arr[i],end="")
        k+=1
    print("")

def main():
    ll = input()
    l = list(map(lambda x:int(x),input().split()))
    print("origin:")
    fprint(l)
    heap_sort(l)
    print ("sorted:")
    fprint(l)
 
if __name__ == "__main__":
    main()

```

**代码结果没问题，但是它一直说换行和空格有错误，不知道是哪里的问题，没AC**