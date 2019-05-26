### 03.01_Java语言基础(逻辑运算符的基本用法)(掌握)

- A:逻辑运算符有哪些
  - &,|,^,!
  - &&,|| 
- B:案例演示
逻辑与:
```java
class data 
{
	public static void main(String[] args) 
	{
		//逻辑与 & 并且and 遇false则false
		int a = 10;
		int b = 20;
		int c = 30;
		System.out.println(a < b & b < c);			//true & true = true
		System.out.println(a < b & b > c);				//true & false = false
		System.out.println(a > b & b < c);				//false & true = false
		System.out.println(a > b & b > c);				//false & false = false

	}
}

```
逻辑或:
```
class data 
{
	public static void main(String[] args) 
	{
		//逻辑或 或or 遇true则true
		int a = 10;
		int b = 20;
		int c = 30;
		System.out.println(a < b | b < c);				//true | true = true
		System.out.println(a < b | b > c);				//true | false = true
		System.out.println(a > b | b < c);				//false | true = true
		System.out.println(a > b | b > c);				//false | flase = false
	}
}

```
逻辑异或:
```java
class data 
{
	public static void main(String[] args) 
	{
		//逻辑或 或or 遇true则true
		int a = 10;
		int b = 20;
		int c = 30;
		//逻辑异或 ^ 两边相同为false,两边不同为true
		System.out.println(a < b ^ b < c);				//true ^ true = false
		System.out.println(a < b ^ b > c);				//true ^ false = true
		System.out.println(a > b ^ b < c);				//false ^ true = true
		System.out.println(a > b ^ b > c);				//false ^ flase = false
	}
}


```
逻辑非:
```java
class data 
{
	public static void main(String[] args) 
	{
		//逻辑非!
		System.out.println(!true);  //false
		System.out.println(!!true); //true
	}
}

```
- 逻辑运算符的基本用法
- 注意事项：
  - a:逻辑运算符一般用于连接boolean类型的表达式或者值。
  - b:表达式：就是用运算符把常量或者变量连接起来的符合java语法的式子。
    - 算术表达式：a + b
    - 比较表达式：a == b(条件表达式)
- C:结论：
- &逻辑与:有false则false。
- |逻辑或:有true则true。
- ^逻辑异或:相同为false，不同为true。
- !逻辑非:非false则true，非true则false。
  - 特点：偶数个不改变本身。

### 03.02_Java语言基础(逻辑运算符&&和&的区别)(掌握)

- A:案例演示
  - &&和&的区别?
    - a:最终结果一样。
    - b:&&具有短路效果。左边是false，右边不执行。
    - &是无论左边是false还是true,右边都会执行
使用&时,两边都执行,因此x,y的值都加一
```java
class data 
{
	public static void main(String[] args) 
	{
		int x = 3;
		int y = 4;
		System.out.println((++x == 3) & (++y == 4));	//false & false = false
		System.out.println("x = " + x);					//x = 4
		System.out.println("y = " + y);					//y = 5
}
}

```
执行结果:

```java
false
x = 4
y = 5
请按任意键继续. . .
```
使用&&时:右边不执行,因此只有x的值加一
```java
class data 
{
	public static void main(String[] args) 
	{
		int x = 3;
		int y = 4;
		System.out.println((++x == 3) && (++y == 4));	//false & false = false
		System.out.println("x = " + x);					//x = 4
		System.out.println("y = " + y);					//y = 5
}
}
```
执行结果:
```java
false
x = 4
y = 4
请按任意键继续. . .
```
- B:同理||和|的区别?(学生自学)
- C:开发中常用谁?
  - &&,||,!

### 03.03_Java语言基础(位运算符的基本用法1)(了解)

- A:位运算符有哪些
  - &,|,^,~ ,>>,>>>,<<
- B:案例演示
  - 位运算符的基本用法1
  - &,|,^,~ 的用法
  - &:有0则0
  - |:有1则1
  - ^:相同则0，不同则1
  - ~:按位取反
