# 总结
```java
1:StringBuffer(掌握)
	(1)用字符串做拼接，比较耗时并且也耗内存，而这种拼接操作又是比较常见的，为了解决这个问题，Java就提供了
	   一个字符串缓冲区类。StringBuffer供我们使用。
	(2)StringBuffer的构造方法
		A:StringBuffer()
		B:StringBuffer(int size)
		C:StringBuffer(String str)
	(3)StringBuffer的常见功能(自己补齐方法的声明和方法的解释)
		A:添加功能
		B:删除功能
		C:替换功能
		D:反转功能
		E:截取功能(注意这个返回值)
	(4)StringBuffer的练习(做一遍)
		A:String和StringBuffer相互转换
			String -- StringBuffer
				构造方法
			StringBuffer -- String
				toString()方法
		B:字符串的拼接
		C:把字符串反转
		D:判断一个字符串是否对称
	(5)面试题
		小细节：
			StringBuffer：同步的，数据安全，效率低。
			StringBuilder：不同步的，数据不安全，效率高。
		A:String,StringBuffer,StringBuilder的区别
		B:StringBuffer和数组的区别?
	(6)注意的问题：
		String作为形式参数，StringBuffer作为形式参数。
	
2:数组高级以及Arrays(掌握)
	(1)排序
		A:冒泡排序
			相邻元素两两比较，大的往后放，第一次完毕，最大值出现在了最大索引处。同理，其他的元素就可以排好。
			
			public static void bubbleSort(int[] arr) {
				for(int x=0; x<arr.length-1; x++) {
					for(int y=0; y<arr.length-1-x; y++) {
						if(arr[y] > arr[y+1]) {
							int temp = arr[y];
							arr[y] = arr[y+1];
							arr[y+1] = temp;
						}
					}
				}
			}
			
		B:选择排序
			把0索引的元素，和索引1以后的元素都进行比较，第一次完毕，最小值出现在了0索引。同理，其他的元素就可以排好。
			
			public static void selectSort(int[] arr) {
				for(int x=0; x<arr.length-1; x++) {
					for(int y=x+1; y<arr.length; y++) {
						if(arr[y] < arr[x]) {
							int temp = arr[x];
							arr[x] = arr[y];
							arr[y] = temp;
						}
					}
				}
			}
	(2)查找
		A:基本查找
			针对数组无序的情况
			
			public static int getIndex(int[] arr,int value) {
				int index = -1;
				
				for(int x=0; x<arr.length; x++) {
					if(arr[x] == value) {
						index = x;
						break;
					}
				}
				
				return index;
			}
		B:二分查找(折半查找)
			针对数组有序的情况(千万不要先排序，在查找)
			
			public static int binarySearch(int[] arr,int value) {
				int min = 0;
				int max = arr.length-1;
				int mid = (min+max)/2;
				
				while(arr[mid] != value) {
					if(arr[mid] > value) {
						max = mid - 1;
					}else if(arr[mid] < value) {
						min = mid + 1;
					}
					
					if(min > max) {
						return -1;
					}
					
					mid = (min+max)/2;
				}
				
				return mid;
			}
	(3)Arrays工具类
		A:是针对数组进行操作的工具类。包括排序和查找等功能。
		B:要掌握的方法(自己补齐方法)
			把数组转成字符串：
			排序：
			二分查找：
	(4)Arrays工具类的源码解析
	(5)把字符串中的字符进行排序
		举例：
			"edacbgf"
			得到结果
			"abcdefg"

3:Integer(掌握)
	(1)为了让基本类型的数据进行更多的操作，Java就为每种基本类型提供了对应的包装类类型
		byte 		Byte
		short		Short
		int			Integer
		long		Long
		float		Float
		double		Double
		char		Character
		boolean		Boolean
	(2)Integer的构造方法
		A:Integer i = new Integer(100);
		B:Integer i = new Integer("100");
			注意：这里的字符串必须是由数字字符组成
	(3)String和int的相互转换
		A:String -- int
			Integer.parseInt("100");
		B:int -- String
			String.valueOf(100);
	(4)其他的功能(了解)
		进制转换
	(5)JDK5的新特性
		自动装箱	基本类型--引用类型
		自动拆箱	引用类型--基本类型
		
		把下面的这个代码理解即可：
			Integer i = 100;
			i += 200;
	(6)面试题
		-128到127之间的数据缓冲池问题

4:Character(了解)
	(1)Character构造方法	
		Character ch = new Character('a');
	(2)要掌握的方法：(自己补齐)
		A:判断给定的字符是否是大写
		B:判断给定的字符是否是小写
		C:判断给定的字符是否是数字字符
		D:把给定的字符转成大写
		E:把给定的字符转成小写
	(3)案例：
		统计字符串中大写，小写及数字字符出现的次数

```

# StringBuffer类概述及其构造方法

- StringBuffer类概述
- 我们如果对字符串进行拼接操作，每次拼接，都会构建一个新的String对象，既耗时，又浪费空间。而
  StringBuffer就可以解决这个问题

- 线程安全的可变字符序列

-  StringBuffer和String的区别?

-  构造方法

    •     public StringBuffer() 

    •     public StringBuffer(int capacity)

    •     public StringBuffer(String str)
