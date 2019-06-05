# StringBuffer类概述及其构造方法

l  StringBuffer类概述

•     我们如果对字符串进行拼接操作，每次拼接，都会构建一个新的String对象，既耗时，又浪费空间。而

StringBuffer就可以解决这个问题

•     线程安全的可变字符序列

l  StringBuffer和String的区别?

l  构造方法

•     public StringBuffer() 

•     public StringBuffer(int capacity)

•     public StringBuffer(String str)

# StringBuffer类的成员方法

l  添加功能

•     public StringBuffer append(String str)

•     public StringBuffer insert(int offset,String str)

l  删除功能

•     public StringBuffer deleteCharAt(int index)

•     public StringBuffer delete(int start,int end)

l  替换功能

•     public StringBuffer replace(int start,int end,String str)

l  反转功能 public StringBuffer reverse()

# StringBuffer类的成员方法

l  截取功能

•     public String substring(int start)

•     public String substring(int start,int end)

l  截取功能和前面几个功能的不同

•     返回值类型是String类型，本身没有发生改变

# StringBuffer类练习

l  String和StringBuffer的相互转换

l  把数组拼接成一个字符串

l  把字符串反转

l  判断一个字符串是否是对称字符串

• 例如"abc"不是对称字符串，"aba"、"abba"、"aaa" 、"mnanm"是对称字符串

# StringBuffer类面试题

l  通过查看API了解一下StringBuilder类

l  String,StringBuffer,StringBuilder的区别

l  StringBuffer和数组的区别

l  看程序写结果：

•     String作为参数传递

•     StringBuffer作为参数传递

## 数组高级**(**排序和查找**)**

l  排序

•     冒泡排序

•     相邻元素两两比较，大的往后放，第一次完毕，最大值出现在了最大索引处

•     选择排序

•     从0索引开始，依次和后面元素比较，小的往前放，第一次完毕，最小值出现在了最小索引处

l  查找

•     基本查找 数组元素无序

•     二分查找 数组元素有序

## 数组高级练习题

l 把字符串中的字符进行排序。

•     举例：”dacgebf”

•     结果：”abcdefg”

## **Arrays**类概述及其常用方法

l  Arrays类概述

•     针对数组进行操作的工具类。

•     提供了排序，查找等功能。

l  成员方法

•     public static String toString(int[] a)

•     public static void sort(int[] a)

•     public static int binarySearch(int[] a,int key)

## **Arrays**类常用方法源码详细解释

l  public static String toString(int[] a) 源码解析

l  public static int binarySearch(int[] a,int key) 源码解析

## 基本类型包装类概述

l  将基本数据类型封装成对象的好处在于可以在对象中定义更多的功能方法操作该数据。

l  常用的操作之一：用于基本数据类型与字符串之间的转换。

l  基本类型和包装类的对应

• Byte,Short,Integer,Long,Float,Double

Character,Boolean

## **Integer**类概述及其构造方法

l Integer类概述

•   Integer 类在对象中包装了一个基本类型 int 的值

•   该类提供了多个方法，能在 int 类型和 String 类型之间互相转换，还提供了处理 int 类型时非常有用的其他一些常量和方法 l 构造方法

•   public Integer(int value)

•   public Integer(String s)

# Integer类成员方法

l  int类型和String类型的相互转换

• int – String • String – int

l  public int intValue()

l  public static int parseInt(String s)

l  public static String toString(int i)

l  public static Integer valueOf(int i)

l  public static Integer valueOf(String s)

# Integer类成员方法

l  常用的基本进制转换

•     public static String toBinaryString(int i)

•     public static String toOctalString(int i)

•     public static String toHexString(int i)

l  十进制到其他进制

•     public static String toString(int i,int radix)

l  其他进制到十进制

•     public static int parseInt(String s,int radix)

# JDK5的新特性

l JDK1.5以后，简化了定义方式。

•    Integer x = new Integer(4);可以直接写成

•    Integer x = 4;//自动装箱。

•    x  = x + 5;//自动拆箱。通过intValue方法。

l需要注意：

•在使用时，Integer  x = null;上面的代码就会出现NullPointerException。

# Integer的面试题

l  Integer i = 1; i += 1;做了哪些事情

l  缓冲池(看程序写结果)

• 通过查看源码知道为什么

# Character类概述及其构造方法

l  Character类概述

•     Character 类在对象中包装一个基本类型 char 的值

•     此外，该类提供了几种方法，以确定字符的类别（小写字母，数字，等等），并将字符从大写转换成小写

，反之亦然

l  构造方法

•     public Character(char value)

# Character类成员方法

l  public static boolean isUpperCase(char ch)

l  public static boolean isLowerCase(char ch)

l  public static boolean isDigit(char ch)

l  public static char toUpperCase(char ch) l public static char toLowerCase(char ch)

