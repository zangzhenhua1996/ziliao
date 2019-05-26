### 04.01_Java语言基础(循环结构概述和for语句的格式及其使用)

- A:循环结构的分类
  - for,while,do...while 
- B:循环结构for语句的格式：
- for(初始化表达式;条件表达式;循环后的操作表达式) {
  		循环体;
  	}
- C执行流程：
  - a:执行初始化语句
  - b:执行判断条件语句,看其返回值是true还是false
    - 如果是true，就继续执行
    - 如果是false，就结束循环
  - c:执行循环体语句;
  - d:执行循环后的操作表达式
  - e:回到B继续。
- D:案例演示
  - 在控制台输出10次"helloworld"
案列:
```java
/*
* A:循环结构的分类
	* for,while,do...while 
* B:循环结构for语句的格式：
* 
		for(初始化表达式;条件表达式;循环后的操作表达式) {
			循环体;
		}
* C执行流程：
	* a:执行初始化语句
	* b:执行判断条件语句,看其返回值是true还是false
		* 如果是true，就继续执行
		* 如果是false，就结束循环
	* c:执行循环体语句;
	* d:执行循环后的操作表达式
	* e:回到B继续。
* D:案例演示
	* 在控制台输出10次"helloworld"
*/
class Demo1_For {
	public static void main(String[] args) {
		//在控制输出10次helloworld,这样做不推荐,因为复用性太差
		/*System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");
		System.out.println("helloworld");*/

		for (int i = 1;i <= 10 ;i++ ) {
			System.out.println("helloworld");
		}
	}
}

```
### 04.02_Java语言基础(循环结构for语句的练习之获取数据)

- A:案例演示
  - 需求：请在控制台输出数据1-10

  - 需求：请在控制台输出数据10-1
```java
/*
* A:案例演示
	* 需求：请在控制台输出数据1-10
	* 需求：请在控制台输出数据10-1
* B:注意事项
	* a:判断条件语句无论简单还是复杂结果是boolean类型。
	* b:循环体语句如果是一条语句，大括号可以省略；如果是多条语句，大括号不能省略。建议永远不要省略。
	* c:一般来说：有左大括号就没有分号，有分号就没有左大括号
*/
class Test1_For {
	public static void main(String[] args) {
		for (int i = 1;i <= 10 ;i++ ){
			System.out.println("i = " + i);
		}
		System.out.println("-----------------------");

		for (int i = 10;i >= 1 ;i-- ) {
			System.out.println("i = " + i);
		}
	}
}

```
输出结果
```java
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
i = 7
i = 8
i = 9
i = 10
-----------------------
i = 10
i = 9
i = 8
i = 7
i = 6
i = 5
i = 4
i = 3
i = 2
i = 1
请按任意键继续. . .
```
- B:注意事项
  - a:判断条件语句无论简单还是复杂结果是boolean类型。
  - b:循环体语句如果是一条语句，大括号可以省略；如果是多条语句，大括号不能省略。建议永远不要省略。
  - c:一般来说：有左大括号就没有分号，有分号就没有左大括号

### 04.03_Java语言基础(循环结构for语句的练习之求和思想)

- A:案例演示
  - 需求：求出1-10之间数据之和
```java
class test 
{
	public static void main(String[] args) 
	{		//1-10的和
		int sum = 0;
		for (int i = 1;i <= 10 ;i++ ) {
			sum = sum + i;
		}

		System.out.println("sum = " + sum);
	}
}
```
- B:学生练习
  - 需求：求出1-100之间偶数和
```java
class test  {
	public static void main(String[] args) 
	{		//1-10的和
		int sum = 0;
		for (int i = 1;i <= 100 ;i++ ) {
			if (i%2==0) {
				sum = sum + i;
			}
			
		}

		System.out.println("sum = " + sum);
	}
}
```
  - 需求：求出1-100之间奇数和
```java
class test  {
	public static void main(String[] args) 
	{		//1-10的和
		int sum = 0;
		for (int i = 1;i <= 100 ;i++ ) {
			if (i%2!=0) {
				sum = sum + i;
			}
			
		}

		System.out.println("sum = " + sum);
	}
}
```
### 04.04_Java语言基础(循环结构for语句的练习之水仙花)

- A:案例演示
  - 需求：在控制台输出所有的”水仙花数”
  - 所谓的水仙花数是指一个三位数，其各位数字的立方和等于该数本身。
  - 举例：153就是一个水仙花数。
  - 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153
