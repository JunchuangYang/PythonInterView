# Java 面试题

文章参考：https://blog.csdn.net/qq_42999092/article/details/109068522

## JavaSE

### 1.自增变量

```java
public static void main(String[] args) {
    public static void main(String[] args) {
        /*
        *赋值=，最后计算
        *=右边的从左到右加载值依次压入操作数栈
        *实际先算哪个，看运算符的优先级
        *自增、自减操作都是直接修改变量的值，不经过操作数栈
        *最后的赋值之前，临时结果也存在操作数栈中
        *赋值赋的是操作数栈中的值
        * */
        int i = 1;
        /*
        * 1.把i的值压入操作数栈。 操作数栈： i=1
        * 2.i变量自增1。局部变量表：i=2
        * 3.把操作数栈中的i=1 赋给 局部变量表中的 i。 i=1
        * */
        i = i++;// i=1
        int j = i++;//j=1，i=2
        int k = i + ++i * i++;//
        System.out.println("i=" + i);//4
        System.out.println("j=" + j);//1
        System.out.println("k=" + k);//11
    }
}
```

### 2.写一个Singleton示例

#### 什么是Singleton?

Singleton:在Java中 即指单例设置模式，探视软件开发最常用的设置模式之一

单：唯一

例：实例

单例设计模式，即某个类在整个系统中只能有一个实例对象可被获取和使用的代码模式

例如：代表JVM运行环境的Runtime类

#### 要点：

##### 一是某个类只能有一个实例

 构造器私有化

##### 二是他必须自行创建实例

 含有一个该类的静态变量来保存这个唯一的实例

##### 三是它必须自行向整个系统提供这个实例

 对外提供获取该类实例对象的方式

- 直接暴露
- 用静态变量的get方法获取

####　几种常见形式

饿汉式：直接创建对象，不存在线程安全问题

>  直接实例化饿汉式(简洁直观)
>
>  枚举式 (最简洁)
>
>  静态代码块饿汉式(适合复杂实例化)

懒汉式;延迟创建对象

>  线程不安全(使用于单线程)
>
>  线程安全(使用于多线程)
>
>  静态内部类模式 (适用于多线程)

#### 饿汉式

##### 直接实例化饿汉式(简洁直观)

```java
public class Singleton1 {
    /**
     * 1、构造器私有化
     * 2、自行创建，并且用静态变量保存
     * 3、向外提供实例
     * 4、强调这是一个单例，我们可以用final修改
     */
    private Singleton1() {

    }
    public static final Singleton1 INSTANCE = new Singleton1();

}
```

##### 枚举式 (最简洁)

```java
public enum  Singleton2 {
    /**
     * 枚举类型：表示该类型是有限的几个
     */
    INSTANCE
}
```

##### 静态代码块饿汉式(适合复杂实例化)

```java
public class Singleton3 {
    /**
     *  静态代码块
     */
    public static final Singleton3 INSTANCE;
    private String info;
	// 类加载时创建实例对象
    static {
        try {
            INSTANCE = new Singleton3("123");
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }
    private Singleton3(String info) {
        this.info = info;
    }
}
```

#### 懒汉式

##### 线程不安全(使用于单线程)

```java
public class Singleton4 {
    /**
     * 1、构造器私有化
     * 2、用一个静态变量保存这个唯一的实例
     * 3、提供一个静态方法，获取这个实例对象
     */
    static Singleton4 instance;
    private Singleton4() {}

    public static Singleton4 getInstance() {
            if (instance == null) {
                instance = new Singleton4();
            }
            return instance;

    }
}
```

##### 线程安全(使用于多线程)

```java
public class Singleton5 {
    /**
     * 1、构造器私有化
     * 2、用一个静态变量保存这个唯一的实例
     * 3、提供一个静态方法，获取这个实例对象
     */
    static Singleton5 instance;
    private Singleton5() {}

    public static Singleton5 getInstance() {
        if (instance == null) {
            synchronized (Singleton5.class) {
                if (instance == null) {
                    instance = new Singleton5();
                }
                return instance;
            }
        }
        return instance;
    }
}
```

##### 静态内部类模式 (适用于多线程)

```java
public class Singleton6 {
    /**
     * 1、内部类被加载和初始化时，才创建INSTANCE实例对象
     * 2、静态内部类不会自动创建,随着外部类的加载初始化而初始化，他是要单独去加载和实例化的
     * 3、因为是在内部类加载和初始化时，创建的，因此线程安全
     */
    private Singleton6(){}

    public static class Inner{
        private static final Singleton6 INSTANCE = new Singleton6();
    }
    public static Singleton6 getInstance() {
        return Inner.INSTANCE;
    }
}
```

