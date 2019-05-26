### 06.01_面向对象(面向对象思想概述)(了解)

* A:面向过程思想概述
	* 第一步
	* 第二步 
* B:面向对象思想概述
	* 找对象(第一步,第二步) 
* C:举例
	* 买煎饼果子
	* 洗衣服 
* D:面向对象思想特点
	* a:是一种更符合我们思想习惯的思想
	* b:可以将复杂的事情简单化
	* c:将我们从执行者变成了指挥者
		* 角色发生了转换
* E:面向对象开发
	* 就是不断的创建对象，使用对象，指挥对象做事情。
* F:面向对象设计
	* 其实就是在管理和维护对象之间的关系。
* G:面向对象特征
	* 封装(encapsulation)
	* 继承(inheritance)
	* 多态(polymorphism)

### 06.02_面向对象(类与对象概述)(掌握)

* A:我们学习编程是为了什么
	* 为了把我们日常生活中实物用学习语言描述出来
* B:我们如何描述现实世界事物
	* 属性	就是该事物的描述信息(事物身上的名词)
	* 行为	就是该事物能够做什么(事物身上的动词)
* C:Java中最基本的单位是类,Java中用class描述事物也是如此
	* 成员变量	就是事物的属性
	* 成员方法	就是事物的行为
* D:定义类其实就是定义类的成员(成员变量和成员方法)
	* a:成员变量	和以前定义变量是一样的，只不过位置发生了改变。在类中，方法外。
	* b:成员方法	和以前定义方法是一样的，只不过把static去掉，后面在详细讲解static的作用。
* E:类和对象的概念
	* a:类：是一组相关的属性和行为的集合
	* b:对象：是该类事物的具体体现
	* c:举例：
		* 类	 学生
		* 对象	具体的某个学生就是一个对象

### 06.03_面向对象(学生类的定义)(掌握)

* A:学生事物
* B:学生类
* C:案例演示
	* 属性:姓名,年龄,性别
	* 行为:学习,睡觉
```java
class Demo1_Student {   //测试类中有主方法,
	public static void main(String[] args) {
		//创建对象的格式:类名 对象名 = new 类名();
		//对象名:其实就是合法的标识符,如果是一个单词所有字母小写,如果是多个单词,从第二个单词开始首字母大写
		Student s = new Student();  //应该就是实例化对象
		//* D:如何使用成员变量呢?
		//* 对象名.变量名
		s.name = "张三";  //使用的是属性
		s.age = 23;

		System.out.println(s.name + "..." + s.age);
		//* E:如何使用成员方法呢?
		//* 对象名.方法名(...)
		s.study();
		s.sleep();
	}
}


/*
* A:案例演示
	* 属性:姓名,年龄,性别
	* 行为:学习,睡觉

* B:我们如何描述现实世界事物
	* 属性	就是该事物的描述信息(事物身上的名词)
	* 行为	就是该事物能够做什么(事物身上的动词)
* C:Java中最基本的单位是类,Java中用class描述事物也是如此
	* 成员变量	就是事物的属性
	* 成员方法	就是事物的行为
* D:定义类其实就是定义类的成员(成员变量和成员方法)
	* a:成员变量	和以前定义变量是一样的，只不过位置发生了改变。在类中，方法外。
	* b:成员方法	和以前定义方法是一样的，只不过把static去掉，后面在详细讲解static的作用。
*/

class Student {    //基本类
	String name;						//姓名
	int age;							//年龄
	String gender;						//性别

	public void study() {				//定义学习的方法
		System.out.println("学生学习");
	}

	public void sleep() {				//定义睡觉的方法
		System.out.println("学生睡觉");
	}
}
```

### 06.04_面向对象(手机类的定义)(掌握)

* 模仿学生类，让学生自己完成
	* 属性:品牌(brand)价格(price)
	* 行为:打电话(call),发信息(sendMessage)玩游戏(playGame)
```java
class Demo2_Phone {
	public static void main(String[] args) {
		//创建对象
		Phone p = new Phone();
		//调用对象中的属性并赋值   ,不赋值的就是默认值
		//p.brand = "锤子";
		p.price = 998;

		System.out.println(p.brand + "..."  + p.price);

		//调用成员方法
		p.call();
		p.sendMessage();
		p.playGame();
	}
}

/*
* 模仿学生类，让学生自己完成
	* 属性:品牌(brand)价格(price)
	* 行为:打电话(call),发信息(sendMessage)玩游戏(playGame)

*/
class Phone {
	String brand="锤子";					//品牌  这里赋值在实例化对象后就是默认的属性值
	int price;						//价格

	public void call() {			//打电话
		System.out.println("打电话");
	}

	public void sendMessage() {		//发信息
		System.out.println("发信息");
	}

	public void playGame() {		//玩游戏
		System.out.println("玩游戏");
	}
}
```
### 06.05_面向对象(学生类的使用)(掌握)

