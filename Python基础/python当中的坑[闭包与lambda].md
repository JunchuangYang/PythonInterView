# python当中的坑--闭包与lambda

先来看一个栗子：

```python
def create():
    return [lambda x:i*x for i in range(5)]
 
for i in create():
    print(i(2))
```

结果：

```
8
8
8
8
8
```

create函数的返回值时一个列表，**列表的每一个元素都是一个函数** ，将输入参数x乘以一个倍数i的函数。

预期的结果时0，2，4，6，8. 但结果是5个8，意外不意外。

由于出现这个陷阱的时候经常使用了lambda，所以可能会认为是lambda的问题，但lambda表示不愿意背这个锅。问题的本质在与python中的属性查找规则，

**LEGB（local，enclousing，global，bulitin）**

在上面的例子中，**i就是在闭包作用域（enclousing），而Python的闭包是延迟迟绑定 ， 这意味着闭包中用到的变量的值，是在内部函数被调用时查询得到的**

 解决办法也很简单，那就是变闭包作用域为局部作用域。

```python
def create():
    return [lambda x, i=i:i*x for i in range(5)]
 
for i in create():
    print(i(2))
```

换种写法：

```python
def create():
    a = []
    for i in range(5):
        def demo(x, i=i):
            return x*i
        a.append(demo)
    return a
 
for i in create():
    print(i(2))
```

以上两种写法是一样的

结果：

```
0
2
4
6
8
```

　　---_<_>_---

再来一个问题相似的栗子

代码很简单：（声明:python3问题）

```python
nums = range(2,20)
for i in nums:
    nums = filter(lambda x: x==i or x%i, nums)
print(list(nums))
```

结果:

```python
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

同样按照正常的逻辑结果应该为：

```
[2, 3, 5, 7, 11, 13, 17, 19]
```

问题产生的原因：

- **在python3当中filter()函数返回的是一个迭代器，因此并没有做真正的执行，而是在每次调用的时候执行**（python2中filter()返回的值列表，无此现象）
- 在遍历后执行打印时，现在执行循环当中的函数，同上面一个栗子的问题，**i这个变量使用的是最后调用时的值**，与以上栗子不同的是以上栗子用的是闭包作用域的值，而这个栗子用的是全局i的值

修改代码:

```python
nums = range(2,20)
for i in nums:
    nums = filter(lambda x,i=i: x==i or x%i, nums)
print(list(nums))
```

结果：

```
[2, 3, 5, 7, 11, 13, 17, 19]
```

转：

[python当中的坑【闭包与lambda】](https://www.cnblogs.com/kayb/p/7468801.html)

