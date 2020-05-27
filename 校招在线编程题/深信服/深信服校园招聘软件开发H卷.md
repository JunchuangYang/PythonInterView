# 深信服校园招聘c/c 软件开发H卷

### 1、访问权限

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

JSON是一种可以用来保存配置的数据格式，其结构为树状。

JSON中某个子节点的位置可以JSON路径的形式表示，JSON路径类似UNIX文件路径，以'/'分隔父子节点名。JSON路径中不会出现空格。

如下JSON值中

mem -- daemons -- findme

​    |          |- waccd

​    |

​    |- apps -- appd

findme子节点的JSON路径为： /mem/daemons/findme

appd子节点的JSON路径为：/mem/apps/appd

waccd子节点的JSON路径为：/mem/daemons/waccd

有一个列表用来描述各JSON子节点是否允许用户编辑。如下：

Y /mem/daemons/findme

N /mem/daemons

Y /mem

如果有设置用户对某个子节点的权限，则实际权限为该设定权限，否则继承其父节点的可访问性，对根节点的默认访问权限为N。



##### **输入描述:**

```
第一行为一个正整数N，表示接下来有N行数据(0 < N < 100)
第2行到第N+1行，为字符串Path，表示待检查访问权限的JSON路径。
第N+2行为一个正整数T，表示接下来有T行数据（0 < T < 1000）

接下来会有T行数据，格式为"权限 JSON路径"。

权限有两种取值：Y和N
JSON路径最大长度为256
```

##### **输出描述:**

```
输出“权限”，权限表示该节点的实际访问权限。
```

##### **输入例子1:**

```
1
/mem/total
3
Y /mem/daemons/findme
N /mem/daemons
Y /mem
```

##### **输出例子1:**

```
Y
```

**要考虑的情况挺多的**

1. **在每个文件路径后面加上`/`,防止出现`/men /me`这种情形**
2. **要考虑文件路径权限中出现根`/`文件的情况**
3. **要考虑文件路径权限中出现根`/`文件和 `N /men/`的情况**
4. **将所给的文件路径按降序排列，以str1为子路径，查找str2父路径的权限情况**

```python
# -*- coding:utf-8 -*-
import sys
n = int(input())
str1 = []
for _ in range(n):
    str1.append(input()+"/")

m = int(input())
str3 = []
str2 = []
FFF = 0
for _ in range(m):
    l = list(input().split())
    if l[1]=='/':
        FFF=1
    str2.append([l[0],l[1]+"/"])

str2.sort(key = lambda x:x[1],reverse=True)
for i in range(n):
    flag = 0
    for j in range(m):
        #print(str1[i],str2[j],str1[i].find(str2[j]) )
        if str1[i] == str2[j][1]:
            flag=1
            print(str2[j][0])
            break
        elif str1[i].find(str2[j][1])==0 and str2[j][0]=="Y" and len(str2[j][1]) <= len(str1[i]):
            flag=1
            print("Y")
            break
    if FFF==1 and flag==0:
        print("Y")
    elif flag ==0:
        print("N")
```

### 2、手机号查询

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 64M，其他语言128M

信服君接到一项任务需要制作一个手机号码查询系统，输入连续的数字后，需要显示所有包含该连续数字的手机号。为了验证算法，信服君目前只需输出手机号的个数即可。



##### **输入描述:**

```
首行输入两个整数N，M（1<=N<=15000，1<=M<=100000），之后是N行输入，表示有N个手机号码，每个手机号码由11位首位不为零的连续数字组成，接着是M行查询，每行由连续的数字组成，长度为L（1<=L<=11）。
```

##### **输出描述:**

```
每个请求输出包含查询数字串的不同的手机号共有多少个。
```

##### **输入例子1:**

```
3 2
15623651459
18956036508
18625690367
333
036
```

##### **输出例子1:**

```
0
2
```

**普通模拟超时**

在讨论区看到使用C++中STL的map和set函数通过了，于是想到使用Python中的dict和set:

1. **将输入的每个手机号依次切分成所有的情况，存在str1中;**
2. **使用set对str1去重;**
3. **使用字典判断str1中字符串是否存在，存在+1，不存在添加进去使其等于1**
4. **对所有输入的手机号创建字典，防止手机号冗余（不加只能过case 90%）**

```python
# -*- coding:utf-8 -*-
import sys
l = list(map(int,input().split()))
n,m=l[0],l[1]
dic = {}
dicphone = {}
for _ in range(n):
    s = input()
    str1 = []
    for i in range(11):
        for j in range(i,11):
            str1.append(s[i:j+1])
    #print(str1)
    if s not in dicphone.keys():
        str2 = list(set(str1))
        #print(str2)
        for item in str2:
            if item in dic.keys():
                dic[item]+=1
            else:
                dic[item]=1
        dicphone[s]=1
for _ in range(m):
    s = input()
    #print(dic)
    try:
        print(dic[s])
    except KeyError :
        print(0)
```

### 3、数字序列

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

信服君最近在研究一种有趣的数字串，例如11135917171513...，你可能发现了，除了开始的三个数字为1以外，后面的数字均由三位数字相加得到，现在信服君想知道在给定任意起始三个数字后，第n位是多少。



##### **输入描述:**

```
首行输入一个整数T（1<=T<=1000），表示有T组数据，每组数据给出四个数字a、b、c、n其中前三位依次表示起始的三个数字，n表示求第n位数是多少。其中（0<=a,b,c<10）（1<=n<=10^9）。
```

##### **输出描述:**

```
每组请求输出第n位数字是多少。
```

##### **输入例子1:**

```
2
1 1 1 10
2 3 9 100
```

##### **输出例子1:**

```
7
4
```

**后台测试数据应该有错误。找循环节，有规律可寻。暴力超时。**

``` 
# -*- coding:utf-8 -*-
n = int(input())
for _ in range(n):
    l = list(map(int,input().split()))
    a = l[0]
    b = l[1]
    c = l[2]
    m = l[3]
    num = 0
    s = str(a)+str(b)+str(c)
    num += len(s)
    if m<=num:
        print(s[m-1])
    else:
        while num <= 100:
            d = a+b+c
            temp = str(d)
            num+=len(temp)
            s += temp
            a = int(s[-3])
            b = int(s[-2])
            c = int(s[-1])
        # 找循环节
        sss = []
        sssi = 0
        #print(s)
        for i in range(len(s)):
                if s.count(s[i:len(s)])>2:
                   sss = s[i:]
                   break
        #print(sss)
        index = s.index(sss)
        if not sss or m <100 :
            print(s[m-1])
        else:
            k = (m-index)%len(sss)
            if k ==0:
                k = len(sss)
            print(sss[k-1])
```