```java
/*
* A:案例演示
	* 需求：在控制台输出所有的”水仙花数”

	* 所谓的水仙花数是指一个三位数，其各位数字的立方和等于该数本身。
	* 举例：153就是一个水仙花数。
	* 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153

	分析:
	1,100 - 999
	2,获取每一个位数的值,百位,十位,个位
	3,判断各个位上的立方和是否等于这个数,如果等于打印
*/
class Test3_Flower {
	public static void main(String[] args) {
		for (int i = 100;i <= 999 ;i++ ) {					//获取100到999之间的数
			int ge = i % 10;								//123 % 10 =3
			int shi = i / 10 % 10;							//12 % 10 =2
			int bai = i / 10 / 10 % 10;						//1 % 10 =1

			if (ge * ge * ge + shi * shi * shi + bai * bai * bai == i) {
				System.out.println(i);
			}
		}
	}
}


```
### 04.05_Java语言基础(循环结构for语句的练习之统计思想)

- A:案例演示
  - 需求：统计”水仙花数”共有多少个
```java
/*
* A:案例演示
	* 需求：统计”水仙花数”共有多少个
	分析:
	1,需要有一个变量记录住水仙花数的个数
	2,获取到所有的3位数
	3,判断是否满足水仙花数
	4,如果满足条件,计数器就自增
*/
class Test4_FlowerCount {
	public static void main(String[] args) {
		int count = 0;

		for (int i = 100;i <= 999 ;i++ ) {
			int ge = i % 10;
			int shi = i / 10 % 10;
			int bai = i / 10 / 10;

			if (i == ge * ge * ge + shi * shi * shi + bai * bai * bai) {
				count ++;													//满足条件就自增,计数器思想
			}
		}

		System.out.println(count);
	}
}

```
### 04.06_Java语言基础(循环结构while语句的格式和基本使用)

- A:循环结构while语句的格式：

 ```
  while循环的基本格式：
  while(判断条件语句) {
  	循环体语句;
  }
  
  完整格式：
  
  初始化语句;
  while(判断条件语句) {
  	 循环体语句;
  	 控制条件语句;
  }
  ```

- B:执行流程：

  - a:执行初始化语句
  - b:执行判断条件语句,看其返回值是true还是false
    - 如果是true，就继续执行
    - 如果是false，就结束循环
  - c:执行循环体语句;
  - d:执行控制条件语句
  - e:回到B继续。

- C:案例演示

  - 需求：请在控制台输出数据1-10
```java
class test  {
	public static void main(String[] args) 
	{	
		int x=1;
		while (x<=10) {
			System.out.println("x=: "+x);
			x++;
			}
	}
}

```
### 04.07_Java语言基础(循环结构while语句的练习)

- A:求和思想
  - 求1-100之和
```java
class test  {
	public static void main(String[] args) 
	{		//1-100的和
		int sum = 0;
		int i=0;
		while (i<=100) {
			sum=sum+i;
			i++;

		}

		System.out.println("sum = " + sum);

	}
}

```
- B:统计思想
  - 统计”水仙花数”共有多少个
```java
class While1 {
	public static void main(String[] args) {

		int count=0;
		int i=100;
		while (i<=999) {
			int ge=i%10;
			int shi=i/10%10;
			int bai=i/100;
			 if (i == ge * ge * ge + shi * shi * shi + bai * bai * bai){
				count++;
				}
			i++;
			
			}
		System.out.println(count);
		}
		
	}


```

### 04.08_Java语言基础(循环结构do...while语句的格式和基本使用)

- A:循环结构do...while语句的格式：

- do {
  		循环体语句;
  	}while(判断条件语句);
  	

  ```
  完整格式；
  初始化语句;
  do {
  	循环体语句;
  	控制条件语句;
  }while(判断条件语句);
  ```

- B:执行流程：

  - a:执行初始化语句
  - b:执行循环体语句;
  - c:执行控制条件语句
  - d:执行判断条件语句,看其返回值是true还是false
    - 如果是true，就继续执行
    - 如果是false，就结束循环
  - e:回到b继续。

- C:案例演示

  - 需求：请在控制台输出数据1-10