```java
class Demo1_Operator {
	public static void main(String[] args) {
		/*
		* &,|,^,~ 的用法
		* &:有0则0
		* |:有1则1
		* ^:相同则0，不同则1
		* ~:按位取反
		*/

		System.out.println(6 & 3);				//2   全部转换为二进制进行对应位置的逻辑运算
		System.out.println(6 | 3);				//7
		System.out.println(6 ^ 3);				//5	
		System.out.println(~6);					//-7?					
	}
}
/*
	110
&	011
-----------
    010

	110
|	011
-----------
    111

	110
^	011
-----------
    101

~	00000000 00000000 00000000 00000110		6的原码反码补码都是本身
	11111111 11111111 11111111 11111001		对6取反(补码进行运算)
-	00000000 00000000 00000000 00000001     补码减1得到反码
---------------------------------------
	11111111 11111111 11111111 11111000		反码(取反得到原码)
	10000000 00000000 00000000 00000111		原码(-7) (原码输出)
*/
```



### 03.04_Java语言基础(位异或运算符的特点及面试题)(掌握)

- A:案例演示
  - 位异或运算符的特点
  - ^的特点：一个数据对另一个数据位异或两次，该数本身不变。

- B:面试题：
  - 请自己实现两个整数变量的交换
  - 注意：以后讲课的过程中，我没有明确指定数据的类型，默认int类型。
```java
class Demo2_Operator {
	public static void main(String[] args) {
		/*
		* 位异或运算符的特点

		* ^的特点：一个数据对另一个数据位异或两次，该数本身不变。
		*/

		System.out.println(5 ^ 10 ^ 10);
		System.out.println(5 ^ 10 ^ 5);  //不变得是少的那个

		/*
		* 请自己实现两个整数变量的交换(不需要定义第三方变量)
		* 注意：以后讲课的过程中，我没有明确指定数据的类型，默认int类型。
		*/

		int x = 10;
		int y = 5;

		//需要第三方变量,开发推荐用这种
		/*int temp;
		temp = x;
		x = y;
		y = temp;*/

		//不需要定义第三方变量,有弊端,有可能会超出int的取值范围
		/*x = x + y;				//10 + 5 = 15
		y = x - y;				//15 - 5 = 10
		x = x - y;				//15 - 10 = 5*/

		//不需要第三方变量,通过^来做
		x = x ^ y;				// 10 ^ 5 
		y = x ^ y;				// 10 ^ 5 ^ 5	y = 10
		x = x ^ y;				// 10 ^ 5 ^ 10  x = 5

		System.out.println("x = " + x + ",y = " + y);
	}
}

```
### 03.05_Java语言基础(位运算符的基本用法2及面试题)(了解)

- A:案例演示 >>,>>>,<<的用法:

  - <<:左移	左边最高位丢弃，右边补齐0

  - > > :右移	最高位是0，左边补齐0;最高为是1，左边补齐1

  - > > > :无符号右移 无论最高位是0还是1，左边补齐0

  - 最有效率的算出2 * 8的结果
```java
class Demo3_Operator {
	public static void main(String[] args) {
		/*
		*  <<:左移	左边最高位丢弃，右边补齐0
		*  >>:右移	最高位是0，左边补齐0;最高为是1，左边补齐1
		*  >>>:无符号右移 无论最高位是0还是1，左边补齐0
		*  最有效率的算出2 * 8的结果
		*/

		//左移,向左移动几位就是乘以2的几次幂
		System.out.println(12 << 1);		//24
		System.out.println(12 << 2);		//48

		/*
		00000000 00000000 00000000 00001100		12的补码
	 (0)0000000 00000000 00000000 000011000		24的补码
	(00)000000 00000000 00000000 0000110000		48的补码
		*/

		//右移,向右移动几位就是除以2的几次幂
		System.out.println(12 >> 1);
		System.out.println(12 >> 2);

		/*
		00000000 00000000 00000000 00001100		12的补码
		000000000 00000000 00000000 0000110(0)	6
		0000000000 00000000 00000000 000011(00) 3
		*/

		//最有效率的算出2 * 8的结果
		System.out.println(2 << 3);
	}
}
```

### 03.06_Java语言基础(三元运算符的基本用法)(掌握)

- A:三元运算符的格式
- (关系表达式) ? 表达式1 : 表达式2;
- B:三元运算符的执行流程 
- C:案例演示
  - 获取两个数中的最大值