## 正则表达式概述及基本使用

l  正则表达式：是指一个用来描述或者匹配一系列符合某个句法规则的字符串的单个字符串。

其实就是一种规则。有自己特殊的应用。

l  举例：校验qq号码.

1:要求必须是5-15位数字

2:0不能开头

## 正则表达式的组成规则

l  规则字符在java.util.regex Pattern类中

l  常见组成规则

•     字符

•     字符类

•     预定义字符类

•     边界匹配器

•     数量词

## 正则表达式的应用

l  判断功能

•     public boolean matches(String regex)

l  分割功能

•     public String[] split(String regex)

l  替换功能

•     public String replaceAll(String regex,String replacement)

l  获取功能

•     Pattern和Matcher类的使用

## 正则表达式的练习

l  判断功能：

•     校验邮箱

l  分割功能：

•     我有如下一个字符串:”91 27 46 38 50”

•     请写代码实现最终输出结果是：”27 38 46 50 91”

l  替换功能：

•     论坛中不能出现数字字符，用*替换

l  获取功能：

•     获取由三个字符组成的单词

## **Math**类概述及其成员方法

l  Math类概述

•     Math 类包含用于执行基本数学运算的方法，如初等指数、对数、平方根和三角函数。

l  成员方法

•     public static int abs(int a)

•     public static double ceil(double a)

•     public static double floor(double a)

•     public static int max(int a,int b) min自学

•     public static double pow(double a,double b)

•     public static double random()

•     public static int round(float a) 参数为double的自学

•     public static double sqrt(double a)

## **Random**类概述及其构造方法

l  Random类概述

•     此类用于产生随机数

•     如果用相同的种子创建两个 Random 实例，则对每个实例进行相同的方法调用序列，它们将生成并返回相同的数字序列。

l  构造方法

•     public Random()

•     public Random(long seed)

# Random类成员方法

l  public int nextInt()

l  public int nextInt(int n)

## **System**类概述及其成员方法

l  System类概述

•     System 类包含一些有用的类字段和方法。它不能被实例化。

l  成员方法

•     public static void gc()

•     public static void exit(int status)

•     public static long currentTimeMillis()

•     public static void arraycopy(Object src,int srcPos,Object dest,int destPos,int length)

# BigInteger类概述及其构造方法

l  BigInteger类概述

•     可以让超过Integer范围内的数据进行运算

l  构造方法

•     public BigInteger(String val)

# BigInteger类成员方法

l   public BigInteger add(BigInteger val)

l   public BigInteger subtract(BigInteger val)

l   public BigInteger multiply(BigInteger val)

l   public BigInteger divide(BigInteger val)

l   public BigInteger[] divideAndRemainder(BigInteger val)

# BigDecimal类概述及其构造方法

l  由于在运算的时候，float类型和double很容易丢失精度，演示案例。所以，为了能精确的表示、计算浮点数，Java提供了BigDecimal

l  BigDecimal类概述

•     不可变的、任意精度的有符号十进制数。

l  构造方法

•     public BigDecimal(String val)

# BigDecimal类成员方法

l   public BigDecimal add(BigDecimal augend)

l   public BigDecimal subtract(BigDecimal subtrahend)

l   public BigDecimal multiply(BigDecimal multiplicand)

l   public BigDecimal divide(BigDecimal divisor)

l   public BigDecimal divide(BigDecimal divisor,int scale, int roundingMode)

## **Date**类概述及其方法

l  Date类概述

•     类 Date 表示特定的瞬间，精确到毫秒。

l  构造方法

•     public Date()

•     public Date(long date)

l  成员方法

•     public long getTime()

•     public void setTime(long time)

# DateFormat类概述及其方法

l  DateFormat类概述

•     DateFormat 是日期/时间格式化子类的抽象类，它以与语言无关的方式格式化并解析日期或时间。

•     是抽象类，所以使用其子类SimpleDateFormat

l  SimpleDateFormat构造方法

•     public SimpleDateFormat()

•     public SimpleDateFormat(String pattern)

l  成员方法

•     public final String format(Date date)

•     public Date parse(String source)

# Date类及DateFormat类练习

l  制作一个工具类。DateUtil

l  算一下你来到这个世界多少天?

# Calendar类概述及其方法

l  Calendar类概述

•     Calendar 类是一个抽象类，它为特定瞬间与一组诸如 YEAR、MONTH、DAY_OF_MONTH、HOUR 等日历字段之间的转换提供了一些方法，并为操作日历字段（例如获得下星期的日期）提供了一些方法。

l  成员方法

•     public static Calendar getInstance()

•     public int get(int field)

•     public void add(int field,int amount)

•     public final void set(int year,int month,int date)

# Calendar类练习

l  算一下你来到这个世界多少天?

l  获取任意一年的二月有多少天