```java
class test  {
	public static void main(String[] args) 
	{		//1-100的和
		
		int i=1;

		do{
			System.out.println(i);
			i++;
		}
		while (i<=10);


		}

	}

```
### 04.09_Java语言基础(循环结构三种循环语句的区别)

- A:案例演示
  - 三种循环语句的区别:
  - do...while循环至少执行一次循环体。
  - 而for,while循环必须先判断条件是否成立，然后决定是否执行循环体语句。
- B:案例演示
  - for循环和while循环的区别：
    - A:如果你想在循环结束后，继续使用控制条件的那个变量，用while循环，否则用for循环。不知道用谁就用for循环。因为变量及早的从内存中消失，可以提高内存的使用效率。
      	

### 04.10_Java语言基础(循环结构注意事项之死循环)

- A:一定要注意控制条件语句控制的那个变量的问题，不要弄丢了，否则就容易死循环。
- B:两种最简单的死循环格式
  - while(true){...}
  - for(;;){...}
```java
		//while语句的无限循环
		while (true) {
			System.out.println("hello world");
		}

		//System.out.println("hello world");
		//for语句的无限循环
		for (; ; ) {
			System.out.println("hello world");
```
### 04.11_Java语言基础(循环结构循环嵌套输出4行5列的星星)

- A:案例演示

  - 需求：请输出一个4行5列的星星(*)图案。

  - 如图：
    		*****
    		*****
    		*****
    		*****
    		

    ```
    注意：
    	System.out.println("*");和System.out.print("*");的区别
    ```

- B:结论：

  - 外循环控制行数，内循环控制列数
```java
/*
* A:案例演示
	* 需求：请输出一个4行5列的星星(*)图案。
	* 
			如图：
				*****
				*****
				*****
				*****
				
			注意：
				System.out.println("*");和System.out.print("*");的区别
* B:结论：
	* 外循环控制行数，内循环控制列数
*/
class Demo1_ForFor {
	public static void main(String[] args) {

		for (int i = 1;i <= 4 ;i++ ) {					//外循环决定的是行数
			for (int j = 1;j <= 5 ;j++ ) {				//内循环决定的是列数
				System.out.print("*");    //同行打印
			}
			System.out.println();   //换行打印
		}
	}
}

/*
*****
*****
*****
*****

*/

```
### 04.12_Java语言基础(循环结构循环嵌套输出正三角形)

- A:案例演示
- 需求：请输出下列的形状
```
  	*
  	**
  	***
  	****
  	*****
```
```java
/*
需求：请输出下列的形状
		*
		**
		***
		****
		*****
*/
class Demo2_ForFor {
	public static void main(String[] args) {
		for (int i = 1;i <= 5 ; i++) {				//外循环决定行数
			for (int j = 1;j <= i ;j++ ) {			//内循环决定列数
				System.out.print("*");
			}
			System.out.println();					//将光标换到下一行的行首
		}
	}
}
/*
*
**

*/
```
### 04.13_Java语言基础(循环结构九九乘法表)

- A:案例演示

  - 需求：在控制台输出九九乘法表。
```java
/*
* A:案例演示
	* 需求：在控制台输出九九乘法表。

1 * 1 = 1
1 * 2 = 2 2 * 2 = 4
1 * 3 = 3 2 * 3 = 6 3 * 3 = 9
...

*
**
***
*/
class Demo3_For99 {
	public static void main(String[] args) {
		for (int i = 1;i <= 9 ;i++ ) {					//行数
			for (int j = 1;j <= i ;j++ ) {				//列数
				System.out.print(j + "*" + i + "=" + (i * j) + "\t" );
			}
			System.out.println();
		}

		System.out.println("\"");				//转义双引号
		System.out.println('\'');				//转义单引号
	}
}
```
- B:代码优化

- 注意：
  	'\x' x表示任意，\是转义符号,这种做法叫转移字符。
  	

  ```java
  '\t'	tab键的位置
  '\r'	回车
  '\n'	换行
  '\"'
  '\''
  ```

  

### 04.14_Java语言基础(控制跳转语句break语句)

- A:break的使用场景
  - 只能在switch和循环中 
```java
/*
* A:break的使用场景
	* 只能在switch和 循环 中 
*/
class Demo1_Break {
	public static void main(String[] args) {
		for (int x = 1;x <= 10 ;x++ ) {
			if (x == 4) {
				break;							//跳出循环
			}

			System.out.println("x = " + x);
		}
	}
}

```