### **3.Java中访问修饰符public、private、protected、以及default(默认不写) 时的区别？？**

Java有四种访问权限，其中三种有访问权限修饰符，分别为private，public和protected，还有一种不带任何修饰符：

```
    1、private，私有的，被private修饰的类、方法、属性、只能被本类的对象所访问。

            我什么都不跟别人分享。只有自己知道。

    2、default，默认的，在这种模式下，只能在同一个包内访问。

            我的东西可以和跟我一块住的那个人分享。

    3、protected，受保护的，被protected修饰的类、方法、属性、只能被本类、本包、不同包的子类所访问。

            我的东西我可以和跟我一块住的那个人分享。另外也可以跟不在家的儿子分享消息，打电话

    4、public，公共的，被public修饰的类、方法、属性、可以跨类和跨包访问。

            我的东西大家任何人都可以分享。
```

### 4、类初始化实例初始化

#### 类初始化

> 一个类要创建实例需要先加载并初始化该类
>
>  main方法所在的类需要先加载和初始化
>
> 一个子类要初始化需要先初始化父类
>
> 一个类初始化就是执行 clinit 方法
>
>  clinit 方法由**静态类变量显示赋值代码和静态代码块组成**
>
>  **类变量显示赋值代码和静态代码块代码从上到下执行**
>
>  clinit 方法只调用一次

####　实例初始化过程

> 实例初始化就是执行 init() 方法
>
>  init () 方法可能重载有多个，有几个构造器就有几个 init() 方法
>
>  init() 方法由非静态实例变量显示赋值代码和非静态代码块，对应构造器代码组成
>
>  非静态实例变量显示赋值代码和非静态代码块从上到下顺序执行，而对应构造器的代码最后执行
>
>  每次创建实例对象，调用对应构造器，执行的就是对应的 ini方法
>
>  init 方法的首行是super()和super(实参列表) ,即对应父类的 init 方法

##### Father.java

```java
/**
 * @program: JavaSEInterView
 * @description: 类初始化和实例初始化测试
 * @author: YJC
 * @create: 2020/12/03 11:08
 **/

/**
 * 父类初始化<clinit>
 * 1、j = method()
 * 2、 父类的静态代码块
 *
 * 父类实例化方法:
 * 1、super()（最前）
 * 2、i = test() (9)
 * 3、子类的非静态代码块 (3)
 * 4、子类的无参构造（最后）(2)
 *
 *
 * 非静态方法前面其实有一个默认的对象this
 * this在构造器或<init> 他表示的是正在创建的对象，因为咱们这里是正在创建Son对象，所以
 * test()执行的就是子类重写的代码(面向对象多态)
 *
 * 这里i=test() 执行的就是子类重写的test()方法
 *
 * 1.哪些方法不可以被重写
 * 		final方法
 *		静态方法
 *		private等子类中不可见的方法
 * 2.对象的多态性
 *		子类如果重写了父类的方法，通过子类的对象调用的一定是子类重写过的代码
 *		非静态方法默认的调用对象是this
 *		this对象在构造器或者说<init>方法中就是正在创建的对象
 *
 */
public class Father {
    /*
    *  * 非静态方法前面其实有一个默认的对象this
     * this在构造器或<init> 他表示的是正在创建的对象，因为咱们这里是正在创建Son对象，所以
     * test()执行的就是子类重写的代码(面向对象多态)
    * 
    * */
    private int i = test();//5 调用的是子类重写后的test()方法
    private static int j = method();//1

    static{
        System.out.println("(1)");//2
    }
    Father() {
        System.out.println("(2)");//7
    }
    {
        System.out.println("(3)");//6
    }
    public int test(){
        System.out.println("(4)");
        return 1;
    }
    public static int method() {
        System.out.println("(5)");
        return 1;
    }
}
```

##### Son.java

```java
/**
 * @program: JavaSEInterView
 * @description: 类初始化和实例初始化测试
 * @author: YJC
 * @create: 2020/12/03 11:09
 **/

/**
 * 子类的初始化<clinit>
 * 1、j = method()
 * 2、子类的静态代码块
 *
 * 先初始化父类 (5)(1)
 * 初始化子类 (10) (6)
 *
 * 子类实例化方法:
 * 1、super()（最前
 * 2、i = test() (9)
 * 3、子类的非静态代码块 (8)
 * 4、子类的无参构造（最后）(7)
 */
public class Son extends Father {
    private int i = test();//8
    private static int j = method();//3
    static {
        System.out.println("(6)");//4
    }
    Son() {
        //super(); //写或不写都是存在的，在子类的构造其中一定会调用父类的构造器
        System.out.println("(7)");//10 构造参数是最后执行的
    }
    {
        System.out.println("(8)");//9
    }
    public int test(){
        System.out.println("(9)");
        return 1;
    }
    public static int method() {
        System.out.println("(10)");
        return 1;
    }

    public static void main(String[] args) {
        Son son = new Son();
        System.out.println();
        Son son1 = new Son();
    }
}
```