```java
class Demo1_Operator {
	public static void main(String[] args) {
		//(关系表达式) ? 表达式1 : 表达式2;
		int x = 10;
		int y = 5;
		int z;
		z = (x > y) ? x : y;    //如果x>y表达式1,否则表达式2

		System.out.println("z = " + z);     
	}
}

```

### 03.07_Java语言基础(三元运算符的练习)(掌握)

- A:案例演示
  - 比较两个整数是否相同
```java
class data 
{
	public static void main(String[] args) 
	{
		//比较两个整数是否相同

		int x = 10;
		int y = 10;

		//boolean b = (x == y) ? true : false;
		boolean b = (x == y);
		System.out.println("b = " +  b);
	}
}
```
- B:案例演示
  - 获取三个整数中的最大值
```java
class data 
{
	public static void main(String[] args) 
	{
		//获取三个整数中的最大值
		int a = 10;
		int b = 20;
		int c = 30;

		//先比较任意两个数的值,找出这两个数中的最大值
		int temp = (a > b) ? a : b;
		//用前两个数的最大值与第三个数比较,获取最大值
		int max = (temp > c) ? temp : c;
		System.out.println("max =" + max);
	}
}
```
### 03.08_Java语言基础(键盘录入的基本格式讲解)(掌握)

- A:为什么要使用键盘录入数据
  - a:为了让程序的数据更符合开发的数据
  - b:让程序更灵活一下
- B:如何实现键盘录入呢?
  - 先照格式来。
  - a:导包
    - 格式：
      - ` import java.util.Scanner; ` 
    - 位置：
      - 在class上面。
  - b:创建键盘录入对象
    - 格式：
      - ` Scanner sc = new Scanner(System.in); ` 本质就是创建一个对象
  - c:通过对象获取数据	
    - 格式：
      - `int x = sc.nextInt();`
- C:案例演示
  - 键盘录入1个整数，并输出到控制台。
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		Scanner sc =new Scanner(System.in);
		System.out.println("请输入一个整数");
		int x = sc.nextInt();
		System.out.println(x);
	}
}
```

  - 键盘录入2个整数，并输出到控制台。
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		Scanner sc =new Scanner(System.in);
		System.out.println("请输入一个整数");
		int x = sc.nextInt();
		int y =sc.nextInt();
		System.out.println("x= "+ x+"y ="+y);
	}
}
```

### 03.09_Java语言基础(键盘录入的练习1)(掌握)

- A:案例演示
  - 键盘录入练习：键盘录入两个数据，并对这两个数据求和，输出其结果
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		//键盘录入练习：键盘录入两个数据，并对这两个数据求和，输出其结果
		Scanner sc =new Scanner(System.in);
		System.out.println("请输入第一个整数:");
		int x = sc.nextInt();					//将键盘录入的数据存储在x中
		System.out.println("请输入第二个整数:");
		int y = sc.nextInt();					//将键盘录入的数据存储在y中
		int sum = x + y;

		System.out.println("求和的结果: "+sum);
	}
}
```
- B:案例演示
  - 键盘录入练习：键盘录入两个数据，获取这两个数据中的最大值
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		//键盘录入练习：键盘录入两个数据，并对这两个数据求和，输出其结果
		Scanner sc =new Scanner(System.in);
		System.out.println("请输入第一个整数:");
		int x = sc.nextInt();					//将键盘录入的数据存储在x中
		System.out.println("请输入第二个整数:");
		int y = sc.nextInt();					//将键盘录入的数据存储在y中

		int max = (x > y) ? x : y;				//获取x和y中的最大值
		System.out.println("max = " + max);
	}
}
```

### 03.10_Java语言基础(键盘录入的练习2)(掌握)

