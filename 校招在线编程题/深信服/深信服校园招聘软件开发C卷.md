# 深信服校园招聘c/c 软件开发C卷

 https://www.nowcoder.com/test/question/85fc7b237a254acdb5aca673a319be16?pid=23090672&tid=33531380

### 1、字符串匹配

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

 函数match检查字符串str是否匹配模板pattern，匹配则返回0，否则返回-1。模板支持普通字符(a-z0-9A-Z)及通配符`?`和`*`。普通字符匹配该字符本身，`?`匹配任意一个字符，`*`匹配任意多个任意字符。比如字符串abc对下述模板的匹配结果为：

| 模板 | 结果 | 模板 | 结果 |
| ---- | ---- | ---- | ---- |
| abc  | 0    | a*b  | -1   |
| a*   | 0    | ab?  | 0    |
| a*c  | 0    | a?   | -1   |

请完成该函数代码：

```
int match(const char *str, const char *pattern)
{


} 
```



##### **输入描述:**

```
第一行为输入串 第二行为模板串
```

##### **输出描述:**

```
匹配输出match,不匹配输出unmatch
```

##### **输入例子1:**

```
abc
a*c
```

##### **输出例子1:**

```
match
```

**递归判断，遇到*有两种情况，匹配一个或匹配多个**

```python

def solution(str,re_str):
    if len(str)==0 and len(re_str)==0:
        return True
    if (len(str)==0 and len(re_str)!=0) or (len(str)!=0 and len(re_str)==0):
        return False

    if re_str[0]=='*':
        #递归判断，遇到*有两种情况，匹配一个或匹配多个
        return solution(str[1:],re_str[1:]) or solution(str[1:],re_str[:])
    if re_str[0] == str[0] or re_str[0]=='?':
        return solution(str[1:],re_str[1:])
    return False

if __name__ == "__main__":
    #l = list(map(lambda x:int(x),input().split()))
    str = input()
    re_str = input()
    if solution(str,re_str):
        print("match")
    else:
        print("unmatch")

```

### 字符串解析

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

以下函数解析字符串str是否合法的C语言字符串字面值定义(不考虑八进制和十六进制字符编码)，如果是，则将解码后的内容保存到buf中，并返回0，否则返回-1。比如，"hello \"sangfor\""解码后结果为hello "sangfor"，请完成该函数代码：

```
int unescape_c_quoted(char *buf, const char *str)
{

}
```

框架代码：

int main()

{

​    char str[10000];

​    char buf[10000];

​    int len;

​    int ret;

​    if (fgets(str, sizeof(str), stdin) == NULL) {

​        fprintf(stderr, "input error\n");

​        return 0;

​    }

​    len = strlen(str);

​    while (len > 0 && isspace(str[len - 1])) {

​        str[len - 1] = '\0';

​        --len;

​    }

​    ret = unescape_c_quoted(buf, str);

​    if (ret < 0)

​        printf("error\n");

​    else

​        printf("%s\n", buf);

​    fprintf(stderr, "input:%s\noutput:%s\n", str, buf);

​    return 0;

}



##### **输入描述:**

```
字符串
```

##### **输出描述:**

```
解码后的字符串
```

##### **输入例子1:**

```
"\"hello world\\n\\\"too\""
```

##### **输出例子1:**

```
"hello world\n\"too"
```

**没过，格式错误，不知道哪错了，AC：50%**

```python

def solution(str):
    i = 1
    res = ""
    while i<len(str)-1:
        if str[i] =='\\':
            if i+1<len(str) and str[i+1] in ['a','b','e','n','v','t','r','f']:
                if str[i+1]=='a':res+= '\a'
                elif str[i+1]=='b':res+= '\b'
                elif str[i+1]=='e':res+= '\e'
                elif str[i+1]=='n':res+= '\n'
                elif str[i+1]=='v':res+= '\v'
                elif str[i+1]=='t':res+= '\t'
                elif str[i+1]=='r':res+= '\r'
                elif str[i+1]=='f':res+= '\f'
                i+=2
            elif i+1<len(str) and str[i+1]!='\\':
                res+=(str[i+1])
                i+=2
            elif i+1<len(str) and str[i+1]=='\\':
                res+=(str[i])
                i+=2
        else:
            res+=(str[i])
            i+=1

    k = res[:]
    import sys
    sys.stdout.write(k)
if __name__ == "__main__":
    #l = list(map(lambda x:int(x),input().split()))
    str = input()
    solution(str)

```

### 围棋数气

时间限制：C/C++ 1秒，其他语言2秒

空间限制：C/C++ 32M，其他语言64M

函数calc计算围棋盘位置(x,y)处的棋子还有多少口气。

某个位置处的棋子还有多少口气的计算方法(简化计算)：从该位置出发，向四个方向遍历，允许拐弯，但不允许走斜线。如果遇到边线和对方棋子，则认为不能继续往前走。遍历完成后统计遍历过程中遇到的未落子的位置个数，该位置个数即出发点棋子的气的数目。



enum color {

​    NONE, WHITE, BLACK,         // 棋子颜色，NONE表示未落子

};

struct weiqi {

​    enum color board[19][19];   // 棋盘上每个位置的落子

};

int calc(struct weiqi *wq, int x, int y)

{

}



##### **输入描述:**

```
第1-19行数据是棋盘上棋子的颜色数据。0表示未落子，1表示白子，2表示黑子。 第1行最左边位置的坐标是(0,0)，第1行第2列的坐标是(1,0)，第2行第1列的坐标是(0,1)，依此类推。 第20行数据是起始坐标(x,y)
```

##### **输出描述:**

```
位置(x,y)处的棋子还有多少口气，如果该位置未落子，则输出-1
```

##### **输入例子1:**

```
0000000000000000000
0000011000000000000
0000001111000000000
0000001021000000000
0000001110100000000
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
8,3
```

##### **输出例子1:**

```
1
```

##### **例子说明1:**

```
位置(8,3)处的棋子是黑色，还有1口气
```

**与A卷有一题很像**

```python
def dfs(res,x,y,val):
    global result
    if x>=0 and x<len(res) and y>=0 and y<len(res[0]) and (res[x][y]==val or res[x][y]==0):
        if res[x][y]==0:
            result += 1
        res[x][y]=3
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
            print(-1)
```