实例:
```java
package cn.itcast_01;

/*
 * 线程安全(多线程讲解)
 * 安全 -- 同步 -- 数据是安全的
 * 不安全 -- 不同步 -- 效率高一些
 * 安全和效率问题是永远困扰我们的问题。
 * 安全：医院的网站，银行网站
 * 效率：新闻网站，论坛之类的
 * 
 * StringBuffer:
 * 		线程安全的可变字符串。
 * 
 * StringBuffer和String的区别?
 * 前者长度和内容可变，后者不可变。
 * 如果使用前者做字符串的拼接，不会浪费太多的资源。
 * 
 * StringBuffer的构造方法：
 * 		public StringBuffer():无参构造方法
 *		public StringBuffer(int capacity):指定容量的字符串缓冲区对象
 *		public StringBuffer(String str):指定字符串内容的字符串缓冲区对象
 *
 * StringBuffer的方法：
 *		public int capacity()：返回当前容量。	理论值
 *		public int length():返回长度（字符数）。 实际值
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		// public StringBuffer():无参构造方法
		StringBuffer sb = new StringBuffer();
		System.out.println("sb:" + sb);
		System.out.println("sb.capacity():" + sb.capacity());
		System.out.println("sb.length():" + sb.length());
		System.out.println("--------------------------");

		// public StringBuffer(int capacity):指定容量的字符串缓冲区对象
		StringBuffer sb2 = new StringBuffer(50);
		System.out.println("sb2:" + sb2);
		System.out.println("sb2.capacity():" + sb2.capacity());
		System.out.println("sb2.length():" + sb2.length());
		System.out.println("--------------------------");

		// public StringBuffer(String str):指定字符串内容的字符串缓冲区对象
		StringBuffer sb3 = new StringBuffer("hello");
		System.out.println("sb3:" + sb3);
		System.out.println("sb3.capacity():" + sb3.capacity());  //缓冲区默认是16这里是16+5
		System.out.println("sb3.length():" + sb3.length());
	}
}

```
执行结果:
```java
sb:
sb.capacity():16
sb.length():0
--------------------------
sb2:
sb2.capacity():50
sb2.length():0
--------------------------
sb3:hello
sb3.capacity():21
sb3.length():5
```
# StringBuffer类的成员方法

- 添加功能

   	 •    public StringBuffer append(String str)

    	•     public StringBuffer insert(int offset,String str)
```java
package cn.itcast_02;

/*
 * StringBuffer的添加功能：
 * public StringBuffer append(String str):可以把任意类型数据添加到字符串缓冲区里面,并返回字符串缓冲区本身
 * 
 * public StringBuffer insert(int offset,String str):在指定位置把任意类型的数据插入到字符串缓冲区里面,并返回字符串缓冲区本身
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		// 创建字符串缓冲区对象
		StringBuffer sb = new StringBuffer();

		// public StringBuffer append(String str)
		// StringBuffer sb2 = sb.append("hello"); //这里相当于返回与本身,就是说sb2根sb是同一个对象,地址值是一样的,以后用的时候不用接受值
		// System.out.println("sb:" + sb);
		// System.out.println("sb2:" + sb2);
		// System.out.println(sb == sb2); // true

		// 一步一步的添加数据
		// sb.append("hello");
		// sb.append(true);
		// sb.append(12);
		// sb.append(34.56);

		// 链式编程
		sb.append("hello").append(true).append(12).append(34.56);
		System.out.println("sb:" + sb);

		// public StringBuffer insert(int offset,String
		// str):在指定位置把任意类型的数据插入到字符串缓冲区里面,并返回字符串缓冲区本身
		sb.insert(5, "world");
		System.out.println("sb:" + sb);
	}
}

```
执行结果:
```java
sb:hellotrue1234.56
sb:helloworldtrue1234.56
```


- 删除功能

  •     public StringBuffer deleteCharAt(int index)

  •     public StringBuffer delete(int start,int end)
```java
package cn.itcast_03;

/*
 * StringBuffer的删除功能
 * public StringBuffer deleteCharAt(int index):删除指定位置的字符，并返回本身
 * public StringBuffer delete(int start,int end):删除从指定位置开始指定位置结束的内容，并返回本身(包含开始不包含结尾)
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		// 创建对象
		StringBuffer sb = new StringBuffer();

		// 添加功能
		sb.append("hello").append("world").append("java");
		System.out.println("sb:" + sb);

		// public StringBuffer deleteCharAt(int index):删除指定位置的字符，并返回本身
		// 需求：我要删除e这个字符，肿么办?
		// sb.deleteCharAt(1);
		// 需求:我要删除第一个l这个字符，肿么办?  #上面删了一个下面删除的时候还是1
		// sb.deleteCharAt(1);

		// public StringBuffer delete(int start,int
		// end):删除从指定位置开始指定位置结束的内容，并返回本身
		// 需求：我要删除world这个字符串，肿么办?
		// sb.delete(5, 10);

		// 需求:我要删除所有的数据(sb.length()其实比索引大1)
		sb.delete(0, sb.length());

		System.out.println("sb:" + sb);
	}
}
```


- 替换功能

  •     public StringBuffer replace(int start,int end,String str)
```java
package cn.itcast_04;

/*
 * StringBuffer的替换功能：(包左不包右)
 * public StringBuffer replace(int start,int end,String str):从start开始到end用str替换
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		// 创建字符串缓冲区对象
		StringBuffer sb = new StringBuffer();

		// 添加数据
		sb.append("hello");
		sb.append("world");
		sb.append("java");
		System.out.println("sb:" + sb);

		// public StringBuffer replace(int start,int end,String
		// str):从start开始到end用str替换
		// 需求：我要把world这个数据替换为"节日快乐"
		sb.replace(5, 10, "节日快乐");
		System.out.println("sb:" + sb);
	}
}

```
执行结果:
```java
sb:helloworldjava
sb:hello节日快乐java
```
- 反转功能 public StringBuffer reverse()
```java
package cn.itcast_05;

/*
 * StringBuffer的反转功能：
 * public StringBuffer reverse()
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		// 创建字符串缓冲区对象
		StringBuffer sb = new StringBuffer();

		// 添加数据
		sb.append("霞青林爱我");
		System.out.println("sb:" + sb);

		// public StringBuffer reverse()
		sb.reverse();
		System.out.println("sb:" + sb);
	}
}
```
执行结果:
```java
sb:霞青林爱我
sb:我爱林青霞
```
# StringBuffer类的成员方法

- 截取功能

  •     public String substring(int start)

  •     public String substring(int start,int end)