### 04.15_Java语言基础(控制跳转语句continue语句)

- A:continue的使用场景
  - 只能在循环中 
```java
/*
* A: continue的使用场景
	* 只能在循环中 
*/
class Demo2_Continue {
	public static void main(String[] args) {
		for (int x = 1;x <= 10 ;x++ ) {
			if (x == 4) {
				continue;							//终止本次循环不会输出4,继续下次循环
			}

			System.out.println("x = " + x);
		}
	}
}
```
输出结果:
```java
x = 1
x = 2
x = 3
x = 5
x = 6
x = 7
x = 8
x = 9
x = 10
请按任意键继续. . .

```
### 04.16_Java语言基础(控制跳转语句标号)

- 标号:标记某个循环对其控制
- 标号组成规则:其实就是合法的标识符
```java
class Demo3_Mark {										//mark 标记
	public static void main(String[] args) {
		outer: for (int i = 1;i <= 10 ;i++ ) {		//a就是标号,只要是合法的标识符即可
			System.out.println("i = " + i);
			inner: for (int j = 1;j <= 10 ;j++ ) {
				System.out.println("j = " + j);
				break outer;
			}
		}

		System.out.println("大家好");
		http://www.heima.com
		System.out.println("才是真的好");  //注意的是http:是一个标号,后面的是一个单行注释
	}
}

```
### 04.17_Java语言基础(控制调整语句练习)

- A:练习题
```java
for(int x=1; x<=10; x++) {
  		if(x%3==0) {
  			//在此处填写代码
  		}
  		System.out.println(“Java基础班”);
  	}
  ```

  ```
  我想在控制台输出2次:“Java基础班“
  我想在控制台输出7次:“Java基础班“
  我想在控制台输出13次:“Java基础班“	
  ```
实现
```java
/*
		for(int x=1; x<=10; x++) {
			if(x%3==0) {
				//在此处填写代码
			}
			System.out.println(“Java基础班”);
		}
		
		我想在控制台输出2次:“Java基础班“
		我想在控制台输出7次:“Java基础班“
		我想在控制台输出13次:“Java基础班“	
*/
class Test1 {
	public static void main(String[] args) {
		for(int x=1; x<=10; x++) {
			if(x%3==0) {
				//break;						//我想在控制台输出2次:“Java基础班“
				//continue;						//我想在控制台输出7次:“Java基础班“
				System.out.println("Java基础班");//我想在控制台输出13次:“Java基础班“	
			}
			System.out.println("Java基础班");//我想在控制台输出13次:“Java基础班“
		}
	}
}
```

### 04.18_Java语言基础(控制跳转语句return语句)

- A:return的作用
  - 返回
  - 其实它的作用不是结束循环的，而是结束方法的。
```java
class Demo4_Return {
	public static void main(String[] args) {
		for (int i = 1;i <= 10 ;i++ ) {
			if (i == 4) {				
				//break;						//停止循环
				return;							//返回的意思,用来返回方法
			}
		}

		System.out.println("循环结束了");
	}
}

```
- B:案例演示
  - return和break以及continue的区别?
  - return是结束方法
  - break是跳出循环
  - continue是终止本次循环继续下次循环

### 04.19_Java语言基础(方法概述和格式说明)

- A:为什么要有方法
  - 提高代码的复用性 
- B:什么是方法
  - 完成特定功能的代码块。 
- C:方法的格式
- 修饰符 返回值类型 方法名(参数类型 参数名1,参数类型 参数名2...) {
  		方法体语句;
  		return 返回值; 
  	} 
- D:方法的格式说明
  - 修饰符：目前就用 public static。后面我们再详细的讲解其他的修饰符。
  - 返回值类型：就是功能结果的数据类型。
  - 方法名：符合命名规则即可。方便我们的调用。
  - 参数：
    - 实际参数：就是实际参与运算的。
    - 形式参数；就是方法定义上的，用于接收实际参数的。
  - 参数类型：就是参数的数据类型
  - 参数名：就是变量名
  - 方法体语句：就是完成功能的代码。
  - return：结束方法的。
  - 返回值：就是功能的结果，由return带给调用者。 

### 04.20_Java语言基础(方法之求和案例及其调用)

- A:如何写一个方法
  - 1,明确返回值类型
  - 2,明确参数列表 
- B:案例演示
  - 需求：求两个数据之和的案例
