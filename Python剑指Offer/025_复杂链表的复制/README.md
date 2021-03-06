### 题目描述

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

**解题思路：**

转<https://www.cnblogs.com/darlinFly/p/9339280.html>

1、遍历链表，复制链表中的每个结点，并将复制的结点插入到该结点的后面。例如，原链表为A->B->C, 遍历完毕后，链表变为A->A'->B->B'->C->C'，其中A‘，B'，C'是结点A，B，C的复制结点。

看图中，蓝色箭头为next指针：

![img](https://images2018.cnblogs.com/blog/1379031/201807/1379031-20180720004256599-1726273203.png)  

复制结点后：

![img](https://images2018.cnblogs.com/blog/1379031/201807/1379031-20180720004316219-1927624298.png)

2、为复制结点的random指针赋值

如果原结点的random指针指向的是结点B，那么将复制结点的random指针指向结点B的复制结点B'。

图中黑色箭头为random指针：

![img](https://images2018.cnblogs.com/blog/1379031/201807/1379031-20180720005111566-783733294.png)

复制结点的random指针赋值后：

![img](https://images2018.cnblogs.com/blog/1379031/201807/1379031-20180720005045852-845801966.png)

3、将链表的原始结点与复制结点分割至两个链表，使原始结点构成一个链表，复制结点构成一个链表。

 ![img](https://images2018.cnblogs.com/blog/1379031/201807/1379031-20180720005505570-2076127344.png)