- 截取功能和前面几个功能的不同

  •     返回值类型是String类型，本身没有发生改变
```java
package cn.itcast_06;

/*
 * StringBuffer的截取功能:注意返回值类型不再是StringBuffer本身了而是一个String
 * public String substring(int start)
 * public String substring(int start,int end)
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		// 创建字符串缓冲区对象
		StringBuffer sb = new StringBuffer();

		// 添加元素
		sb.append("hello").append("world").append("java");
		System.out.println("sb:" + sb);

		// 截取功能
		// public String substring(int start)
		String s = sb.substring(5); //这里返回的是一个字符串本身是不变的
		System.out.println("s:" + s);
		System.out.println("sb:" + sb);

		// public String substring(int start,int end)
		String ss = sb.substring(5, 10);
		System.out.println("ss:" + ss);
		System.out.println("sb:" + sb);
	}
}

```
执行结果:
```java
sb:helloworldjava
s:worldjava
sb:helloworldjava
ss:world
```
# StringBuffer类练习

- String和StringBuffer的相互转换
```java
package cn.itcast_07;

/*
 * 为什么我们要讲解类之间的转换：
 * A -- B的转换
 * 我们把A转换为B，其实是为了使用B的功能。
 * B -- A的转换
 * 我们可能要的结果是A类型，所以还得转回来。
 * 
 * String和StringBuffer的相互转换?
 */
public class StringBufferTest {
	public static void main(String[] args) {
		// String -- StringBuffer
		String s = "hello";
		// 注意：不能把字符串的值直接赋值给StringBuffer
		// StringBuffer sb = "hello";
		// StringBuffer sb = s;
		// 方式1:通过构造方法
		StringBuffer sb = new StringBuffer(s);
		// 方式2：通过append()方法
		StringBuffer sb2 = new StringBuffer();
		sb2.append(s);
		System.out.println("sb:" + sb);
		System.out.println("sb2:" + sb2);
		System.out.println("---------------");

		// StringBuffer -- String
		StringBuffer buffer = new StringBuffer("java");
		// String(StringBuffer buffer)
		// 方式1:通过构造方法
		String str = new String(buffer);
		// 方式2：通过toString()方法
		String str2 = buffer.toString(); //toString返回的是一个字符串
		System.out.println("str:" + str);
		System.out.println("str2:" + str2);
	}
}

```
执行:
```java
sb:hello
sb2:hello
---------------
str:java
str2:java
```
- 把数组拼接成一个字符串
```java
package cn.itcast_07;

/*
 * 把数组拼接成一个字符串
 */
public class StringBufferTest2 {
	public static void main(String[] args) {
		// 定义一个数组
		int[] arr = { 44, 33, 55, 11, 22 };

		// 定义功能
		// 方式1：用String做拼接的方式
		String s1 = arrayToString(arr);
		System.out.println("s1:" + s1);

		// 方式2:用StringBuffer做拼接的方式
		String s2 = arrayToString2(arr);
		System.out.println("s2:" + s2);
	}

	// 用StringBuffer做拼接的方式(速度快,占用的内存空间小)
	public static String arrayToString2(int[] arr) {
		StringBuffer sb = new StringBuffer();

		sb.append("[");
		for (int x = 0; x < arr.length; x++) {
			if (x == arr.length - 1) {
				sb.append(arr[x]);
			} else {
				sb.append(arr[x]).append(", "); //这里中间的元素需要加,
			}
		}
		sb.append("]");

		return sb.toString();
	}

	// 用String做拼接的方式
	public static String arrayToString(int[] arr) {
		String s = "";

		s += "[";
		for (int x = 0; x < arr.length; x++) {
			if (x == arr.length - 1) {
				s += arr[x];
			} else {
				s += arr[x];
				s += ", ";
			}
		}
		s += "]";

		return s;
	}
}

```
执行:
```java
s1:[44, 33, 55, 11, 22]
s2:[44, 33, 55, 11, 22]
```


- 把字符串反转
```java
package cn.itcast_07;

import java.util.Scanner;

/*
 * 把字符串反转
 */
public class StringBufferTest3 {
	public static void main(String[] args) {
		// 键盘录入数据
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入数据：");
		String s = sc.nextLine();

		// 方式1：用String做拼接
		String s1 = myReverse(s);
		System.out.println("s1:" + s1);
		// 方式2：用StringBuffer的reverse()功能
		String s2 = myReverse2(s);
		System.out.println("s2:" + s2);
	}

	// 用StringBuffer的reverse()功能
	public static String myReverse2(String s) {
		// StringBuffer sb = new StringBuffer();
		// sb.append(s);

		// StringBuffer sb = new StringBuffer(s);
		// sb.reverse();
		// return sb.toString();

		// 简易版
		return new StringBuffer(s).reverse().toString();
	}

	// 用String做拼接
	public static String myReverse(String s) {
		String result = "";

		char[] chs = s.toCharArray();
		for (int x = chs.length - 1; x >= 0; x--) {
			// char ch = chs[x];
			// result += ch;
			result += chs[x];
		}

		return result;
	}
}

```
执行:
```java
请输入数据：
abc
s1:cba
s2:cba
```