- A:案例演示
  - 键盘录入练习：键盘录入两个数据，比较这两个数据是否相等
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		//键盘录入练习：键盘录入两个数据，比较这两个数据是否相等
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入第一个整数:");
		int x = sc.nextInt();						//将键盘录入的数据存储在x中
		System.out.println("请输入第二个整数:");
		int y = sc.nextInt();						//将键盘录入的数据存储在y中

		//boolean b = (x == y)? true : false;
		boolean b = (x == y);
		System.out.println(b);
	}
}
```
- B:案例演示
  - 键盘录入练习：键盘录入三个数据，获取这三个数据中的最大值
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{

		Scanner sc = new Scanner(System.in);
		//键盘录入练习：键盘录入三个数据，获取这三个数据中的最大值

		System.out.println("请输入第一个整数:");
		int x = sc.nextInt();						//将键盘录入的数据存储在x中
		System.out.println("请输入第二个整数:");
		int y = sc.nextInt();						//将键盘录入的数据存储在y中
		System.out.println("请输入第三个整数:");
		int z = sc.nextInt();						//将键盘录入的数据存储在y中

		//定义临时变量记录住比较出前两个变量中的最大值
		int temp = (x > y) ? x : y;
		//将比较后的结果与第三个变量中的值比较,比较出三个数中的最大值
		int max = (temp > z) ? temp : z;
		System.out.println(max);
	}
}
```
### 03.11_Java语言基础(顺序结构语句)(了解)

- A:什么是流程控制语句
  - 流程控制语句：可以控制程序的执行流程。
- B:流程控制语句的分类
  - 顺序结构
  - 选择结构
  - 循环结构
- C:执行流程：
  - 从上往下，依次执行。
- D:案例演示
  - 输出几句话看效果即可
```java
class Demo1_Sequence {							//sequence 顺序
	public static void main(String[] args) {
		System.out.println("Hello World!11111");
		System.out.println("Hello World!3333");
		System.out.println("Hello World!22222");
		System.out.println("Hello World!44444");
	}
}

```
执行的结果:
```java
Hello World!11111
Hello World!3333
Hello World!22222
Hello World!44444
请按任意键继续. . .
```

### 03.12_Java语言基础(选择结构if语句格式1及其使用)(掌握)

- A:选择结构的分类
  - if语句
  - switch语句
- B:if语句有几种格式
  - 格式1
  - 格式2
  - 格式3
- C:if语句的格式1
- if(比较表达式) {
  		语句体;
  	}
- D:执行流程：
  - 先计算比较表达式的值，看其返回值是true还是false。
  - 如果是true，就执行语句体；
  - 如果是false，就不执行语句体；

### 03.13_Java语言基础(选择结构if语句注意事项)(掌握)

- A:案例演示
  - a:比较表达式无论简单还是复杂，结果必须是boolean类型
  - b:if语句控制的语句体如果是一条语句，大括号可以省略；
    - 如果是多条语句，就不能省略。建议永远不要省略。
  - c:一般来说：有左大括号就没有分号，有分号就没有左大括号
```java
/*
* C:if语句的格式1
* 
		if(比较表达式) {
			语句体;
		}
* D:执行流程：
	* 先计算比较表达式的值，看其返回值是true还是false。
	* 如果是true，就执行语句体；
	* 如果是false，就不执行语句体；
*/
class Demo1_If {
	public static void main(String[] args) {
		int age = 19;

		if (age >= 18) {
			System.out.println("可以浏览本网站");
		}

		System.out.println("完了");
	}
}

```

### 03.14_Java语言基础(选择结构if语句格式2及其使用)(掌握)

- A:if语句的格式2
- if(比较表达式) {
  		语句体1;
  	}else {
  		语句体2;
  	}
- B:执行流程：
  - 首先计算比较表达式的值，看其返回值是true还是false。
  - 如果是true，就执行语句体1；
  - 如果是false，就执行语句体2；
- C:案例演示
  - a:获取两个数据中较大的值
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{

		int a = 0;
		if (a == 1) {
			System.out.println("男厕所欢迎您");
		}else {
			System.out.println("女厕所欢迎您");
		}
		
		//a:获取两个数据中较大的值
		int x = 10;
		int y = 20;
		int z;

		if (x > y) {
			z = x;
		}else {
			z = y;
		}

		System.out.println(z);
	}
}
```
  - b:判断一个数据是奇数还是偶数,并输出是奇数还是偶数
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{

		//b:判断一个数据是奇数还是偶数,并输出是奇数还是偶数
		int num = 11;
		if (num % 2 == 0) {
			System.out.println(num + "是一个偶数");
		}else {
			System.out.println(num + "是一个奇数");
		}
	}
}
```
  - 注意事项：else后面是没有比较表达式的，只有if后面有。

### 03.15_Java语言基础(if语句的格式2和三元的相互转换问题)(掌握)