执行结果

```java
// 类初始化，先父类后子类，静态属性和方法从上到下执行
(5)
(1)
(10)
(6)
// new了一个子类对象，执行一次实例初始化：先父类后子类，非静态属性和方法从上到下执行，构造函数最后执行
(9)
(3)
(2)
(9)
(8)
(7)
// 又new了一个子类对象，再执行一次实例初始化
(9)
(3)
(2)
(9)
(8)
(7)
```

### 5、方法参数传递机制

代码：

```java
package com.atguigu.methodParam;

import java.util.Arrays;

public class Exam4 {
    public static void main(String[] args) {
        int i = 1;
        String str = "hello";
        Integer num = 200;
        int[] arr = {1,2,3,4,5};
        MyData my = new MyData();

        change(i,str,num,arr,my);

        // arr my变了
        System.out.println("i= " + i);
        System.out.println("str= " + str);
        System.out.println("num= " + num);
        System.out.println("arr= " + Arrays.toString(arr));
        System.out.println("my.a= " + my.a);

    }
    public static void change(int j, String s, Integer n, int[] a, MyData m) {
        j += 1;
        s += "world";
        n += 1;
        a[0] += 1;
        m.a += 1;
    }
}
class MyData {
    int a = 10;

}
```

#### 考点？

方法的参数传递机制

String、包装类等对象的不可变性

#### 方法的参数传递机制

1、形参是基本数据类型

- 传递数据值

2、实参是引用数据类型

- 传递地址值

 **特殊的类型：String、包装类等对象的不可变性**

输出结果

```java
i= 1
str= hello
num= 200
arr= [2, 2, 3, 4, 5]
my.a= 11
```

### 6、有n步台阶，一次只能上1步或2步，共有多少种走法？

```markdown
n=1		->一步															f(1)=1
n=2		->1.一步一步 2.直接两步												f(2)=2
n=3		->1.先到达f(1),然后从f(2)跨一步 2.先到达f(2),然后从f(1)跨两步         f(3)=f(1)+f(2)
n=4		->1.先到达f(2),然后从f(2)跨2步 2.先到达f(3),然后从f(3)跨1步          f(4)=f(3)+f(2)
...
n=x		->1.先到达f(x-2),然后从f(x-2)跨2步 2.先到达f(x-1),然后从f(x-1)跨1步          					f(x)=f(x-1)+f(x-2)
```

### 7、成员变量和局部变量

#### 考点？

- 就近原则
- 变量的分类
-  成员变量： 类变量、实例变量
-  局部变量
- 非静态代码块的执行：每次创建实例对象都会执行
- 方法的调用规则：调用一次执行一次

## 局部变量与成员变量区别:

```java
/**
 * @program: JavaSEInterView
 * @description: 成员变量和局部变量
 * @author: YJC
 * @create: 2020/12/03 15:54
 **/
public class Demo2 {
    static int s;// 成员变量，类变量
    int i; // 成员变量，实例变量
    int j;// 成员变量，实例变量
    // 非静态代码块
    {
        int i = 1; // 非静态代码块中局部变量i
        i++; // 就近原则
        j++;
        s++;
    }
    public void test(int j) {//形参，局部变量，j
        j++; // 就近原则 17行的j
        i++; // 就近原则+作用域
        s++;
    }
    public static void main(String[] args){//形参，局部变量，args
        Demo2 obj1 = new Demo2();//局部变量，obj1
        Demo2 obj2 = new Demo2();//局部变量，obj2
        obj1.test(10);
        obj1.test(20);
        obj2.test(30);
        // 2 1 5
        System.out.println(obj1.i + "," + obj1.j + "," + obj1.s);
        // 1 1 5
        System.out.println(obj2.i + "," + obj2.j + "," + obj2.s);
    }
}
```

#### 1、声明的位置

 局部变量：方法体{}中，形参，代码块{}中

 成员变量：类方法外

 类变量： 有static修饰

 实例变量：没有static修饰

#### 2、修饰符

 局部变量：final

 成员变量：public,protected,private,final ,static volatile,transient

#### 3、值存储位置

-  局部变量：栈
-  实例变量：堆
-  类变量：方法区

![image-20201203160418798](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201203160418798.png)

**堆(Heap)** ，此内存区域的唯一目的就是存放对象实例，几乎所有的对象实例都在这里分配内存。这一点在Java虚拟机规范中的描述是:所有的对象实例以及数组都要在堆上分配。