* A:文件名问题
	* 在一个java文件中写两个类：一个基本的类，一个测试类。
	* 建议：文件名称和测试类名称一致。
* B:如何使用对象?
	* 创建对象并使用
	* 格式：类名 对象名 = new 类名();
* D:如何使用成员变量呢?
	* 对象名.变量名
* E:如何使用成员方法呢?
	* 对象名.方法名(...)

### 06.06_面向对象(手机类的使用)(掌握)

* A:学生自己完成
	* 模仿学生类，让学生自己完成
	
### 06.07_面向对象(一个对象的内存图)(掌握)
```java
class Demo1_Car {
	public static void main(String[] args) {
		Car c1 = new Car();				//创建对象

		//调用属性并赋值
		c1.color = "red";				//为车的颜色赋值
		c1.num = 8;						//为车的轮胎数赋值

		//调用行为
		c1.run();

		Car c2 = new Car();				//创建对象
		c2.color = "black";				//为车的颜色赋值
		c2.num = 4;						//为车的轮胎数赋值
		c2.run();

		//c2 = null;						//用null把原来的地址值覆盖掉了

		//c2.run();						//c2里面记录的是null,所以报出空指针异常

		Car c3 = c2;
		c3.run();
		
	}
}
/*
车的属性
	车的颜色
	车的轮胎数
车的行为
	车运行
*/

class Car {
	//成员变量
	String color;						//车的颜色
	int num;							//车的轮胎数

	public void run() {					//车运行
		System.out.println(color + "..." + num);
	}
}
```
* A:画图演示
	* 一个对象