- A:案例演示
  - if语句和三元运算符完成同一个效果
```java
/*
* A:案例演示
	* if语句和三元运算符完成同一个效果
* B:案例演示
	* if语句和三元运算符的区别
	
	* 三元运算符实现的，都可以采用if语句实现。反之不成立。
	
	* 什么时候if语句实现不能用三元改进呢?
		* 当if语句控制的操作是一个输出语句的时候就不能。
		* 为什么呢?因为三元运算符是一个运算符，运算符操作完毕就应该有一个结果，而不是一个输出。

*/
class Demo4_If {
	public static void main(String[] args) {
		int x = 10;
		int y = 20;
		int z;

		if (x > y) {
			z = x;
			System.out.println(x + "是最大值");
		}else {
			z = y;
			System.out.println(y + "是最大值");
		}

		System.out.println(z);

		int a = 20;
		int b = 30;

		int c = (a > b)? a : b;
		System.out.println(c);

	}
}

```
- B:案例演示
  - if语句和三元运算符的区别
  - 三元运算符实现的，都可以采用if语句实现。反之不成立。
  - 什么时候if语句实现不能用三元改进呢?
    - 当if语句控制的操作是一个输出语句的时候就不能。
    - 为什么呢?因为三元运算符是一个运算符，运算符操作完毕就应该有一个结果，而不是一个输出。

### 03.16_Java语言基础(选择结构if语句格式3及其使用)(掌握)

- A:if语句的格式3：
- if(比较表达式1) {
  		语句体1;
  	}else if(比较表达式2) {
  		语句体2;
  	}else if(比较表达式3) {
  		语句体3;
  	}
  	...
  	else {
  		语句体n+1;
  	}
- B:执行流程：
  - 首先计算比较表达式1看其返回值是true还是false，
  - 如果是true，就执行语句体1，if语句结束。
  - 如果是false，接着计算比较表达式2看其返回值是true还是false，
  - 如果是true，就执行语句体2，if语句结束。
  - 如果是false，接着计算比较表达式3看其返回值是true还是false，
  - 如果都是false，就执行语句体n+1。
- C:注意事项:最后一个else可以省略,但是建议不要省略,可以对范围外的错误值提示 
```java
/*
* A:if语句的格式3：
* 
		if(比较表达式1) {
			语句体1;
		}else if(比较表达式2) {
			语句体2;
		}else if(比较表达式3) {
			语句体3;
		}
		...
		else {
			语句体n+1;
		}
* B:执行流程：
	* 首先计算比较表达式1看其返回值是true还是false，
	* 如果是true，就执行语句体1，if语句结束。
	* 如果是false，接着计算比较表达式2看其返回值是true还是false，
	
	* 如果是true，就执行语句体2，if语句结束。
	* 如果是false，接着计算比较表达式3看其返回值是true还是false，
	
	* 如果都是false，就执行语句体n+1。
* C:注意事项:最后一个else可以省略,但是建议不要省略,可以对范围外的错误值提示 
*/
class Demo5_If {
	public static void main(String[] args) {
		int x = 4;
		if (x == 1) {
			System.out.println("男厕所欢迎您");
		}else if (x == 0) {
			System.out.println("女厕所欢迎您");
		}else {
			System.out.println("无法识别您的性别");
		}
	}
}

```

### 03.17_Java语言基础(选择结构if语句格式3练习)(掌握)

- A:练习1
- 需求：键盘录入一个成绩，判断并输出成绩的等级。
  	90-100 优
  	80-89  良
  	70-79  中
  	60-69  及
  	0-59   差
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);

		//需求：键盘录入一个成绩，判断并输出成绩的等级。
		System.out.println("请输入学生成绩范围在1到100之间");
		int x = sc.nextInt();

		if (x >= 90 && x <= 100) {
			System.out.println("优");
		}else if (x >= 80 && x <= 89 ) {
			System.out.println("良");
		}else if (x >= 70 && x <= 79 ) {
			System.out.println("中");
		}else if (x >= 60 && x <= 69 ) {
			System.out.println("及");
		}else if (x >= 0 && x <= 59 ) {
			System.out.println("差");
		}else {
			System.out.println("成绩录入错误");
		}
	}
}
```
- B:练习2
  - 需求：
    - 键盘录入x的值，计算出y的并输出。
    - x>=3	y = 2 * x + 1;
    - -1<x<3	y = 2 * x;
    - x<=-1	y = 2 * x - 1;
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);

		//需求： 键盘录入x的值，计算出y的并输出
		System.out.println("请输入一个整数:");
		int x = sc.nextInt();
		int y = 0;
		if (x >= 3) {
			y = 2 * x + 1;
		}else if (x > -1 && x < 3) {
			y = 2 * x;
		}else if (x <= -1) {
			y = 2 * x - 1;
		}

		System.out.println(y);
	}
}
```
### 03.18_Java语言基础(选择结构if语句的嵌套使用)(掌握)