**通常所说的栈(Stack)** ，是指虚拟机栈。虚拟机栈用于存储局部变量表等。局部变量
表存放了编译期可知长度的各种基本数据类型(boolean、byte、 char、short、 int、 float、long、double) 、对象引用(reference 类型，它不等同于对象本身，是对象在堆内存的首地址)。方法执行完， 自动释放。

**方法区(Method Area)**用于存储已被虛拟机加载的类信息、常量、~~静态变量~~、即时编译器编译后的代码等数据。

#### 4、作用域：

**局部变量**：从声明处开始，到所属的 } 好结束

**实例变量**：在当前类中 this 有时this. 可以省略,在其他类中 对象名. 访问

**类变量**：在当前类中 类名 有时类名. 可以省略，在其它类中类名.或对象名.访问

#### 5、生命周期

**局部变量**：每一个线程，每一次调用执行都是新的生命周期

**实例变量**：随着对象的创建而初始化，随着对象的被回收而消亡，每一个对象的实例变量都是独立的

**类变量**：随着类的初始化而初始化，随着类的卸载而消亡，该类的所有对象的类变量是共享的

当局部变量与XX变量重名时，如何区分：

1、局部变量与实例变量重名

-  在成员便令前面加 this

2、局部变量与类变量重名

-  在类变量前面加 类名

## SSM

### 1、Bean的作用域

在Spring中，可以在\<bean>元素的scope中属性里设置Bean的作用域，默认为singleton单实例的。

| 类型      | 说明                                                         |
| :-------- | ------------------------------------------------------------ |
| singleton | 在SpringIOC容器中仅存在一个Bean实例，Bean以单实例的方式存在  |
| prototype | 每次调用getBean()都会返回一个新的实例                        |
| request   | 每次Http请求都会创建一个新的Bean，该作用域仅适用于WebApplicationContext环境 |
| Session   | 同一个HTTP Session共享一个Bean，不同的Http Session使用不同的Bean，该作用域仅适用于WebApplicationContext环境 |

### Spring中支持的常用数据库事务传播属性和事务隔离级别

#### 1 事务的传播行为

#### 1.1 简介

当事务方法被另一个事务方法调用时，必须指定事务应该如何传播，列如方法可能继续在现有事务中运行，也可能开启一个新事务，并在自己的事务中运行，事务传播的行为有传播属性指定，Spring定义了7中类传播行为

| 传播属性           | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| **REQUIRED**(默认) | 如果有事务在运行，当前的方法就在这个事务内运行，否则就启动一个新的事务，并在自己的事务内运行<br>（在一个事物内运行） |
| REQUIRED_NEW       | 当前方法必须启动事务，并在它自己的事务内运行，如果有事务正在运行，应该将他挂起<br>（开启新的事务） |
| SUPPORTS           | 如果有事务在运行，当前的方法就在这个事务内运行，否则他可以不运行在事务中 |
| NOT_SUPPORTE       | 当前的方法不应该运行在事务中，如果有运行的事务，将他挂起     |
| MANDATORY          | 当前的方法必须运行在事务内部，如果没有正在运行的事务，就抛出异常 |
| NEVER              | 当前方法不应该运行在事务中，如果有运行的事务，就抛出异常     |
| NESTED             | 如果有事务在运行，当前的方法就应该在这个事物的嵌套事务内运行，否则，就启动一个新的事务，并在它自己的事务内运行 |

事务传播属性可以在@Transactional注解的propagation属性中定义

### 2 事务隔离级别

#### 2.1 数据库事务并发问题

 假设现在有两个事务：Transaction01和Transaction02并发执行。

##### 1) 脏读：当前事务读取到了其它事务更新还没有提交的值

 ①Transaction01将某条记录的AGE值从20修改为30。

 ②Transaction02读取了Transaction01更新后的值：30。

 ③Transaction01回滚，AGE值恢复到了20。

 ④Transaction02读取到的30就是一个无效的值。

##### 2) 不可重复读：当前事务读两次读取到的值不一致

 ①Transaction01读取了AGE值为20。

 ②Transaction02将AGE值修改为30。

 ③Transaction01再次读取AGE值为30，和第一次读取不一致。

##### 3) 幻读

 ①Transaction01读取了STUDENT表中的一部分数据。

 ②Transaction02向STUDENT表中插入了新的行。

 ③Transaction01读取了STUDENT表时，多出了一些行。

#### 2.2 隔离级别

数据库系统必须具有隔离并发运行各个事务的能力，使它们不会相互影响，避免各种并发问题。**一个事务与其他事务隔离的程度称为隔离级别**。SQL标准中规定了多种事务隔离级别，不同隔离级别对应不同的干扰程度，隔离级别越高，数据一致性就越好，但并发性越弱。