![image.png](https://upload-images.jianshu.io/upload_images/14555448-9e0a0eef96325fda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 06.08_面向对象(二个对象的内存图)(了解)

* A:画图演示
	* 二个不同的对象
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4ab35fe0b10d87db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 06.09_面向对象(三个引用两个对象的内存图)(了解)

* A:画图演示
	* 三个引用，有两个对象的引用指向同一个地址
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ddf2382a13da4c7c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 06.10_面向对象(成员变量和局部变量的区别)(掌握)

* A:在类中的位置不同
	* 成员变量：在类中方法外
	* 局部变量：在方法定义中或者方法声明上
* B:在内存中的位置不同
	* 成员变量：在堆内存(成员变量属于对象,对象进堆内存)
	* 局部变量：在栈内存(局部变量属于方法,方法进栈内存)
* C:生命周期不同
	* 成员变量：随着对象的创建而存在，随着对象的消失而消失
	* 局部变量：随着方法的调用而存在，随着方法的调用完毕而消失
* D:初始化值不同
	* 成员变量：有默认初始化值
	* 局部变量：没有默认初始化值，必须定义，赋值，然后才能使用。
	
* 注意事项：
	* 局部变量名称可以和成员变量名称一样，在方法中使用的时候，采用的是就近原则。
	* 基本数据类型变量包括哪些:byte,short,int,long,float,double,boolean,char
	* 引用数据类型变量包括哪些:数组,类,接口,枚举
```java
class Demo2_Person {
	public static void main(String[] args) {
		Person p = new Person();
		p.speak();
	}
}
/*
* A:在类中的位置不同
	* 成员变量：在类中方法外
	* 局部变量：在方法定义中或者方法声明上
* B:在内存中的位置不同
	* 成员变量：在堆内存(成员变量属于对象,对象进堆内存)
	* 局部变量：在栈内存(局部变量属于方法,方法进栈内存)
* C:生命周期不同
	* 成员变量：随着对象的创建而存在，随着对象的消失而消失
	* 局部变量：随着方法的调用而存在，随着方法的调用完毕而消失
* D:初始化值不同
	* 成员变量：有默认初始化值
	* 局部变量：没有默认初始化值，必须定义，赋值，然后才能使用。
	
* 注意事项：
	* 局部变量名称可以和成员变量名称一样，在方法中使用的时候，采用的是就近原则。
	* 基本数据类型变量包括哪些:byte,short,int,long,float,double,boolean,char
	* 引用数据类型变量包括哪些:数组,类,接口,枚举
*/
class Person {
	String name;						//成员变量
	int num;

	public void speak() {
		int num = 10;						//x和num都是局部变量
		System.out.println(name);
	
		System.out.println(num);
	}
}

```
	
### 06.11_面向对象(方法的形式参数是类名的时候如何调用)(掌握)

* A:方法的参数是类名public void print(Student s){}//print(new Student());
	* 如果你看到了一个方法的形式参数是一个类类型(引用类型)，这里其实需要的是该类的对象。
```java
class Demo1_Student {
	public static void main(String[] args) {
		print(10);

		Student s = new Student();					//创建对象,并将对象的地址值赋值给s
		print(s);
	}

	public static void print(int x) {				//基本数据类型当作形式参数(值),基本数据类型直接给形参一个值就可以
		System.out.println(x);
	}

	public static void print(Student stu) {			//引用数据类型当作形式参数(地址值)
		stu.name = "张三";
		stu.age = 23;
		stu.speak();
	}
}

/*
* A:方法的参数是类名public void print(Student s){}//print(new Student());
	* 如果你看到了一个方法的形式参数是一个类类型(引用类型)，这里其实需要的是该类的对象。
*/
class Student {
	String name;					//姓名
	int age;						//年龄

	public void speak() {
		System.out.println(name + "..." + age);
	}
}
```

### 06.12_面向对象(匿名对象的概述和应用)(掌握)

* A:什么是匿名对象
	* 没有名字的对象 
* B:匿名对象应用场景
	* a:调用方法，仅仅只调用一次的时候。
		* 那么，这种匿名调用有什么好处吗?
			* 节省代码 
		* 注意：调用多次的时候，不适合。匿名对象调用完毕就是垃圾。可以被垃圾回收器回收。
	* b:匿名对象可以作为实际参数传递
* C:案例演示
	* 匿名对象应用场景
```java
/*
* A:什么是匿名对象
	* 没有名字的对象 
* B:匿名对象应用场景
	* a:调用方法，仅仅只调用一次的时候。
		* 那么，这种匿名调用有什么好处吗?!
			* 节省代码 
		* 注意：调用多次的时候，不适合。匿名对象调用完毕就是垃圾。可以被垃圾回收器回收。
	* b:匿名对象可以作为实际参数传递
* C:案例演示
	* 匿名对象应用场景
*/
class Demo2_Car {
	public static void main(String[] args) {
		/*Car c1 = new Car();			//创建有名字的对象
		c1.run();
		c1.run();

		new Car().run();			//匿名对象调用方法
		new Car().run();	*/	//匿名对象只适合对方法的一次调用,因为调用多次就会产生多个对象,不如用有名字的对象	
	
		//匿名对象是否可以调用属性并赋值?有什么意义?
		/*
		匿名对象可以调用属性,但是没有意义,因为调用后就变成垃圾
		如果需要赋值还是用有名字对象
		*/
		new Car().color = "red";
		new Car().num = 8;
		new Car().run();  //由于每次都是创建一个新的对象,因此给属性赋值没有丝毫的用处
	}
}

class Car {
	String color;			//颜色
	int num;				//轮胎数

	public void run() {
		System.out.println(color + "..." + num);
	}
}
```
```java
class Demo3_Car {
	public static void main(String[] args) {
		//Car c1 = new Car();
		/*c1.color = "red";
		c1.num = 8;
		c1.run();*/
		//method(c1);

		method(new Car());

		//Car c2 = new Car();
		//method(c2);
		method(new Car());				//匿名对象可以当作参数传递
	}

	//抽取方法提高代码的复用性
	public static void method(Car cc) {	//Car cc = new Car();
		cc.color = "red";
		cc.num = 8;
		cc.run();
	}
}

class Car {
	String color;			//颜色
	int num;				//轮胎数

	public void run() {
		System.out.println(color + "..." + num);
	}
}
```

### 06.13_面向对象(封装的概述)(掌握)

* A:封装概述
	* 是指隐藏对象的属性和实现细节，仅对外提供公共访问方式。

* B:封装好处
	* 隐藏实现细节，提供公共的访问方式
	* 提高了代码的复用性
	* 提高安全性。
* C:封装原则
	* 将不需要对外提供的内容都隐藏起来。
	* 把属性隐藏，提供公共方法对其访问。

### 06.14_面向对象(private关键字的概述和特点)(掌握)

* A:人类赋值年龄的问题
* B:private关键字特点
	* a:是一个权限修饰符
	* b:可以修饰成员变量和成员方法
	* c:被其修饰的成员只能在本类中被访问
* C:案例演示
	* 封装和private的应用：
	* A:把成员变量用private修饰
	* B:提供对应的getXxx()和setXxx()方法
	* private仅仅是封装的一种体现形式,不能说封装就是私有
```java
/*
* A:人类赋值年龄的问题
* B:private关键字特点
	* a:是一个权限修饰符
	* b:可以修饰成员变量和成员方法
	* c:被其修饰的成员只能在本类中被访问
* C:案例演示
	* 封装和private的应用：
	* A:把成员变量用private修饰
	* B:提供对应的getXxx()和setXxx()方法
	* private仅仅是封装的一种体现形式,不能说封装就是私有
*/
class Demo1_Person {
	public static void main(String[] args) {
		Person p1 = new Person();
		p1.name = "张三";			//调用姓名属性并赋值
		//p1.age = -17;				//调用年龄属性并赋值
		//p1.speak();					//调用行为

		p1.setAge(-17);

		System.out.println(p1.getAge());
	}
}

class Person {
	String name;					//姓名
	private int age;				//年龄(使用了private权限,只能再本类中进行调用)
	
	public void setAge(int a) {		//设置年龄
		if (a > 0 && a < 200) {
			
			age = a;                        //使用了封装,进行判断保证了安全
		}
		else {
			System.out.println("请回火星吧,地球不适合你");
		}
		
	}

	public int getAge() {			//获取年龄
		return age;
	}

	public void speak() {
		System.out.println(name + "..." + age);
	}
}
```
### 06.15_面向对象(this关键字的概述和应用)(掌握)

* A:this关键字特点
	* 代表当前对象的引用 
* B:案例演示
	* this的应用场景
	* 用来区分成员变量和局部变量重名
```java
/*
* A:this关键字特点
	* 代表当前对象的引用 
* B:案例演示
	* this的应用场景
	* 用来区分成员变量和局部变量  重名
*/
class Demo1_This {
	public static void main(String[] args) {
		Person p1 = new Person();
		p1.setName("张三");
		p1.setAge(23);
		System.out.println(p1.getName() + "..." + p1.getAge());

		Person p2 = new Person();
		p2.setName("李四");
		p2.setAge(24);
		System.out.println(p2.getName() + "..." + p2.getAge());
	}
}

class Person {
	private String name;			//姓名
	private int age;				//年龄
	
	public void setAge(int age) {		//设置年龄
		if (age > 0 && age < 200) {
			this.age = age;
			//System.out.println(age);
		}else {
			System.out.println("请回火星吧,地球不适合你");
		}
		
	}

	public int getAge() {			//获取年龄
		return age;
	}

	public void setName(String name) {	//设置姓名
		this.name = name;
		//System.out.println(name);
	}

	public String getName() {
		return name;
	}
}
```
### 06.16_面向对象(手机类代码及其测试)(掌握)

* A:学生练习
	* 请把手机类写成一个标准类，然后创建对象测试功能。
	
```java
class Demo2_Phone {
	public static void main(String[] args) {
		Phone p1 = new Phone();
		p1.setBrand("三星");
		p1.setPrice(5288);

		System.out.println(p1.getBrand() + "..." + p1.getPrice());
		p1.call();
		p1.sendMessage();
		p1.playGame();
	}
}
/*
手机类
	属性:品牌brand,价格price
	行为:打电话call,发短信sendMessage,玩游戏,playGame
*/
class Phone {								//java bean
	private String brand;					//品牌
	private int price;						//价格

	public void setBrand(String brand) {	//设置品牌
		this.brand = brand;
	}

	public String getBrand() {				//获取品牌
		return this.brand;					//this.可以省略,你不加系统会默认给你加
	}

	public void setPrice(int price) {		//设置价格
		this.price = price;
	}

	public int getPrice() {					//获取价格
		return price;
	}

	public void call() {					//打电话
		System.out.println("打电话");
	}

	public void sendMessage() {				//发短信
		System.out.println("发短信");
	}

	public void playGame() {				//玩游戏
		System.out.println("玩游戏");
	}
}
```
