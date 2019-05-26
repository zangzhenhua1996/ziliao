### 07.01_面向对象(构造方法Constructor概述和格式)(掌握)

- A:构造方法概述和作用
  - 给对象的数据(属性)进行初始化
- B:构造方法格式特点
  - a:方法名与类名相同(大小也要与类名一致)
  - b:没有返回值类型，连void都没有
  - c:没有具体的返回值return;
```java
class Demo1_Constructor {						//Constructor构造
	public static void main(String[] args) {
		Person p = new Person();				//在一创建对象的时候,系统就帮我调用了构造方法
		//p.Person();							//构造方法不能用对象调用
		p.show();   //调用p.show函数

		Person p2 = new Person();				//再次创建对象
	
		p2.show();
	}
}

/*
* A:构造方法概述和作用
	* 给对象的数据(属性)进行初始化
* B:构造方法格式特点
	* a:方法名与类名相同(大小也要与类名一致)   重点
	* b:没有返回值类型，连void都没有
	* c:没有具体的返回值return;
*/

class Person {
	private String name;
	private int age;

	//构造方法
	public Person() {   //b:没有返回值类型，连void都没有
		//System.out.println("Hello World!");
		//return;								//构造方法也是有return语句的,格式是return;
		name = "张三";
		age = 23;       //给本类的私有值赋值
	}

	public void show() {
		System.out.println(name + "..." + age);
	}
}
```
执行结果:
```java
张三...23
张三...23
请按任意键继续. . .
```
### 07.02_面向对象(构造方法的重载及注意事项)(掌握)

- A:案例演示
  - 构造方法的重载
  - 重载:方法名相同,与返回值类型无关(构造方法没有返回值),只看参数列表
```java
class Demo2_Person {
	public static void main(String[] args) {
		Person p1 = new Person();   //无参构造
		p1.show();

		System.out.println("---------------------");

		Person p2 = new Person("张三",23);
		p2.show();

		System.out.println("---------------------");

		Person p3 = new Person("李四",24);
		p3.show();
	}
}
/*
* A:案例演示
	* 构造方法的重载
	* 重载:方法名相同,与返回值类型无关(构造方法没有返回值),只看参数列表
* B:构造方法注意事项
	* a:如果我们没有给出构造方法，系统将自动提供一个无参构造方法。
	* b:如果我们给出了构造方法，系统将不再提供默认的无参构造方法。
		* 注意：这个时候，如果我们还想使用无参构造方法，就必须自己给出。建议永远自己给出无参构造方法
		
*/
class Person {
	private String name;			//姓名
	private int age;				//年龄

	public Person() {				//空参构造
		System.out.println("空参的构造");
	}

	public Person(String name,int age) {  //有参的构造,两个一块用,省的使用空参构造时出错
		this.name = name;
		this.age = age;
		System.out.println("有参的构造");
	}
	
	public void show() {
		System.out.println(name + "..." + age);
	}
}
```
执行结果:
```java
空参的构造
null...0
---------------------
有参的构造
张三...23
---------------------
有参的构造
李四...24
请按任意键继续. . .
```
- B:构造方法注意事项
  - a:如果我们没有给出构造方法，系统将自动提供一个无参构造方法。
  - b:如果我们给出了构造方法，系统将不再提供默认的无参构造方法。
    - 注意：这个时候，如果我们还想使用无参构造方法，就必须自己给出。建议永远自己给出无参构造方法

### 07.03_面向对象(给成员变量赋值的两种方式的区别)

- A:setXxx()方法
  - 修改属性值 
- B:构造方法
  - 给对象中属性进行初始化 