1. **读未提交**：READ UNCOMMITTED

允许Transaction01读取Transaction02未提交的修改。

1. **读已提交**：READ COMMITTED

 要求Transaction01只能读取Transaction02已提交的修改。

1. **可重复读**：REPEATABLE READ

 确保Transaction01可以多次从一个字段中读取到相同的值，即Transaction01执行期间禁止其它事务对这个字段进行更新。

1. **串行化**：SERIALIZABLE

 确保Transaction01可以多次从一个表中读取到相同的行，在Transaction01执行期间，禁止其它事务对这个表进行添加、更新、删除操作。可以避免任何并发问题，但性能十分低下。

1. **各个隔离级别解决并发问题的能力见下表**

|                  | 脏读 | 不可重复读 | 幻读 |
| ---------------- | ---- | ---------- | ---- |
| READ UNCOMMITTED | 有   | 有         | 有   |
| READ COMMITTED   | 无   | 有         | 有   |
| REPEATABLE READ  | 无   | 有         | 有   |
| SERIALIZABLE     | 无   | 无         | 无   |

各种数据库产品对事务隔离级别的支持程度：

|                  | Oracle     | MySql      |
| ---------------- | ---------- | ---------- |
| READ UNCOMMITTED | 无         | 有         |
| READ COMMITTED   | 有（默认） | 有         |
| REPEATABLE READ  | 无         | 有（默认） |
| SERIALIZABLE     | 有         | 有         |

```
//1.请简单介绍Spring支持的常用数据库事务传播属性和事务隔离级别？

	/**
	 * 事务的属性：
	 * 	1.★propagation：用来设置事务的传播行为
	 * 		事务的传播行为：一个方法运行在了一个开启了事务的方法中时，当前方法是使用原来的事务还是开启一个新的事务
	 * 		-Propagation.REQUIRED：默认值，使用原来的事务
	 * 		-Propagation.REQUIRES_NEW：将原来的事务挂起，开启一个新的事务
	 * 	2.★isolation：用来设置事务的隔离级别
	 * 		-Isolation.REPEATABLE_READ：可重复读，MySQL默认的隔离级别
	 * 		-Isolation.READ_COMMITTED：读已提交，Oracle默认的隔离级别，开发时通常使用的隔离级别
	 */
```

### SpringMVC如何解决乱码问题？