- 判断一个字符串是否是对称字符串
```java
package cn.itcast_07;

import java.util.Scanner;


/*
 * 判断一个字符串是否是对称字符串
 * 例如"abc"不是对称字符串，"aba"、"abba"、"aaa"、"mnanm"是对称字符串
 * 
 * 分析：
 * 		判断一个字符串是否是对称的字符串，我只需要把
 * 			第一个和最后一个比较
 * 			第二个和倒数第二个比较
 * 			...
 * 		比较的次数是长度除以2。
 */
public class StringBufferTest4 {
	public static void main(String[] args) {
		// 创建键盘录入对象
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入一个字符串：");
		String s = sc.nextLine();

		// 一个一个的比较
		boolean b = isSame(s);
		System.out.println("b:" + b);
		
		//用字符串缓冲区的反转功能
		boolean b2 = isSame2(s);
		System.out.println("b2:"+b2);
	}
	
	public static boolean isSame2(String s) {
		return new StringBuffer(s).reverse().toString().equals(s);
	}
	

	// public static boolean isSame(String s) {
	// // 把字符串转成字符数组
	// char[] chs = s.toCharArray();
	//
	// for (int start = 0, end = chs.length - 1; start <= end; start++, end--) {
	// if (chs[start] != chs[end]) {
	// return false;
	// }
	// }
	//
	// return true;
	// }

	public static boolean isSame(String s) {
		boolean flag = true;

		// 把字符串转成字符数组
		char[] chs = s.toCharArray();

		for (int start = 0, end = chs.length - 1; start <= end; start++, end--) {
			if (chs[start] != chs[end]) {
				flag = false;
				break;
			}
		}

		return flag;
	}
}
```
执行:
```java
请输入一个字符串：
aba
b:true
b2:true
```


  • 例如"abc"不是对称字符串，"aba"、"abba"、"aaa" 、"mnanm"是对称字符串

# StringBuffer类面试题

- 通过查看API了解一下StringBuilder类

- String,StringBuffer,StringBuilder的区别

- StringBuffer和数组的区别

- 看程序写结果：

  •     String作为参数传递

  •     StringBuffer作为参数传递
```java
package cn.itcast_08;

/*
 * 面试题：
 * 1：String,StringBuffer,StringBuilder的区别?
 * A:String是内容不可变的，而StringBuffer,StringBuilder都是内容可变的。
 * B:StringBuffer是同步的，数据安全,效率低;StringBuilder是不同步的,数据不安全,效率高
 * 
 * 2：StringBuffer和数组的区别?
 * 二者都可以看出是一个容器，装其他的数据。
 * 但是呢,StringBuffer的数据最终是一个字符串数据。
 * 而数组可以放置多种数据，但必须是同一种数据类型的。
 * 
 * 3:形式参数问题
 * String作为参数传递
 * StringBuffer作为参数传递 
 * 
 * 形式参数：
 * 		基本类型：形式参数的改变不影响实际参数
 * 		引用类型：形式参数的改变直接影响实际参数
 * 
 * 注意：
 * 		String作为参数传递，效果和基本类型作为参数传递是一样的。(常量)
 */
public class StringBufferDemo {
	public static void main(String[] args) {
		String s1 = "hello";
		String s2 = "world";
		System.out.println(s1 + "---" + s2);// hello---world
		change(s1, s2);
		System.out.println(s1 + "---" + s2);// hello---world

		StringBuffer sb1 = new StringBuffer("hello");
		StringBuffer sb2 = new StringBuffer("world");
		System.out.println(sb1 + "---" + sb2);// hello---world
		change(sb1, sb2);
		System.out.println(sb1 + "---" + sb2);// hello---worldworld

	}

	public static void change(StringBuffer sb1, StringBuffer sb2) {
		sb1 = sb2;
		sb2.append(sb1);  //操作内容会变,但是直接赋值不会变(常量)
	}

	public static void change(String s1, String s2) {
		s1 = s2;
		s2 = s1 + s2;
	}
}

```
执行:
```java
hello---world
hello---world
hello---world
hello---worldworld
```


## 数组高级**(**排序和查找**)**

- 排序

  •     冒泡排序

  •     相邻元素两两比较，大的往后放，第一次完毕，最大值出现在了最大索引处