```java
class Demo3_Person {
	public static void main(String[] args) {
		Person p1 = new Person("张三",23);   //有参构造
		//p1 = new Person("张天一",23);	//这种方式看运行结果貌似是改名了,其实是将原对象变成垃圾,这里是创建了一个新的对象把地址付给了P1.
		System.out.println(p1.getName() + "..." + p1.getAge());

		System.out.println("--------------------");
		Person p2 = new Person();		//空参构造创建对象
		p2.setName("李四");
		p2.setAge(24);

		p2.setName("李鬼");//进行改名,不用创建新的对象
		System.out.println(p2.getName() + "..." + p2.getAge());
	}
}
/*
构造方法
	给属性进行初始化
setXxx方法
	修改属性值
	这两种方式,在开发中用setXxx更多一些,因为比较灵活
*/
class Person {
	private String name;				//姓名
	private int age;					//年龄

	public Person() {					//空参构造
	}

	public Person(String name,int age) {//有参构造
		this.name = name;
		this.age = age;
	}
	
	public void setName(String name) {	//设置姓名
		this.name = name;
	}

	public String getName() {			//获取姓名
		return name;
	}

	public void setAge(int age) {		//设置年龄
		this.age = age;
	}

	public int getAge() {				//获取年龄
		return age;
	}
}
```
执行结果:
```java
张三...23
--------------------
李鬼...24
请按任意键继续. . .
```
### 07.04_面向对象(学生类的代码及测试)(掌握)

- A:案例演示
  - 学生类：
    - 成员变量：
      - name，age
    - 构造方法：
      - 无参，带两个参
    - 成员方法：
      - getXxx()/setXxx()
      - show()：输出该类的所有成员变量值
- B:给成员变量赋值：
  - a:setXxx()方法
  - b:构造方法
- C:输出成员变量值的方式：
  - a:通过getXxx()分别获取然后拼接
  - b:通过调用show()方法搞定
```java
class Demo4_Student {
	public static void main(String[] args) {
		Student s1 = new Student();					//使用空参构造
		s1.setName("张三");							//设置姓名
		s1.setAge(23);	
		//设置年龄
		s1.show();
		System.out.println("我的姓名是:" + s1.getName() + ",我的年龄是:" + s1.getAge());
		//getXxx()获取属性值,可以打印,也可以赋值给其他的变量,做其他的操作
		Student s2 = new Student("李四",24);
		s2.show();									//只是为了显示属性值
	}
}
/*
* A:案例演示
	* 学生类：
		* 成员变量：
			* name，age
		* 构造方法：
			* 无参，带两个参
		* 成员方法：
			* getXxx()/setXxx()
			* show()：输出该类的所有成员变量值
* B:给成员变量赋值：
	* a:setXxx()方法
	* b:构造方法
	
* C:输出成员变量值的方式：
	* a:通过getXxx()分别获取然后拼接
	* b:通过调用show()方法搞定
*/

class Student {
	private String name;							//姓名
	private int age;								//年龄

	public Student() {
	}								//空参构造

	public Student(String name,int age) {			//有参构造
		this.name = name;
		this.age = age;
	}

	public void setName(String name) {				//设置姓名
		this.name = name;
	}

	public String getName() {						//获取姓名
		return name;
	}

	public void setAge(int age) {					//设置年龄
		this.age = age;
	}

	public int getAge() {							//获取年龄
		return age;
	}

	public void show() {
		System.out.println("我的姓名是:" + name +  ",我的年龄是:" +  age);
	}
}
```
执行结果:
```java
我的姓名是:张三,我的年龄是:23
我的姓名是:张三,我的年龄是:23
我的姓名是:李四,我的年龄是:24
请按任意键继续. . .
```
### 07.05_面向对象(手机类的代码及测试)(掌握)

- A:案例演示
  - 模仿学生类，完成手机类代码
```java
class Demo5_Phone {
	public static void main(String[] args) {
		Phone p1 = new Phone();
		p1.setBrand("苹果");
		p1.setPrice(1500);
		System.out.println(p1.getBrand() + "..." + p1.getPrice());

		Phone p2 = new Phone("小米",98);
		p2.show();
	}
}
/*
手机类:
	成员变量:
		品牌brand,价格price
	构造方法
		无参,有参
	成员方法
		setXxx和getXxx
		show
*/
class Phone {
	private String brand;						//品牌
	private int price;							//价格

	public Phone(){}							//空参构造

	public Phone(String brand,int price) {		//有参构造
		this.brand = brand;
		this.price = price;
	}

	public void setBrand(String brand) {		//设置品牌
		this.brand = brand;
	}

	public String getBrand() {					//获取品牌
		return brand;
	}

	public void setPrice(int price) {			//设置价格
		this.price = price;
	}

	public int getPrice() {						//获取价格
		return price;
	}

	public void show() {
		System.out.println(brand + "..." + price);
	}
}
```
执行结果:
```java
苹果...1500
小米...98
请按任意键继续. . .
```
### 07.06_面向对象(创建一个对象的步骤)(掌握)