- A:案例演示
  - 需求：获取三个数据中的最大值
  - if语句的嵌套使用。
```java
/*
* A:案例演示
	* 需求：获取三个数据中的最大值
	* if语句的嵌套使用。
*/
class Demo6_IfIf {
	public static void main(String[] args) {
		int a = 40;
		int b = 50;
		int c = 30;
		
		if (a > b) {
			if (a > c) {
				System.out.println(a + "是最大值");
			}else {
				System.out.println(c + "是最大值");
			}

		}else {	//b >= a
			if (b > c) {
				System.out.println(b + "是最大值");
			}else {
				System.out.println(c + "是最大值");
			}
		}
	}
}

```

### 03.19_Java语言基础(选择结构switch语句的格式及其解释)(掌握)

- A:switch语句的格式
- switch(表达式) {
  	      case 值1：
  			语句体1;
  			break;
  		    case 值2：
  			语句体2;
  			break;
  		    …
  		    default：	
  			语句体n+1;
  			break;
      }
- B:switch语句的格式解释
- C:面试题
  - byte可以作为switch的表达式吗?
  - long可以作为switch的表达式吗?
  - String可以作为switch的表达式吗?
- C:执行流程
  - 先计算表达式的值
  - 然后和case后面的匹配，如果有就执行对应的语句，否则执行default控制的语句
```java
class Demo1_Switch {
	public static void main(String[] args) {
		/*
		* A:switch语句的格式
		*		int x = 10;
				switch(表达式) {		//基本数据类型可以接收byte,short,char,int
					  case 值1：		//引用数据类型可以接收枚举(JDK1.5)String字符串(JDK1.7)
						语句体1;
						break;
						case 值2：
						语句体2;
						break;
						…
						default：	
						语句体n+1;
						break;
				}
		 
		* B:switch语句的格式解释
		* C:面试题
			* byte可以作为switch的表达式吗?   byte可以啊
			* long可以作为switch的表达式吗?    long不可以但是int可以
			* String可以作为switch的表达式吗?    在1.7版本以后可以
		* C:执行流程
			* 先计算表达式的值
			* 然后和case后面的匹配，如果有就执行对应的语句，否则执行default控制的语句
		*/

		String name = "rose";
		String gender = "男士";
		switch (gender) {
		case "男士":
			System.out.println(name + "是一位" + gender + "喜欢吃饭睡觉打dota");
		break;
		case "女士":
			System.out.println(name + "是一位" + gender + "喜欢逛街购物美容");
		break;
		default:
			System.out.println(name + "是一位" + gender + "打雌性激素维持美貌容颜");
		break;
		}
	}
}

```

### 03.20_Java语言基础(选择结构switch语句的练习)(掌握)

- A:整数(给定一个值,输出对应星期几)
```java
class Test1_Switch {
	public static void main(String[] args) {
		//* A:整数(给定一个值,输出对应星期几)
		int week = 1;
		switch (week) {
		case 1:
			System.out.println("星期一");
		break;
		case 2:
			System.out.println("星期二");
		break;
		case 3:
			System.out.println("星期三");
		break;
		case 4:
			System.out.println("星期四");
		break;
		case 5:
			System.out.println("星期五");
		break;
		case 6:
			System.out.println("星期六");
		break;
		case 7:
			System.out.println("星期日");
		break;
		default:
			System.out.println("对不起没有对应的星期");
		break;   //最后一个breake可以省略,但是前面的不能省略否则会出现break穿透,default可以写在前面但是不建议这么做
		}
	}
}

```