![image.png](https://upload-images.jianshu.io/upload_images/14555448-5fedab49f82a0f05.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```java
package cn.itcast_01;

/*
 * 数组排序之冒泡排序：
 * 		相邻元素两两比较，大的往后放，第一次完毕，最大值出现在了最大索引处
 */
public class ArrayDemo {
	public static void main(String[] args) {
		// 定义一个数组
		int[] arr = { 24, 69, 80, 57, 13 };
		System.out.println("排序前：");
		printArray(arr);

		/*
		// 第一次比较
		// arr.length - 1是为了防止数据越界
		// arr.length - 1 - 0是为了减少比较的次数
		for (int x = 0; x < arr.length - 1 - 0; x++) {
			if (arr[x] > arr[x + 1]) {
				int temp = arr[x];
				arr[x] = arr[x + 1];
				arr[x + 1] = temp;
			}
		}
		System.out.println("第一次比较后：");
		printArray(arr);

		// 第二次比较
		// arr.length - 1是为了防止数据越界
		// arr.length - 1 - 1是为了减少比较的次数
		for (int x = 0; x < arr.length - 1 - 1; x++) {
			if (arr[x] > arr[x + 1]) {
				int temp = arr[x];
				arr[x] = arr[x + 1];
				arr[x + 1] = temp;
			}
		}
		System.out.println("第二次比较后：");
		printArray(arr);

		// 第三次比较
		// arr.length - 1是为了防止数据越界
		// arr.length - 1 - 2是为了减少比较的次数
		for (int x = 0; x < arr.length - 1 - 2; x++) {
			if (arr[x] > arr[x + 1]) {
				int temp = arr[x];
				arr[x] = arr[x + 1];
				arr[x + 1] = temp;
			}
		}
		System.out.println("第三次比较后：");
		printArray(arr);

		// 第四次比较
		// arr.length - 1是为了防止数据越界
		// arr.length - 1 - 3是为了减少比较的次数
		for (int x = 0; x < arr.length - 1 - 3; x++) {
			if (arr[x] > arr[x + 1]) {
				int temp = arr[x];
				arr[x] = arr[x + 1];
				arr[x + 1] = temp;
			}
		}
		System.out.println("第四次比较后：");
		printArray(arr);
		*/

		// 既然听懂了，那么上面的代码就是排序代码
		// 而上面的代码重复度太高了，所以用循环改进
		// for (int y = 0; y < 4; y++) {
		// for (int x = 0; x < arr.length - 1 - y; x++) {
		// if (arr[x] > arr[x + 1]) {
		// int temp = arr[x];
		// arr[x] = arr[x + 1];
		// arr[x + 1] = temp;
		// }
		// }
		// }

		/*
		// 由于我们知道比较的次数是数组长度-1次，所以改进最终版程序
		for (int x = 0; x < arr.length - 1; x++) {
			for (int y = 0; y < arr.length - 1 - x; y++) {
				if (arr[y] > arr[y + 1]) {
					int temp = arr[y];
					arr[y] = arr[y + 1];
					arr[y + 1] = temp;
				}
			}
		}
		System.out.println("排序后：");
		printArray(arr);
		*/
		
		//由于我可能有多个数组要排序，所以我要写成方法
		bubbleSort(arr);
		System.out.println("排序后：");
		printArray(arr);
	}
	
	//冒泡排序代码
	public static void bubbleSort(int[] arr){
		for (int x = 0; x < arr.length - 1; x++) {
			for (int y = 0; y < arr.length - 1 - x; y++) {
				if (arr[y] > arr[y + 1]) {
					int temp = arr[y];
					arr[y] = arr[y + 1];
					arr[y + 1] = temp;
				}
			}
		}
	}

	// 遍历功能
	public static void printArray(int[] arr) {
		System.out.print("[");
		for (int x = 0; x < arr.length; x++) {
			if (x == arr.length - 1) {
				System.out.print(arr[x]);
			} else {
				System.out.print(arr[x] + ", ");
			}
		}
		System.out.println("]");
	}
}
```
执行结果:
```java
排序前：
[24, 69, 80, 57, 13]
排序后：
[13, 24, 57, 69, 80]
```

  •     选择排序

  •     从0索引开始，依次和后面元素比较，小的往前放，第一次完毕，最小值出现在了最小索引处
![image.png](https://upload-images.jianshu.io/upload_images/14555448-522465056954ac74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```java
package cn.itcast_02;

/*
 * 数组排序之选择排序：
 * 		从0索引开始，依次和后面元素比较，小的往前放，第一次完毕，最小值出现在了最小索引处
 */
public class ArrayDemo {
	public static void main(String[] args) {
		// 定义一个数组
		int[] arr = { 24, 69, 80, 57, 13 };
		System.out.println("排序前：");
		printArray(arr);

		/*
		// 第一次
		int x = 0;
		for (int y = x + 1; y < arr.length; y++) {
			if (arr[y] < arr[x]) {
				int temp = arr[x];
				arr[x] = arr[y];
				arr[y] = temp;
			}
		}
		System.out.println("第一次比较后：");
		printArray(arr);

		// 第二次
		x = 1;
		for (int y = x + 1; y < arr.length; y++) {
			if (arr[y] < arr[x]) {
				int temp = arr[x];
				arr[x] = arr[y];
				arr[y] = temp;
			}
		}
		System.out.println("第二次比较后：");
		printArray(arr);

		// 第三次
		x = 2;
		for (int y = x + 1; y < arr.length; y++) {
			if (arr[y] < arr[x]) {
				int temp = arr[x];
				arr[x] = arr[y];
				arr[y] = temp;
			}
		}
		System.out.println("第三次比较后：");
		printArray(arr);

		// 第四次
		x = 3;
		for (int y = x + 1; y < arr.length; y++) {
			if (arr[y] < arr[x]) {
				int temp = arr[x];
				arr[x] = arr[y];
				arr[y] = temp;
			}
		}
		System.out.println("第四次比较后：");
		printArray(arr);
		*/
		
		/*
		//通过观察发现代码的重复度太高，所以用循环改进
		for(int x=0; x<arr.length-1; x++){
			for(int y=x+1; y<arr.length; y++){
				if(arr[y] <arr[x]){
					int temp = arr[x];
					arr[x] = arr[y];
					 arr[y] = temp;
				}
			}
		}
		System.out.println("排序后：");
		printArray(arr);
		*/
		
		//用方法改进
		selectSort(arr);
		System.out.println("排序后：");
		printArray(arr);

	}
	
	public static void selectSort(int[] arr){
		for(int x=0; x<arr.length-1; x++){
			for(int y=x+1; y<arr.length; y++){
				if(arr[y] <arr[x]){
					int temp = arr[x];
					arr[x] = arr[y];
					 arr[y] = temp;
				}
			}
		}
	}

	// 遍历功能
	public static void printArray(int[] arr) {
		System.out.print("[");
		for (int x = 0; x < arr.length; x++) {
			if (x == arr.length - 1) {
				System.out.print(arr[x]);
			} else {
				System.out.print(arr[x] + ", ");
			}
		}
		System.out.println("]");
	}
}

```
执行:
```java
排序前：
[24, 69, 80, 57, 13]
排序后：
[13, 24, 57, 69, 80]
```

- 查找

  •     基本查找 数组元素无序

  •     二分查找 数组元素有序
![image.png](https://upload-images.jianshu.io/upload_images/14555448-c19e19366ba43e02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 数组高级练习题

- 把字符串中的字符进行排序。

  •     举例：”dacgebf”

  •     结果：”abcdefg”


   ```java
package cn.itcast_03;

/*
 * 把字符串中的字符进行排序。
 * 		举例："dacgebf"
 * 		结果："abcdefg"
 * 
 * 分析：
 * 		A:定义一个字符串
 * 		B:把字符串转换为字符数组
 * 		C:把字符数组进行排序
 * 		D:把排序后的字符数组转成字符串
 * 		E:输出最后的字符串
 */
public class ArrayTest {
	public static void main(String[] args) {
		// 定义一个字符串
		String s = "dacgebf";

		// 把字符串转换为字符数组
		char[] chs = s.toCharArray();

		// 把字符数组进行排序
		bubbleSort(chs);

		//把排序后的字符数组转成字符串
		String result = String.valueOf(chs);
		
		//输出最后的字符串
		System.out.println("result:"+result);
	}

	// 冒泡排序
	public static void bubbleSort(char[] chs) {
		for (int x = 0; x < chs.length - 1; x++) {
			for (int y = 0; y < chs.length - 1 - x; y++) {
				if (chs[y] > chs[y + 1]) {
					char temp = chs[y];
					chs[y] = chs[y + 1];
					chs[y + 1] = temp;
				}
			}
		}
	}
}

   ```


## **Arrays**类概述及其常用方法

- Arrays类概述

  •     针对数组进行操作的工具类。

  •     提供了排序，查找等功能。

- 成员方法

  •     public static String toString(int[] a)

  •     public static void sort(int[] a)

  •     public static int binarySearch(int[] a,int key)
```java
package cn.itcast_05;

import java.util.Arrays;

/*
 * Arrays:针对数组进行操作的工具类。比如说排序和查找。
 * 1:public static String toString(int[] a) 把数组转成字符串
 * 2:public static void sort(int[] a) 对数组进行排序
 * 3:public static int binarySearch(int[] a,int key) 二分查找
 */
public class ArraysDemo {
	public static void main(String[] args) {
		// 定义一个数组
		int[] arr = { 24, 69, 80, 57, 13 };

		// public static String toString(int[] a) 把数组转成字符串
		System.out.println("排序前：" + Arrays.toString(arr));

		// public static void sort(int[] a) 对数组进行排序
		Arrays.sort(arr); //直接调用排序方法
		System.out.println("排序后：" + Arrays.toString(arr));

		// [13, 24, 57, 69, 80]
		// public static int binarySearch(int[] a,int key) 二分查找
		System.out.println("binarySearch:" + Arrays.binarySearch(arr, 57));
		System.out.println("binarySearch:" + Arrays.binarySearch(arr, 577));
	}
}
```
执行结果:
```java
排序前：[24, 69, 80, 57, 13]
排序后：[13, 24, 57, 69, 80]
binarySearch:2
binarySearch:-6
```

## **Arrays**类常用方法源码详细解释

- public static String toString(int[] a) 源码解析 (底层是快速排序)

- public static int binarySearch(int[] a,int key) 源码解析
```java
public static String toString(int[] a)
public static void sort(int[] a) 底层是快速排序，知道就可以了。有空看，有问题再问我
public static int binarySearch(int[] a,int key)

开发原则：
	只要是对象，我们就要判断该对象是否为null。

int[] arr = { 24, 69, 80, 57, 13 };
System.out.println("排序前：" + Arrays.toString(arr));

public static String toString(int[] a) {
	//a -- arr -- { 24, 69, 80, 57, 13 }

    if (a == null)
        return "null"; //说明数组对象不存在
    int iMax = a.length - 1; //iMax=4;
    if (iMax == -1)
        return "[]"; //说明数组存在,但是没有元素。

    StringBuilder b = new StringBuilder();
    b.append('['); //"["
    for (int i = 0; ; i++) {
        b.append(a[i]); //"[24, 69, 80, 57, 13"
        if (i == iMax)
        	//"[24, 69, 80, 57, 13]"
            return b.append(']').toString();
        b.append(", "); //"[24, 69, 80, 57, "
    }
}
-----------------------------------------------------

int[] arr = {13, 24, 57, 69, 80};
System.out.println("binarySearch:" + Arrays.binarySearch(arr, 577));

public static int binarySearch(int[] a, int key) {
	//a -- arr -- {13, 24, 57, 69, 80}
	//key -- 577
    return binarySearch0(a, 0, a.length, key);
}

private static int binarySearch0(int[] a, int fromIndex, int toIndex,
                                 int key) {
    //a -- arr --  {13, 24, 57, 69, 80}
    //fromIndex -- 0
    //toIndex -- 5
    //key -- 577                           
                                 
                                 
    int low = fromIndex; //low=0 
    int high = toIndex - 1; //high=4

    while (low <= high) {
        int mid = (low + high) >>> 1; //mid=2,mid=3,mid=4
        int midVal = a[mid]; //midVal=57,midVal=69,midVal=80

        if (midVal < key)
            low = mid + 1; //low=3,low=4,low=5
        else if (midVal > key)
            high = mid - 1;
        else
            return mid; // key found
    }
    return -(low + 1);  // key not found.
}
```
## 基本类型包装类概述

- 将基本数据类型封装成对象的好处在于可以在对象中定义更多的功能方法操作该数据。

- 常用的操作之一：用于基本数据类型与字符串之间的转换。

- 基本类型和包装类的对应

  • Byte,Short,Integer,Long,Float,Double

  Character,Boolean

## **Integer**类概述及其构造方法

- Integer类概述

  •   Integer 类在对象中包装了一个基本类型 int 的值

  •   该类提供了多个方法，能在 int 类型和 String 类型之间互相转换，还提供了处理 int 类型时非常有用的其他一些常量和方法 l 构造方法

  •   public Integer(int value)

  •   public Integer(String s)

```java
package cn.itcast_02;

/*
 * Integer的构造方法：
 * public Integer(int value)
 * public Integer(String s)
 * 		注意：这个字符串必须是由数字字符组成
 */
public class IntegerDemo {
	public static void main(String[] args) {
		// 方式1
		int i = 100;
		Integer ii = new Integer(i);
		System.out.println("ii:" + ii);

		// 方式2
		String s = "100";
		// NumberFormatException
		// String s = "abc";
		Integer iii = new Integer(s);
		System.out.println("iii:" + iii);
	}
}
```
执行:
```java
ii:100
iii:100
```
# Integer类成员方法

- int类型和String类型的相互转换

  • int – String • String – int

- public int intValue()

- public static int parseInt(String s)

- public static String toString(int i)

- public static Integer valueOf(int i)

- public static Integer valueOf(String s)
```java
package cn.itcast_03;

/*
 * int类型和String类型的相互转换
 * 
 * int -- String
 * 		String.valueOf(number)
 * 
 * String -- int
 * 		Integer.parseInt(s)
 */
public class IntegerDemo {
	public static void main(String[] args) {
		// int -- String
		int number = 100;
		// 方式1
		String s1 = "" + number;
		System.out.println("s1:" + s1);
		// 方式2
		String s2 = String.valueOf(number);
		System.out.println("s2:" + s2);
		// 方式3
		// int -- Integer -- String
		Integer i = new Integer(number);
		String s3 = i.toString();
		System.out.println("s3:" + s3);
		// 方式4
		// public static String toString(int i)
		String s4 = Integer.toString(number);
		System.out.println("s4:" + s4);
		System.out.println("-----------------");

		// String -- int
		String s = "100";
		// 方式1
		// String -- Integer -- int
		Integer ii = new Integer(s);
		// public int intValue()
		int x = ii.intValue();
		System.out.println("x:" + x);
		//方式2
		//public static int parseInt(String s)
		int y = Integer.parseInt(s);
		System.out.println("y:"+y);
	}
}

```
执行:
```java
s1:100
s2:100
s3:100
s4:100
-----------------
x:100
y:100
```

# Integer类成员方法

- 常用的基本进制转换

  •     public static String toBinaryString(int i)

  •     public static String toOctalString(int i)

  •     public static String toHexString(int i)

- 十进制到其他进制

  •     public static String toString(int i,int radix)

- 其他进制到十进制

  •     public static int parseInt(String s,int radix)
```java
package cn.itcast_04;

/*
 * 常用的基本进制转换
 * public static String toBinaryString(int i)
 * public static String toOctalString(int i)
 * public static String toHexString(int i)
 * 
 * 十进制到其他进制
 * public static String toString(int i,int radix)
 * 由这个我们也看到了进制的范围：2-36
 * 为什么呢?0,...9,a...z
 * 
 * 其他进制到十进制
 * public static int parseInt(String s,int radix)
 */
public class IntegerDemo {
	public static void main(String[] args) {
		// 十进制到二进制，八进制，十六进制
		System.out.println(Integer.toBinaryString(100));
		System.out.println(Integer.toOctalString(100));
		System.out.println(Integer.toHexString(100));
		System.out.println("-------------------------");

		// 十进制到其他进制
		System.out.println(Integer.toString(100, 10));
		System.out.println(Integer.toString(100, 2));
		System.out.println(Integer.toString(100, 8));
		System.out.println(Integer.toString(100, 16));
		System.out.println(Integer.toString(100, 5));
		System.out.println(Integer.toString(100, 7));
		System.out.println(Integer.toString(100, -7));
		System.out.println(Integer.toString(100, 70));
		System.out.println(Integer.toString(100, 1));
		System.out.println(Integer.toString(100, 17));
		System.out.println(Integer.toString(100, 32));
		System.out.println(Integer.toString(100, 37));
		System.out.println(Integer.toString(100, 36));
		System.out.println("-------------------------");
		
		//其他进制到十进制
		System.out.println(Integer.parseInt("100", 10));
		System.out.println(Integer.parseInt("100", 2));
		System.out.println(Integer.parseInt("100", 8));
		System.out.println(Integer.parseInt("100", 16));
		System.out.println(Integer.parseInt("100", 23));
		//NumberFormatException
		//System.out.println(Integer.parseInt("123", 2));
	}
}

```
执行:
```java
1100100
144
64
-------------------------
100
1100100
144
64
400
202
100
100
100
5f
34
100
2s
-------------------------
100
4
64
256
529
```
# JDK5的新特性

- JDK1.5以后，简化了定义方式。

  •    Integer x = new Integer(4); 可以直接写成

  •    Integer x = 4; //自动装箱。

  •    x  = x + 5; //自动拆箱。通过intValue方法。

- 需要注意：

  • 在使用时，Integer  x = null;上面的代码就会出现NullPointerException。
```java
package cn.itcast_05;

/*
 * JDK5的新特性
 * 自动装箱：把基本类型转换为包装类类型
 * 自动拆箱：把包装类类型转换为基本类型
 * 
 * 注意一个小问题：
 * 		在使用时，Integer  x = null;代码就会出现NullPointerException。
 * 		建议先判断是否为null，然后再使用。
 */
public class IntegerDemo {
	public static void main(String[] args) {
		// 定义了一个int类型的包装类类型变量i
		// Integer i = new Integer(100);
		Integer ii = 100;
		ii += 200;
		System.out.println("ii:" + ii);

		// 通过反编译后的代码
		// Integer ii = Integer.valueOf(100); //自动装箱
		// ii = Integer.valueOf(ii.intValue() + 200); //自动拆箱，再自动装箱
		// System.out.println((new StringBuilder("ii:")).append(ii).toString());

		Integer iii = null;
		// NullPointerException
		if (iii != null) {
			iii += 1000;
			System.out.println(iii);
		}
	}
}

```
执行
```java
ii:300
```
# Integer的面试题

- Integer i = 1; i += 1;做了哪些事情

- 缓冲池(看程序写结果)

  • 通过查看源码知道为什么
```java
package cn.itcast_06;

/*
 * 看程序写结果
 * 
 * 注意：Integer的数据直接赋值，如果在-128到127之间，会直接从缓冲池里获取数据
 */
public class IntegerDemo {
	public static void main(String[] args) {
		Integer i1 = new Integer(127);
		Integer i2 = new Integer(127);
		System.out.println(i1 == i2);  //这里是创建了新的空间所以是false
		System.out.println(i1.equals(i2));
		System.out.println("-----------");

		Integer i3 = new Integer(128);
		Integer i4 = new Integer(128);
		System.out.println(i3 == i4);
		System.out.println(i3.equals(i4));
		System.out.println("-----------");

		Integer i5 = 128;
		Integer i6 = 128;
		System.out.println(i5 == i6);  //128超出了范围创建了新的空间
		System.out.println(i5.equals(i6));
		System.out.println("-----------");

		Integer i7 = 127;
		Integer i8 = 127;
		System.out.println(i7 == i8);  //这里是直接从常量池里取出来的
		System.out.println(i7.equals(i8));

		// 通过查看源码，我们就知道了，针对-128到127之间的数据，做了一个数据缓冲池，如果数据是该范围内的，每次并不创建新的空间
		// Integer ii = Integer.valueOf(127);
	}
}

```
执行:
```java
false
true
-----------
false
true
-----------
false
true
-----------
true
true
```
# Character类概述及其构造方法(character了解)

- Character类概述

  •     Character 类在对象中包装一个基本类型 char 的值

  •     此外，该类提供了几种方法，以确定字符的类别（小写字母，数字，等等），并将字符从大写转换成小写，反之亦然

- 构造方法

  •     public Character(char value)
```java
package cn.itcast_01;

/*
 * Character 类在对象中包装一个基本类型 char 的值
 * 此外，该类提供了几种方法，以确定字符的类别（小写字母，数字，等等），并将字符从大写转换成小写，反之亦然
 * 
 * 构造方法：
 * 		Character(char value)
 */
public class CharacterDemo {
	public static void main(String[] args) {
		// 创建对象
		// Character ch = new Character((char) 97);
		Character ch = new Character('a');
		System.out.println("ch:" + ch);
	}
}
```

# Character类成员方法

- public static boolean isUpperCase(char ch)

- public static boolean isLowerCase(char ch)

- public static boolean isDigit(char ch)

- public static char toUpperCase(char ch)

- public static char toLowerCase(char ch)
```java
package cn.itcast_02;

/*
 * public static boolean isUpperCase(char ch):判断给定的字符是否是大写字符
 * public static boolean isLowerCase(char ch):判断给定的字符是否是小写字符
 * public static boolean isDigit(char ch):判断给定的字符是否是数字字符
 * public static char toUpperCase(char ch):把给定的字符转换为大写字符
 * public static char toLowerCase(char ch):把给定的字符转换为小写字符
 */
public class CharacterDemo {
	public static void main(String[] args) {
		// public static boolean isUpperCase(char ch):判断给定的字符是否是大写字符
		System.out.println("isUpperCase:" + Character.isUpperCase('A'));
		System.out.println("isUpperCase:" + Character.isUpperCase('a'));
		System.out.println("isUpperCase:" + Character.isUpperCase('0'));
		System.out.println("-----------------------------------------");
		// public static boolean isLowerCase(char ch):判断给定的字符是否是小写字符
		System.out.println("isLowerCase:" + Character.isLowerCase('A'));
		System.out.println("isLowerCase:" + Character.isLowerCase('a'));
		System.out.println("isLowerCase:" + Character.isLowerCase('0'));
		System.out.println("-----------------------------------------");
		// public static boolean isDigit(char ch):判断给定的字符是否是数字字符
		System.out.println("isDigit:" + Character.isDigit('A'));
		System.out.println("isDigit:" + Character.isDigit('a'));
		System.out.println("isDigit:" + Character.isDigit('0'));
		System.out.println("-----------------------------------------");
		// public static char toUpperCase(char ch):把给定的字符转换为大写字符
		System.out.println("toUpperCase:" + Character.toUpperCase('A'));
		System.out.println("toUpperCase:" + Character.toUpperCase('a'));
		System.out.println("-----------------------------------------");
		// public static char toLowerCase(char ch):把给定的字符转换为小写字符
		System.out.println("toLowerCase:" + Character.toLowerCase('A'));
		System.out.println("toLowerCase:" + Character.toLowerCase('a'));
	}
}

```
执行
```java
isUpperCase:true
isUpperCase:false
isUpperCase:false
-----------------------------------------
isLowerCase:false
isLowerCase:true
isLowerCase:false
-----------------------------------------
isDigit:false
isDigit:false
isDigit:true
-----------------------------------------
toUpperCase:A
toUpperCase:A
-----------------------------------------
toLowerCase:a
toLowerCase:a
```
实例
```java
package cn.itcast_03;

import java.util.Scanner;

/*
 * 统计一个字符串中大写字母字符，小写字母字符，数字字符出现的次数。(不考虑其他字符)
 * 
 * 分析：
 * 		A:定义三个统计变量。
 * 			int bigCont=0;
 * 			int smalCount=0;
 * 			int numberCount=0;
 * 		B:键盘录入一个字符串。
 * 		C:把字符串转换为字符数组。
 * 		D:遍历字符数组获取到每一个字符
 * 		E:判断该字符是
 * 			大写	bigCount++;
 * 			小写	smalCount++;
 * 			数字	numberCount++;
 * 		F:输出结果即可
 */
public class CharacterTest {
	public static void main(String[] args) {
		// 定义三个统计变量。
		int bigCount = 0;
		int smallCount = 0;
		int numberCount = 0;

		// 键盘录入一个字符串。
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入一个字符串：");
		String line = sc.nextLine();

		// 把字符串转换为字符数组。
		char[] chs = line.toCharArray();

		// 历字符数组获取到每一个字符
		for (int x = 0; x < chs.length; x++) {
			char ch = chs[x];

			// 判断该字符
			if (Character.isUpperCase(ch)) {
				bigCount++;
			} else if (Character.isLowerCase(ch)) {
				smallCount++;
			} else if (Character.isDigit(ch)) {
				numberCount++;
			}
		}

		// 输出结果即可
		System.out.println("大写字母：" + bigCount + "个");
		System.out.println("小写字母：" + smallCount + "个");
		System.out.println("数字字符：" + numberCount + "个");
	}
}

```
执行:
```java
请输入一个字符串：
abposajdposAAJJOI123
大写字母：6个
小写字母：11个
数字字符：3个
```