```java
/*
* A:如何写一个方法
	* 1,明确返回值类型
	* 2,明确参数列表 
* B:案例演示
	* 需求：求两个数据之和的案例
* C:方法调用图解
*/
class Demo2_Sum {
	public static void main(String[] args) {
		/*int a = 10;
		int b = 20;
		int sum = a + b;
		System.out.println(sum);

		int c = 30;
		int d = 40;
		int sum2 = c + d;
		System.out.println(sum2);*/

		int sum = add(10,20);
		System.out.println(sum);

		//add(30,40);						//有返回值方法的单独调用,没有意义
		System.out.println(add(30,40));		//这样调用是可以,but如果需要用这个结果不推荐这样调用

		//盘子 = 炒菜(地沟油,苏丹红,镉大米,烂白菜);
	}

	/*
	求两个整数的和
	1,整数的和结果应该还是整数
	2,有两个未知内容参与运算

	如何写方法
	1,明确返回值类型
	2,明确参数列表

	* 修饰符：目前就用 public static。后面我们再详细的讲解其他的修饰符。
		* 返回值类型：就是功能结果的数据类型。
		* 方法名：符合命名规则即可。方便我们的调用。
		* 参数：
			* 实际参数：就是实际参与运算的。
			* 形式参数；就是方法定义上的，用于接收实际参数的。
		* 参数类型：就是参数的数据类型
		* 参数名：就是变量名
		* 方法体语句：就是完成功能的代码。
		* return：结束方法的。
		* 返回值：就是功能的结果，由return带给调用者。
	*/
	public static int add(int a,int b) {			//int a = 10,int b = 20
		int sum = a + b;
		return sum;									//如果有返回值必须用return语句带回
	}

	/*
	盘子 炒菜(油,调料,米,菜) {
		炒菜的动作
		return 一盘菜;
	}
	*/

}

```
- C:方法调用图解
![image.png](https://upload-images.jianshu.io/upload_images/14555448-dc8e47a8b13c778a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 04.21_Java语言基础(方法的注意事项)

- A:方法调用(有具体返回值)
  - a:单独调用,一般来说没有意义，所以不推荐。
  - b:输出调用,但是不够好。因为我们可能需要针对结果进行进一步的操作。
  - c:赋值调用,推荐方案。
- B:案例演示
  - a:方法不调用不执行
  - b:方法与方法是平级关系，不能嵌套定义
  - c:方法定义的时候参数之间用逗号隔开
  - d:方法调用的时候不用在传递数据类型
  - e:如果方法有明确的返回值，一定要有return带回一个值

### 04.22_Java语言基础(方法的练习)

- A:案例演示
  - 需求：键盘录入两个数据，返回两个数中的较大值

- B:案例演示
  - 需求：键盘录入两个数据，比较两个数是否相等     
```java
/*
* A:案例演示
	* 需求：键盘录入两个数据，返回两个数中的较大值
* B:案例演示
	* 需求：键盘录入两个数据，比较两个数是否相等     
*/
import java.util.Scanner;
class Test1_Method {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);				//创建键盘录入对象
		System.out.println("请输入第一个整数:");
		int x = sc.nextInt();								//将键盘录入的整数存储在x中
		System.out.println("请输入第二个整数:");
		int y = sc.nextInt();								//将键盘录入的整数存储在y中

		//int max = getMax(x,y);
		//System.out.println(max);

		boolean b = isEquals(x,y);
		System.out.println(b);
	}

	/*
	返回连个整数的较大值
	1,明确返回值类型 int
	2,明确参数列表 int a,int b
	*/
	public static int getMax(int a,int b) {
		return a > b ? a : b;
	}

	/*
	判断两个整数是否相等
	1,明确返回值类型 boolean
	2,明确参数列表 int a,int b
	*/
	public static boolean isEquals(int a,int b) {		//isEquals 是否相等
		return a == b;
	}
}

```
### 04.23_Java语言基础(方法之输出星形及其调用)

- A:案例演示
  - 需求：根据键盘录入的行数和列数，在控制台输出星形
```java
/*
* A:案例演示
	* 需求：根据键盘录入的行数和列数，在控制台输出星形
* B:方法调用：
	* 单独调用
	* 输出调用(错误)
	* 赋值调用(错误)
*/
import java.util.Scanner;
class Demo3_Method {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);			//创建键盘录入对象
		System.out.println("请输入行数:");
		int row = sc.nextInt();							//将键盘录入的行数存储在row中
		System.out.println("请输入列数:");
		int column = sc.nextInt();						//将键盘录入的列数存储在column中
		
		//System.out.println(print(row,column));		//错误: 此处不允许使用 '空' 类型,返回值是void的方法不能输出调用
		//返回值是void的方法只能单独调用
		print(row,column);
	}

	/*
	在控制台输出矩形星形
	1,明确返回值类型,经分析没有具体的返回值类型,void
	2,明确参数列表int a,int b
	*/

	public static void print(int a,int b) {
		for (int i = 1;i <= a ;i++ ) {					//行数
			for (int j = 1;j <= b ;j++ ) {				//列数
				System.out.print("*");
			}
			System.out.println();
		}

		//return ;										//如果返回值类型是void,return可以省略,即使省略系统也会默认给加上,形式是return;
	}
}
```
- B:方法调用：(无返回值,void)
  - 单独调用
  - 输出调用(错误)
  - 赋值调用(错误)

### 04.24_Java语言基础(方法的练习)

- A:案例演示
  - 需求：根据键盘录入的数据输出对应的乘法表
```java
/*
* A:案例演示
	* 需求：根据键盘录入的数据输出对应的乘法表
*/
import java.util.Scanner;
class Test2_Method {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);		//创建键盘录入对象
		System.out.println("请录入一个整数,范围在1-9之间");
		int num = sc.nextInt();						//将键盘录入的整数存储在num中
		print99(num);
	}

	/*
	打印99乘法表
	1,返回值类型void
	2,参数列表,int a
	*/

	public static void print99(int a) {
		for (int i = 1;i <= a ;i++ ) {					//行数
			for (int j = 1;j <= i ;j++ ) {				//列数
				System.out.print(j + "*" + i + "=" + (i * j) + "\t" );
			}
			System.out.println();
		}
	}
}
```
### 04.25_Java语言基础(方法重载概述和基本使用)

- A:方法重载概述
  - 求和案例
    - 2个整数
    - 3个整数
    - 4个整数
- B:方法重载：
  - 在同一个类中，方法名相同，参数列表不同。与返回值类型无关。
  - 参数列表不同：
    - A:参数个数不同
    - B:参数类型不同
    - C:参数的顺序不同(算重载,但是在开发中不用)
```java
/*
重载:方法名相同,参数列表不同,与返回值类型无关
重载的分类
1,参数个数不同
2,参数类型不同
	顺序不同算重载,但是在开发中不用
*/
class Demo4_Overload {						//overload重载
	public static void main(String[] args) {

		double sum1 = add(10,20.1);
		System.out.println(sum1);

		int sum2 = add(10,20,30);
		System.out.println(sum2);

		double sum3 = add(12.3,13);
		System.out.println(sum3);
	}

	/*
	求两个整数的和
	1,返回值类型int
	2,参数列表 int a,int b
	*/

	public static double add(int a,double b) {
		return a + b;
	}

	/*
	求三个整数的和
	1,返回值类型int
	2,参数列表 int a,int b,int c
	*/

	public static int add(int a,int b,int c) {
		return a + b + c;
	}

	/*
	求两个小数的和
	1,返回值类型double
	2,参数列表 double a,double b
	*/

	public static double add(double a,int b) {
		return a + b;
	}
}
```
### 04.26_Java语言基础(方法重载练习比较数据是否相等)

- A:案例演示
  - 需求：比较两个数据是否相等。
  - 参数类型分别为两个int类型，两个double类型，并在main方法中进行测试
```java
/*
* A:案例演示
	* 需求：比较两个数据是否相等。
	* 参数类型分别为两个int类型，两个double类型，并在main方法中进行测试

*/
class Test3_Overload {
	public static void main(String[] args) {
		boolean b1 = isEquals(10,10);
		System.out.println(b1);

		boolean b2 = isEquals(10.5,10);
		System.out.println(b2);
	} 

	/*
	比较两个数据是否相等
	1,返回值类型boolean
	2,参数列表int a,int b
	*/

	public static boolean isEquals(int a,int b) {
		return a == b;
	}

	/*
	比较两个数据是否相等
	1,返回值类型boolean
	2,参数列表double a,double b
	*/

	public static boolean isEquals(double a,double b) {
		return a == b;
	}
}
```