### 03.21_Java语言基础(选择结构switch语句的注意事项)(掌握)

- A:案例演示
  - a:case后面只能是常量，不能是变量，而且，多个case后面的值不能出现相同的

  - b:default可以省略吗?
    - 可以省略，但是不建议，因为它的作用是对不正确的情况给出提示。
    - 特殊情况：
      - case就可以把值固定。
      - A,B,C,D
  - c:break可以省略吗?
    - 最后一个可以省略,其他最好不要省略
    - 会出现一个现象：case穿透。
    - 最终我们建议不要省略
  - d:default一定要在最后吗?
    - 不是，可以在任意位置。但是建议在最后。
  - e:switch语句的结束条件
    - a:遇到break就结束了
    - b:执行到switch的右大括号就结束了

### 03.22_Java语言基础(选择结构switch语句练习)(掌握)

- A:看程序写结果：
- int x = 2;
  	int y = 3;
  	switch(x){
  		default:
  			y++;
  			break;
  		case 3:
  			y++;
  		case 4:
  			y++;
  	}
  	System.out.println("y="+y);
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		// A:看程序写结果：

		int x = 2;
		int y = 3;
		switch(x){ 
			default:
				y++;
				break;
			case 3:
				y++;
			case 4:
				y++;
		}
		System.out.println("y="+y);
		// defult y=4
	}
}
```
- B:看程序写结果：
- int x = 2;
  	int y = 3;
  	switch(x){
  		default:
  			y++;
  		case 3:
  			y++;
  		case 4:
  			y++;
  	}
  	System.out.println("y="+y);
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
	//B:看程序写结果：

		int x = 2;
		int y = 3;
		switch(x){
			default:
				y++;    //4
			case 3:  
				y++;    //5
			case 4:
				y++;    //6
		}
		System.out.println("y="+y);  //顺序执行到了右大括号结束,每次y+1,最终是6
	}
}
```


### 03.23_Java语言基础(选择结构if语句和switch语句的区别)(掌握)

- A:总结switch语句和if语句的各自使用场景
- switch建议判断固定值的时候用
- if建议判断区间或范围的时候用
- B:案例演示
  - 分别用switch语句和if语句实现下列需求：
    - 键盘录入月份，输出对应的季节
switch实现:
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		/*

		* 键盘录入月份，输出对应的季节
		一年有四季
		3,4,5春季
		6,7,8夏季
		9,10,11秋季
		12,1,2冬季
		*/
		Scanner sc = new Scanner(System.in);	//创建键盘录入对象
		System.out.println("请输入月份");
		int month = sc.nextInt();				//将键盘录入的结果存储在month
		switch (month) {
		case 3:
		case 4:
		case 5:
			System.out.println(month + "月是春季");
		break;

		case 6:
		case 7:
		case 8:
			System.out.println(month + "月是夏季");     //利用的是case穿透
		break;  

		case 9:
		case 10:
		case 11:
			System.out.println(month + "月是秋季");
		break;

		case 12:
		case 1:
		case 2:
			System.out.println(month + "月是冬季");
		break;

		default:
			System.out.println("对不起没有对应的季节");
		break;
		}


	}
}
```
if实现:
```java
import java.util.Scanner;
class data 
{
	public static void main(String[] args) 
	{
		/*

		* 键盘录入月份，输出对应的季节
		一年有四季
		3,4,5春季
		6,7,8夏季
		9,10,11秋季
		12,1,2冬季
		*/
		Scanner sc = new Scanner(System.in);	//创建键盘录入对象
		System.out.println("请输入月份");
		int month = sc.nextInt();				//将键盘录入的结果存储在month

		//用if语句来完成月份对应季节   //能用switch能做的if都能做,固定值的用switch做范围用if 做
		if (month > 12 || month < 1) {
			System.out.println("对不起没有对应的季节");
		}else if (month >= 3 && month <= 5) {
			System.out.println(month + "月是春季");
		}else if (month >= 6 && month <= 8) {
			System.out.println(month + "月是夏季");
		}else if (month >= 9 && month <= 11) {
			System.out.println(month + "月是秋季");
		}else {
			System.out.println(month + "月是冬季");
		} 


	}
}
```