[springmvc字符编码过滤器CharacterEncodingFilter浅析](https://blog.csdn.net/lianjunzongsiling/article/details/77926370)

#### **一、在web.xml中的配置**

```xml
<!-- characterEncodingFilter字符编码过滤器 -->
<filter>
	<filter-name>characterEncodingFilter</filter-name>
	<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
	<init-param>
		<!--要使用的字符集，一般我们使用UTF-8(保险起见UTF-8最好)-->
		<param-name>encoding</param-name>
		<param-value>UTF-8</param-value>
	</init-param>
	<init-param>
		<!--是否强制设置request的编码为encoding，默认false，不建议更改-->
		<param-name>forceRequestEncoding</param-name>
		<param-value>false</param-value>
	</init-param>
	<init-param>
		<!--是否强制设置response的编码为encoding，建议设置为true，下面有关于这个参数的解释-->
		<param-name>forceResponseEncoding</param-name>
		<param-value>true</param-value>
	</init-param>
</filter>
<filter-mapping>
	<filter-name>characterEncodingFilter</filter-name>
	<!--这里不能留空或者直接写 ' / ' ，否者不起作用-->
	<url-pattern>/*</url-pattern>
</filter-mapping>
```
#### **二、CharacterEncodingFilter过滤器类浅析**

打开该类源码，可以看到该类有三个类属性

```java
private String encoding; //要使用的字符集，一般我们使用UTF-8(保险起见UTF-8最好)
private boolean forceRequestEncoding = false; //是否强制设置request的编码为encoding
private boolean forceResponseEncoding = false; //是否强制设置response的编码为encoding
```

主要方法只有一个，也就是下面这个，代码逻辑很简单，如注释所解释

```java
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        String encoding = getEncoding();
        if (encoding != null) { //如果设置了encoding的值，则根据情况设置request和response的编码
	        //若设置request强制编码或request本身就没有设置编码
	        //则设置编码为encoding表示的值
            if (isForceRequestEncoding() || request.getCharacterEncoding() == null) { 
                request.setCharacterEncoding(encoding);
            }
	        //若设置response强制编码，则设置编码为encoding表示的值
            if (isForceResponseEncoding()) { //请注意这行代码，下面有额外提醒
                response.setCharacterEncoding(encoding);
            }
        }
        filterChain.doFilter(request, response);
    }

```

##### 额外提醒

```java
if (isForceResponseEncoding()) { 
	response.setCharacterEncoding(encoding);
}
```

是在

```java
filterChain.doFilter(request, response);
```

之前执行的，这也就是说这段代码的作用是设置response的默认编码方式，在之后的代码里是可以根据需求设置为其他编码的，即这里设置的编码可能不是最终的编码，网上很多文档说这里设置的是最终的编码方式，这是错的。

### SpringMVC工作流程

#### 整体流程

SpringMVC框架是一个基于请求驱动的Web框架，并且使用了‘前端控制器’模型来进行设计，再根据‘请求映射规则’分发给相应的页面控制器进行处理

![image-20201204093201811](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204093201811.png)



文章参考：https://www.cnblogs.com/leskang/p/6101368.html

#### 1、整体流程

![img](https://gitee.com/junchuangyang/blog-img/raw/master/img/791227-20161125140123503-1552603846.png)

具体步骤：

1、 首先用户发送请求到前端控制器，前端控制器根据请求信息（如 URL）来决定选择哪一个页面控制器进行处理并把请求委托给它，即以前的控制器的控制逻辑部分；图中的 1、2 步骤；

2、 页面控制器接收到请求后，进行功能处理，首先需要收集和绑定请求参数到一个对象，这个对象在 Spring Web MVC 中叫命令对象，并进行验证，然后将命令对象委托给业务对象进行处理；处理完毕后返回一个 ModelAndView（模型数据和逻辑视图名）；图中的 3、4、5 步骤；

3、 前端控制器收回控制权，然后根据返回的逻辑视图名，选择相应的视图进行渲染，并把模型数据传入以便视图渲染；图中的步骤 6、7；

4、 前端控制器再次收回控制权，将响应返回给用户，图中的步骤 8；至此整个结束。

#### 2、核心流程

![img](https://gitee.com/junchuangyang/blog-img/raw/master/img/791227-20161125140338768-995727439.png)

具体步骤：

第一步：发起请求到前端控制器(DispatcherServlet)

第二步：前端控制器请求HandlerMapping查找 Handler （可以根据xml配置、注解进行查找）

第三步：处理器映射器HandlerMapping向前端控制器返回Handler，HandlerMapping会把请求映射为HandlerExecutionChain对象（包含一个Handler处理器（页面控制器）对象，多个HandlerInterceptor拦截器对象），通过这种策略模式，很容易添加新的映射策略

第四步：前端控制器调用处理器适配器去执行Handler

第五步：处理器适配器HandlerAdapter将会根据适配的结果去执行Handler

第六步：Handler执行完成给适配器返回ModelAndView

第七步：处理器适配器向前端控制器返回ModelAndView （ModelAndView是springmvc框架的一个底层对象，包括 Model和view）

第八步：前端控制器请求视图解析器去进行视图解析 （根据逻辑视图名解析成真正的视图(jsp)），通过这种策略很容易更换其他视图技术，只需要更改视图解析器即可

第九步：视图解析器向前端控制器返回View

第十步：前端控制器进行视图渲染 （视图渲染将模型数据(在ModelAndView对象中)填充到request域）

第十一步：前端控制器向用户响应结果

#### **总结 核心开发步骤**

1、 DispatcherServlet 在 web.xml 中的部署描述，从而拦截请求到 Spring Web MVC

2、 HandlerMapping 的配置，从而将请求映射到处理器

3、 HandlerAdapter 的配置，从而支持多种类型的处理器

注：处理器映射求和适配器使用纾解的话包含在了注解驱动中，不需要在单独配置

4、 ViewResolver 的配置，从而将逻辑视图名解析为具体视图技术

5、 处理器（页面控制器）的配置，从而进行功能处理 

View是一个接口，实现类支持不同的View类型（jsp、freemarker、pdf...）

### Mybatis中当实体类中的属性名和表中的字段不一样，怎么办？

解决方案：

1、写 SQL 语句的时候 写别名

2、在MyBatis的全局配置文件中开启驼峰命名规则

```xml
<!-- 开启驼峰命名规则，可以将数据库中下划线映射为驼峰命名
	列如 last_name 可以映射为 lastName
-->
<setting name="mapUnderscoreToCameLCase" value="true" />

```

要求 数据库字段中含有下划线

3、在Mapper映射文件中使用 resultMap 自定义映射

```xml
<!-- 
	自定义映射
-->
<resultMap type="com.atguigu.pojo.Employee" id="myMap">
    <!-- 映射主键 -->
	<id cloumn="id" property="id"/>
    <!-- 映射其他列 -->
    <result column="last_name" property="lastName" />
    <result column="email" property="email" />
    <result column="salary" property="salary" />
    <result column="dept_id" property="deptId" />
</resultMap>

```

## Java高级

#### git分支相关命令、实际引用

##### 分支

> 创建分支

git branch <分支名>

git branch -v 查看分支

> 切换分支

git checkout <分支名>

一步完成: git checkout -b <分支名>

> 合并分支

先切换到主干 git checkout master

git merge <分支名>

> 删除分支

先切换到主干 git checkout master

git branch -D <分支名>



## redis持久化有几种类型，他们的区别

#### Redis 提供了 2 个不同形式的持久化方式

RDB ( Redis DataBase)

AOF (Append OF File)

### RDB

在指定的时间间隔内将内存中的数据集快照写入磁盘，也就是行话讲的Snapshot快照，它恢复时是将快照文件直接读到内存里。

> 备份是如何执行的

Redis会单独创建(fork) 一个子进程来进行持款化，先将数据写入到一个临时文件中，待持久化过程都结束了,再用这个临时文件替换上次持久化好的文件。整个过程中，主进程是不进行任何I0操作的,这就确保了极高的性能如果需要进行大规模数据的恢复，对于数据恢复的完整性不是非常敏感，那RDB方式要比AOF方式更加的高效。RDB的缺点是最后一次持久化后的数据可能丢失。

rdb 的保存文件

在 redis.conf 中配置文件名称 默认为 dump.rdb

![在这里插入图片描述](https://gitee.com/junchuangyang/blog-img/raw/master/img/20201014105538134.png)
rbd 文件的保存路径，也可以修改，默认为 Redis启动命令行所在目录下

![在这里插入图片描述](https://gitee.com/junchuangyang/blog-img/raw/master/img/20201014105538134.png)

> rdb 的备份

- 先通过 config get dir 查询 rdb文件的目录
- 将 *.rdb 的文件拷贝到别的地方

> rdb 的恢复

- 关闭 Redis
- 先把备份文件拷贝到拷贝到工作目录下
- 启动 Redis，备份数据会直接加载

![在这里插入图片描述](https://gitee.com/junchuangyang/blog-img/raw/master/img/20201014105558306.png)

> rdb 的优点

- 节省磁盘空间
- 恢复速度快

> rdb 的缺点

- 虽然Redis在fork时使用了写时拷贝技术,但是如果数据庞大时还是比较消耗性能。
- 在备份周期在一定间隔时间做一次备份, 所以如果Redis意外down掉的话，就会丢失最后一次快照后的所有修改。

### AOF

以日志的形式来记录每个写操作，**将Redis执行过的所有写指令记录下来(读操作不记录)**，只许追加文件但不可以改写文件，Redis启动之初会读取该文件重新构建数据，换言之，Redis重启的话就根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作。

> Rewrite

AOF采文件追加方式，文件会越来越大为避免出现此种情况,新增了重写机制**,当AOF文件的大小超过所设定的阈值时,Redis就会启动AOF文件的内容压缩**，只保留可以恢复数据的最小指令集，可以使用命令bgrewriteaof.

> Redis 如何实现重写？

AOF文件持续增长而过大时，会fork出一条新进程来将文件写(也是先写临时文件最后再rename)，遍历新进程的内存中数据，条记录有一条的Set语句。 写af文件的操作，并没有读取旧的aof文件，将整个内存中的数据库内容用命令的方式写了一个新的aof文件, 这点和快照有点类似。

> 何时重写

写虽然可以节约大量磁盘空间,减少恢复时间。但是每次重写还是有一定的负担的，因此设定Redis要满足一条件才会进行重写。

```
auto- aof- rewrite- percentage 100
auto- aof- rewrite-min-size 64mb
```

系统载入时或者上次重写完毕时, Redis会记录此时AOF大小,设为 base size ,如果Redis的AOF当前大小 >= base size + base_ size* 100% (默认)且当前大小 >=64mb (默认)的情况下， Redis会对AOF进行重写。

> AOF 的优点

- 备份机制更稳健，丢失数据概率更低。
- 可读的日志文本，通过操作AOF稳健，可以处理误操作。

![在这里插入图片描述](https://gitee.com/junchuangyang/blog-img/raw/master/img/20201014105612781.png)

> AOF的缺点

- 比起RDB占用更多的磁盘空间。
- 恢复备份速度要慢。
- 每次读写都同步的话，有一定的性能压力。
- 存在个别Bug，造成不能恢复。

## Mysql什么时候建索引、什么时候不适合建索引

![image-20201204103411660](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204103411660.png)



### 哪些情况需要创建索引

![image-20201204103647610](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204103647610.png)

1. 主键自动建立唯 一 索引
2. 频繁作为查询条件的字段应该创建索引
3. 查询中与其它表关联的字段，外键关系建立索引
4. 频繁更新的字段不适合创建索引，因为每次更新不单是更新了记录还会更新索引
5. 单键组索引的选择问题：在高并发下优先后创建组合索引
6. 查询中排序的字段，排序字段若通过索引法访问将大大提高排序速度
7. 查询中统计或者分组字段

### 哪些情况下不要建立索引

![image-20201204103659120](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204103659120.png)

1. 表记录太少
   1. Why:提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE.
2. 经常增删改的表
   1. 因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件数据重复且分布平均的表字段，因此应该只为最经常查询和最经常排序的数据列建立索引。
3. 注意，如果某个数据列包含许多重复的内容，为它建立索引就没有太大的实际效果。

## JVM垃圾回收机制、GC发生在JVM哪部分，有几种GC，他们的算法是什么？

![image-20201204104953662](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104953662.png)

GC 发生在JVM的堆里面。

![image-20201204103950117](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204103950117.png)

#### 引用计数法(淘汰)

![image-20201204104033751](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104033751.png)

#### 复制算法(发生在年轻代)

![image-20201204104139162](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104139162.png)

优点和缺点：

![image-20201204104253164](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104253164.png)

#### 标记清除（老年代）

![image-20201204104344636](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104344636.png)

优缺点：

![image-20201204104545644](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104545644.png)

#### 标记压缩（老年代）

![image-20201204104713583](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104713583.png)

#### 标记清除压缩

![image-20201204104845732](https://gitee.com/junchuangyang/blog-img/raw/master/img/image-20201204104845732.png)

## redis 在项目中的使用场景

| 数据类型 | 使用场景                                                     |
| -------- | ------------------------------------------------------------ |
| String   | 比如说，我想知道什么时候封锁一个 IP 地址 Incrby 命令         |
| Hash     | 存储用户信息[ id, name , age] <br>Hset( key ,field, value) <br/>Hset( key ,id, 101)<br/>Hset( key ,name, admin) <br/>Hset( key ,age, 23)<br/>修改案例--------- <br/>Hget(userKev,id) + Hset(userKey,id,102) <br/>为什么不使用String类型来存储 ?<br/>Set(userKey,用户信息字符串)<br/>get(userKey)<br/>String拿到对象值之后需要反序列化，我们只需要更改id <br/>name, age 没有意义， 不建议使用String 类型。 |
| List     | 实现最新消息的排行，还可以利用 List 的 push 命令，将任务存在list集合 中。同时使用另一个命令，将任务从集合中取出[ pop ]。<br/> Redis - List 数据类型来模拟消息队列。<br/>[电商中的秒杀就可以采用这种方式 来完成一个秒杀活动]。 |
| Set      | 特殊之处:可以自动排重。<br/>比如说微博中将每个人的好友存在集合(Set) 中， 这样求两个人的共通好友的操作。我们只需要求交集即可。 |
| Zset     | 以某一个条件为权重，进行排序。<br/>京东:商品详情的时候，都会有一个综合排名，还可以按照价格进行排名 |

## 单点登录

单点登录: 一处登录多处使用！

前提：**单点登录多使用在分布式系统中**

一处登录，处处运行

![在这里插入图片描述](https://gitee.com/junchuangyang/blog-img/raw/master/img/20201014110632902.png)

京东：单点登录，是将 token 放入到 cookie 中

案例：**将浏览器的 cookie 禁用，则在登录京东则失效，无论如何登录不了**

## 购物车实现过程

购物车：

 **1、购物车跟用户的关系 ？**

​		 a）一个用户必须对应一个购物车【一个用户不管买多少商品，都会存在属于自己的购物车中】

​		 b）单点登录一定要在购物车前

 **2、跟购物车有关的操作有那些？**

1. 添加购物车

   - 用户未登录状态

     -  添加到什么地方，未登录将数据保存到什么地方？
       - redis？ ---京东
       - Cookie?  ---Cookie 自己开发项目的时候【如果浏览器禁用Cookie】

   - 用户登录状态

     -  Redis 缓存中 【读写速度快】:存储在Hash中

       Hash: Hset(key,field,value)

       - Key: user:userId:cart

       - Hset(key,skuId,value)

     - 存在数据库中 【Oracle，mysql】

2. 展示购物车

   - 未登录状态

     - 显示直接从 cookie 中 取得数据展示即可

   - 登录状态

     - 用户一旦登录，必须显示数据库【redis】 + cookie 中的购物车的数据

        Cookie 中有三条记录+Redis 中有五条记录=真正展示的时候应该是八条记录