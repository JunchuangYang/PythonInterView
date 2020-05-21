# 深信服校园招聘软件开发D卷

### 1、二进制位反序

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

编写函数reverse，将val(32位无符号整数)的二进制位反序。比如，如果val的二进制表示为1011000011111111，反序后val的二进制表示为1111111100001101。

unsigned int reverse(unsigned int val)

{

}

##### **输入描述:**

```
16进制的一个无符号整数
```

##### **输出描述:**

```
16进制的一个无符号整数
```

##### **输入例子1:**

```
0x1
```

##### **输出例子1:**

```
80000000
```



```python

def unsigned_int_reverse(str):
    num = int(str,16)
    bin_list = list(bin(num))[::-1]
    res = 0
    mi = 0
    j=0
    for i in range(31,-1,-1):
        if j<len(bin_list)-2:
           res += pow(2,i)*int(bin_list[j])
           j+=1
        else:
            break
    print(''.join(list(hex(res))[2:]).zfill(8))

    #print(''.join(list(hex(res))[2:]).rjust(8,'0'))	

if __name__ == "__main__":
    str = input()
    unsigned_int_reverse(str)
```

**补充：python 字符串补全填充固定长度（补0）**

```python
'''
原字符串左侧对齐， 右侧补零:
'''
str.ljust(width,'0') 
input: '789'.ljust(32,'0')
output: '78900000000000000000000000000000'


'''
原字符串右侧对齐， 左侧补零:
方法一：
'''
str.rjust(width,'0') 
input: '798'.rjust(32,'0')
output: '00000000000000000000000000000798'
'''
方法二：
'''
str.zfill(width)
input: '123'.zfill(32)
output:'00000000000000000000000000000123'
'''
方法三：
'''
'%07d' % n
input: '%032d' % 89
output:'00000000000000000000000000000089'
原文链接：https://blog.csdn.net/weixin_42317507/java/article/details/93411132
```

### 2、统计累加算式

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

一个正整数可以表示为多个正整数相加的表达式，表达式中的各个正整数要求都是2的幂。例如给定正整数7，它有下列六个符合要求的表达式：

1)1+1+1+1+1+1+1 

2)1+1+1+1+1+2 

3)1+1+1+2+2 

4)1+1+1+4 

5)1+2+2+2 

6)1+2+4

因此，正整数7符合条件的表达式个数是6. 编写一个程序，对于给定的正整数N(1 <= N <= 1,000)，输出符合条件的表达式个数。要求：时间复杂度不高于O(N)。



##### **输入描述:**

```
一个整数（>=1并且<=1000）
```

##### **输出描述:**

```
表达式个数
```

##### **输入例子1:**

```
7
```

##### **输出例子1:**

```
6
```

**没有做出来，知道有规律，但是一直找不出来规律。**

题解：<https://blog.csdn.net/asneverbefore/article/details/78232898>

```python
"""
1 0
2 2
3 2
4 4
5 4
6 6
7 6
8 10
9 10
"""
if __name__=='__main__':
    num  = int(input())
    res = [0,1]
    for m in range(2,num+1):
        if m%2==1:
            res.append(res[m-1])
        else:
            res.append(res[m-1]+res[m//2])
    print(res[num])
```

### 3、攻击识别

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

小明的服务器遭到了黑客的攻击，他想了一个简易的办法来判断服务器收到的数据包是否是来自黑客的攻击。

小明假设黑客的攻击都是往一些模式串里插入一个片段伪装出来的，例如模式串M为AN--ATTACK，那么黑客可能往M里插入一段信息，如在AN-后插入hello，来得到伪装后的数据包，AN-hello-ATTACK。小明想出了一系列的模式串Mi，你能否帮助小明判断服务器收到的数据包是否可能由某个模式串伪装而成。

示例，给定两个模式串M1=abc，M2=abd，那么数据包abec可能是攻击（模式M1），但数据包xyz则不属于M1、M2里面任何一个类型的攻击。

##### **输入描述:**

```
输入的第一行一个正整数n（1 ≤ n ≤ 100000），表示n种攻击模式。

接下来n行，其中第i行一个字符串Mi（1 ≤ strlen(Mi) ≤ 50），表示第i种攻击模式。

在接下来一个正整数k，表示有k（1 ≤ k ≤ 100）个数据包。

接下来k行，其中第i行一个字符串Di（1 ≤ strlen(Di) ≤ 1000），表示第i个数据包。

有50%的输入数据满足：1 ≤ n ≤ 10
```

##### **输出描述:**

```
输入k行,每行输出“YES”或者“NO”(全部大写)。

其中第i行表示第i个数据包有没有可能是攻击。
```

##### **输入例子1:**

```
3
abc
abd
xyz
6
abacac
affffbd
xxxxxxyyyyz
aaabbbbcccc
ifqwefxxf
xayaz
```

##### **输出例子1:**

```
YES
YES
YES
NO
NO
NO
```

**感觉不难啊，求一个字符串是不是由另一个字符串中间插入字符组成的。难道我理解错了，有坑？mei AC**

```python
# case 0%
def solution(mi,di):
    flag = 0
    for i in range(len(mi)):
        str = mi[i]
        for j in range(1,len(str)):
            left = str[0:j]
            right = str[j:]
            #print("*"*3,left,"  ",di[0:j])
            #print("*"*3,right,"  ",di[len(di)-(len(str)-j):])
            if left==di[0:j] and right == di[len(di)-(len(str)-j):]:
                flag=1
                break
        if flag:break
    if flag:print("YES")
    else: print("NO")


if __name__=='__main__':
    n = int(input())
    mi = []
    for _ in range(n):
        mi.append(input())
    k = int(input())
    for _ in range(k):
        di = input()
        #print(di)
        solution(mi,di)
```