- A:画图演示
  - 画图说明一个对象的创建过程做了哪些事情?
  - Student s = new Student();
  - 1,Student.class加载进内存
  - 2,声明一个Student类型引用s
  - 3,在堆内存创建对象,
  - 4,给对象中属性默认初始化值
  - 5,属性进行显示初始化
  - 6,构造方法进栈,对对象中的属性赋值,构造方法弹栈
  - 7,将对象的地址值赋值给s
```java
 class Demo1_Student {
	public static void main(String[] args) {
		Student s = new Student();  //创建新对象的同时就会调用构造方法
		s.show();
	}
}

class Student {
	private String name = "张三";
	private int age = 23;

	public Student() {  //空参构造
		name = "李四";
		age = 24;
	}

	public void show() {
		System.out.println(name + "..." + age);
	}
}
```
![创建对象的步骤.png](https://upload-images.jianshu.io/upload_images/14555448-703bc16c8931e104.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 07.07_面向对象(长方形案例练习)(掌握)

- A:案例演示
  - 需求：
    - 定义一个长方形类,定义 求周长和面积的方法，
    - 然后定义一个测试类进行测试。
```java
class chang {
	public static void main(String[] args)  {
		Rectangle r =new Rectangle(10,20);
		System.out.println(r.getLength());
		System.out.println(r.getArea());

	}
}

class Rectangle {
	private int width;				//宽
	private int high;				//高

	public Rectangle(){}			//空参构造

	public Rectangle(int width,int high) {
		this.width = width;			//有参构造
		this.high = high;
	}

	public void setWidth(int width) {//设置宽
		this.width = width;
	}


	public int getWidth() {
		return width;
	}
	public void setHigh(int high) {
		this.high = high;
	}
	public int getHigh() {
		return high;
	}

	public int getLength() {
		return 2*(width+high);
		}

	public int getArea() {
		return width*high;
		}
}

```
执行结果:
```java
60
200
请按任意键继续. . .
```
### 07.08_面向对象(员工类案例练习)(掌握)

- A:案例演示
  - 需求：定义一个员工类Employee
  - 自己分析出几个成员，然后给出成员变量
    - 姓名name,工号id,工资salary 
  - 构造方法，
    - 空参和有参的
  - getXxx()setXxx()方法，
  - 以及一个显示所有成员信息的方法。并测试。
    - work 
```java
class Test2_Employee {						//employee员工
	public static void main(String[] args) {
		Employee e = new Employee("令狐冲","9527",20000);
		e.work();
	}
}

//在语法上一定要注意括号和大括号的区分特别的容易出错
/*
* A:案例演示
	* 需求：定义一个员工类Employee
	* 自己分析出几个成员，然后给出成员变量
		* 姓名name,工号id,工资salary 
	* 构造方法，
		* 空参和有参的
	* getXxx()setXxx()方法，
	* 以及一个显示所有成员信息的方法。并测试。
		* work 
*/
class Employee {
	private String name;					//姓名
	private String id;						//工号
	private double salary;					//工资

	public Employee() {}					//空参构造

	public Employee(String name, String id, double salary) {//有参构造
		this.name = name;
		this.id = id;
		this.salary = salary;
	}

	public void setName(String name) {		//设置姓名
		this.name = name;
	}

	public String getName() {				//获取姓名
		return name;
	}

	public void setId(String id) {			//设置id
		this.id = id;
	}

	public String getId() {					//获取id
		return id;
	}

	public void setSalary(double salary) {	//设置工资
		this.salary = salary;
	}
	
	public double getSalary() {				//获取工资
		return salary;
	}

	public void work() {
		System.out.println("我的姓名是:" + name + ",我的工号是:" + id + ",我的工资是:" + salary 
			+ ",我的工作内容是敲代码");
	}
}
	
```
执行结果:
```java
我的姓名是:令狐冲,我的工号是:9527,我的工资是:20000.0,我的工作内容是敲代码
请按任意键继续. . .
```
### 07.09_面向对象(static关键字及内存图)(了解)

- A:案例演示
  - 通过一个案例引入static关键字。
  - 人类：Person。每个人都有国籍，中国。
```java
class Demo1_Static {
	public static void main(String[] args) {
		Person p1 = new Person();	//创建对象
		p1.name = "苍老师";			//调用姓名属性并赋值
		p1.country = "日本";		//调用国籍属性并赋值
		

		Person p2 = new Person();
		p2.name = "小泽老师";		//调用姓名属性并赋值
		//p2.country = "日本";		//调用国籍属性并赋值

		p1.speak();
		p2.speak();

		//Person.country = "日本";	//静态多了一种调用方式,可以通过类名.,也就是说不用创建对象直接将静态变量进行赋值.用的是类名进行调用赋值
		//System.out.println(Person.country);
	}
}

class Person {
	String name;					//姓名(没有使用私有)
	static String country;					//国籍,加了静态以后只要有一个对象将其赋值,以后创建的对象这个值都是默认的第一个对象的赋值
 
	public void speak() {			//说话的方法
		System.out.println(name + "..." + country);
	}
}
```
执行结果:
```java
苍老师...日本
小泽老师...日本
请按任意键继续. . .
```
- B:画图演示
  - 带有static的内存图
![image.png](https://upload-images.jianshu.io/upload_images/14555448-be2c7abb9de137be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![创建对象内存图.png](https://upload-images.jianshu.io/upload_images/14555448-79f6e1149d4f2a9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 07.10_面向对象(static关键字的特点)(掌握)

- A:static关键字的特点
  - a:随着类的加载而加载
  - b:优先于对象存在
  - c:被类的所有对象共享
    - 举例：咱们班级的学生应该共用同一个班级编号。
    - 其实这个特点也是在告诉我们什么时候使用静态?
      - 如果某个成员变量是被所有对象共享的，那么它就应该定义为静态的。
    - 举例：
      - 饮水机(用静态修饰)
      - 水杯(不能用静态修饰)
      - 共性用静态,特性用非静态
  - d:可以通过类名调用
    - 其实它本身也可以通过对象名调用。
    - 推荐使用类名调用。
    - 静态修饰的内容一般我们称其为：与类相关的，类成员
- B:案例演示
  - static关键字的特点

### 07.11_面向对象(static的注意事项)(掌握)

- A:static的注意事项
  - a:在静态方法中是没有this关键字的
    - 如何理解呢?
      - 静态是随着类的加载而加载，this是随着对象的创建而存在。
      - 静态比对象先存在。
  - b:静态方法只能访问静态的成员变量和静态的成员方法
    - 静态方法：
      - 成员变量：只能访问静态变量
      - 成员方法：只能访问静态成员方法
    - 非静态方法：
      - 成员变量：可以是静态的，也可以是非静态的
      - 成员方法：可是是静态的成员方法，也可以是非静态的成员方法。
    - 简单记：
      - 静态只能访问静态。
- B:案例演示
  - static的注意事项
```java
class Demo2_Static {
	public static void main(String[] args) {
		Demo d = new Demo();
		d.print1();

		//Demo.print2();
	}
}

/*
* A:static的注意事项
	* a:在静态方法中是没有this关键字的
		* 如何理解呢?
			* 静态是随着类的加载而加载，this是随着对象的创建而存在。
			* 静态比对象先存在。
	* b:静态方法只能访问静态的成员变量和静态的成员方法
		* 静态方法：
			* 成员变量：只能访问静态变量
			* 成员方法：只能访问静态成员方法
		* 非静态方法：
			* 成员变量：可以是静态的，也可以是非静态的
			* 成员方法：可是是静态的成员方法，也可以是非静态的成员方法。
		* 简单记：
			* 静态只能访问静态。
*/

class Demo {
	int num1 = 10;						//非静态的成员变量
	static int num2 = 20;				//静态的成员变量

	public void print1() {				//非静态的成员方法,既可以访问静态的成员也可以访问非静态的
		System.out.println(num1);
		System.out.println(num2);
	}

	public static void print2() {		//静态的成员方法
		//System.out.println(this.num1);//静态的成员方法不能访问非静态的,错误: 无法从静态上下文中引用非静态 变量 num1
		System.out.println(num2);
	}
}
```
执行结果:
```java
10
20
请按任意键继续. . .

```
```java
class Demo3_Static {
	public static void main(String[] args) {
		//method();								//错误: 无法从静态上下文中引用非静态 方法 method()
		Demo3_Static.print();					//在主方法中调用本类的静态方法,可以省略类名.,系统会默认加上
		Demo3_Static d = new Demo3_Static();	//非静态方法在调用的时候必须创建对象调用
		d.method();
	}

	public void method() {					
		System.out.println("Hello World!");		
	}

	public static void print() {
		System.out.println("Hello World!");
	}
}
```
### 07.12_面向对象(静态变量和成员变量的区别)(掌握)

- 静态变量也叫类变量  成员变量也叫对象变量
- A:所属不同
  - 静态变量属于类，所以也称为为类变量
  - 成员变量属于对象，所以也称为实例变量(对象变量)
- B:内存中位置不同
  - 静态变量存储于方法区的静态区
  - 成员变量存储于堆内存
- C:内存出现时间不同
  - 静态变量随着类的加载而加载，随着类的消失而消失
  - 成员变量随着对象的创建而存在，随着对象的消失而消失
- D:调用不同
  - 静态变量可以通过类名调用，也可以通过对象调用
  - 成员变量只能通过对 象名调用

### 07.13_面向对象(main方法的格式详细解释)(了解)

- A:格式
  - public static void main(String[] args) {}
- B:针对格式的解释
  - public 被jvm调用，访问权限足够大。
  - static 被jvm调用，不用创建对象，直接类名访问
  - void被jvm调用，不需要给jvm返回值
  - main 一个通用的名称，虽然不是关键字，但是被jvm识别
  - String[] args 以前用于接收键盘录入的
- C:演示案例
  - 通过args接收键盘例如数据
```java
class Demo3_Main {
	public static void main(String[] args) {			
		/*
		public : 被jvm调用,所以权限要足够大
		static : 被jvm调用,不需要创建对象,直接类名.调用即可
		void   : 被jvm调用,不需要有任何的返回值
		main   : 只有这样写才能被jvm识别,main不是关键字
		String[] args : 以前是用来接收键盘录入的
		*/

		System.out.println(args.length);
		for (int i = 0;i < args.length ;i++ ) {
			System.out.println(args[i]);
		}
	}
}

```
### 07.14_面向对象(工具类中使用静态)(了解)

- A:制作一个工具类
  - ArrayTool
  - 1,获取最大值
  - 2,数组的遍历
  - 3,数组的反转

### 07.15_面向对象(说明书的制作过程)(了解)

- A:对工具类加入文档注释
- B:通过javadoc命令生成说明书
  - @author(提取作者内容)
  - @version(提取版本内容)
  - javadoc -d 指定的文件目录(存储的目录) -author -version ArrayTool.java
  - @param 参数名称//形式参数的变量名称@return 函数运行完返回的数据
```java
/**
这是一个数组工具类,里面封装了查找数组最大值,打印数组,数组反转的方法
@author fengjia
@version v1.0
*/
public class ArrayTool {
	//如果一个类中所有的方法都是静态的,需要再多做一步,私有构造方法,目的是不让其他类创建本类对象
	//直接用类名.调用即可
	/**
	私有构造方法
	*/
	private ArrayTool(){}

	//1,获取最大值

	/**
	这是获取数组中最大值的方法
	@param arr 接收一个int类型数组
	@return 返回数组中最大值
	*/
	public static int getMax(int[] arr) {
		int max = arr[0];						//记录第一个元素
		for (int i = 1;i < arr.length ;i++ ) {	//从第二个元素开始遍历
			if (max < arr[i]) {					//max与数组中其他的元素比较
				max = arr[i];					//记录住较大的
			}
		}

		return max;								//将最大值返回
	}
	//2,数组的遍历
	/**
	这是遍历数组的方法
	@param arr 接收一个int类型数组
	*/
	public static void print(int[] arr) {
		for (int i = 0;i < arr.length ;i++ ) {	//遍历数组
			System.out.print(arr[i] + " ");
		}
	}
	//3,数组的反转
	/**
	这是数组反转的方法
	@param arr 接收一个int类型数组
	*/
	public static void revArray(int[] arr) {
		for (int i = 0;i < arr.length / 2 ;i++ ) {	//循环次数是元素个数的一半
			/*
			arr[0]与arr[arr.length-1-0]	交换
			arr[1]与arr[arr.length-1-1]	交换
			arr[2]与arr[arr.length-1-2] 交换
			*/
			int temp = arr[i];
			arr[i] = arr[arr.length-1-i];
			arr[arr.length-1-i] = temp;
		}
	}
}
```
### 07.16_面向对象(如何使用JDK提供的帮助文档)(了解)

- A:找到文档，打开文档
- B:点击显示，找到索引，出现输入框
- C:你应该知道你找谁?举例：Scanner
- D:看这个类的结构(需不需要导包)
  - 成员变量	字段
  - 构造方法	构造方法
  - 成员方法	方法

### 07.17_面向对象(学习Math类的随机数功能)(了解)

- 打开JDK提供的帮助文档学习
- A:Math类概述
  - 类包含用于执行基本数学运算的方法
- B:Math类特点
  - 由于Math类在java.lang包下，所以不需要导包。
  - 因为它的成员全部是静态的,所以私有了构造方法
- C:获取随机数的方法
  - public static double random():返回带正号的 double 值，该值大于等于 0.0 且小于 1.0。
- D:我要获取一个1-100之间的随机数，肿么办?
  - int number = (int)(Math.random()*100)+1;

```java
class Demo2_Math {
	public static void main(String[] args) {
		//double d = Math.random();
		//System.out.println(d);
		
		//Math.random()会生成大于等于0.0并且小于1.0的伪随机数
		for (int i = 0;i < 10 ;i++ ) {
			System.out.println(Math.random());
		}

		//生成1-100的随机数
		//Math.random()0.0000000 - 0.999999999
		//Math.random() * 100 ====> 0.00000 - 99.999999999
		//(int)(Math.random() * 100) ====> 0 - 99
		//(int)(Math.random() * 100) + 1

		for (int i = 0;i < 10 ;i++ ) {
			System.out.println((int)(Math.random() * 100) + 1);
		}
	}
}

```
执行结果:
```
0.4302003345397628
0.7676603432494656
0.48280324460896684
0.41828455188990443
0.14225711747026704
0.7997061450236818
0.8836752345661977
0.7949006753873378
0.5338073915536524
0.5020184172554488
21
85
10
62
12
65
79
1
86
26
请按任意键继续. . .
```

### 07.18_面向对象(猜数字小游戏案例)(了解)

- A:案例演示
  - 需求：猜数字小游戏(数据在1-100之间)

```java
/*
* A:案例演示
	* 需求：猜数字小游戏(数据在1-100之间)
*/
import java.util.Scanner;
class Test1_GuessNum {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);				//创建键盘录入对象
		System.out.println("请输入一个整数,范围在1-100之间");
		int guessNum = (int)(Math.random() * 100) + 1;		//心里想的随机数
		while (true) {										//因为需要猜很多次,所以用无限循环
			int result = sc.nextInt();						//大家猜的数
			if (result > guessNum) {						//如果你们猜的数大于了我心里想的数
				System.out.println("大了");					//提示大了
			} else if (result < guessNum) {					//如果你们猜的数小于了我心里想的数
				System.out.println("小了");					//提示小了
			} else {										//如果既不大也不小
				System.out.println("中了");					//中了
				break;
			}
		}
	}
}
```
