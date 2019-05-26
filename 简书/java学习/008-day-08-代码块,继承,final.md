### 08.01_面向对象(代码块的概述和分类)(了解)(面试的时候会问,开发不用或者很少用)

* A:代码块概述
	
	* 在Java中，使用{}括起来的代码被称为代码块。
* B:代码块分类
	
	* 根据其位置和声明的不同，可以分为局部代码块，构造代码块，静态代码块，同步代码块(多线程讲解)。
* C:常见代码块的应用
	* a:局部代码块 
		
		* 在方法中出现；限定变量生命周期，及早释放，提高内存利用率
	* b:构造代码块 (初始化块)
		
		* 在类中方法外出现；多个构造方法方法中相同的代码存放到一起，每次调用构造都执行，并且在构造方法前执行
	* c:静态代码块 
		* 在类中方法外出现，并加上static修饰；用于给类进行初始化，在加载的时候就执行，并且只执行一次。
		
		* 一般用于加载驱动
		
		  ```java
		  class Demo1_Code {
		  	public static void main(String[] args) {
		  		{
		  			int x = 10;						//限定变量的声明周期
		  			System.out.println(x);
		  		}
		  		
		  		Student s1 = new Student();
		  		System.out.println("---------------");
		  		Student s2 = new Student("张三",23);
		  	
		  	}
		  
		  	static {
		  		System.out.println("我是在主方法类中的静态代码块");
		  	}
		  }
		  
		  class Student {
		  	private String name;
		  	private int age;
		  
		  	public Student(){
		  		//study();
		  		System.out.println("空参构造");
		  	}					//空参构造
		  
		  	public Student(String name,int age) {//有参构造
		  		//study();
		  		this.name = name;
		  		this.age = age;
		  		System.out.println("有参构造");
		  	}
		  
		  	public void setName(String name) {
		  		this.name = name;
		  	}
		  
		  	public String getName() {
		  		return name;
		  	}
		  
		  	public void setAge(int age) {
		  		this.age = age;
		  	}
		  
		  	public int getAge() {
		  		return age;
		  	}
		  
		  	{											//构造代码块:每创建一次对象就会执行一次,优先于构造函数执行
		  		//System.out.println("构造代码块");
		  		study();
		  	}
		  
		  	public void study() {
		  		System.out.println("学生学习");
		  	}
		  
		  	static {									//随着类加载而加载,且只执行一次
		  		System.out.println("我是静态代码块");	//作用:用来给类进行初始化,一般用来加载驱动
		  	}											//静态代码块是优先于主方法执行
		  }
		  ```
		
		  执行结果:
		
		  ```java
		  我是在主方法类中的静态代码块   //首先执行的是主类的静态代码块
		  10                        //顺序执行代码块 
		  我是静态代码块              //第一次创建对象时执行静态代码块(加载类),只执行一次
		  学生学习                   //构造代码块,先于构造方法执行
		  空参构造                   //执行构造方法
		  ---------------
		  学生学习
		  有参构造
		  请按任意键继续. . .
		  ```
		
		  

### 08.02_面向对象(代码块的面试题)(掌握)
* A:看程序写结果
   		

   ```java
   class Student {
   	static {
   		System.out.println("Student 静态代码块");
   	}
   	
   	{
   		System.out.println("Student 构造代码块");
   	}
   	
   	public Student() {
   		System.out.println("Student 构造方法");
   	}
   }
   
   class Demo2_Student {
   	static {
   		System.out.println("Demo2_Student静态代码块");  //静态代码块都是最先执行的
   	}
   	
   	public static void main(String[] args) {
   		System.out.println("我是main方法");
   		
   		Student s1 = new Student();
   		Student s2 = new Student();
   	}
   }
   ```

   执行结果:只要明白每个代码块的执行顺序就可以了

   ```java
   Demo2_Student静态代码块
   我是main方法
   Student 静态代码块
   Student 构造代码块
   Student 构造方法
   Student 构造代码块
   Student 构造方法
   请按任意键继续. . .
   ```

   

### 08.03_面向对象(继承案例演示)(掌握)

* A:继承(extends)

  * 让类与类之间产生关系,子父类关系 
* B:继承案例演示：
  * 动物类,猫类,狗类
  * 定义两个属性(颜色,腿的个数)两个功能(吃饭，睡觉)
* C:案例演示

  * 使用继承前
  
    ```java
    class Demo1_Extends {
    	public static void main(String[] args) {
    		Cat c = new Cat();
    		c.color = "花";
    		c.leg = 4;
    		c.eat();
    		c.sleep();
    
    		System.out.println(c.leg  + "..." + c.color);
    	}
    }
    /*
    * A:继承(extends)
    	* 让类与类之间产生关系,子父类关系 
    * B:继承案例演示：
    	* 动物类,猫类,狗类
    	* 定义两个属性(颜色,腿的个数)两个功能(吃饭，睡觉)
    * C:案例演示
    	* 使用继承前
    * D:案例演示
    	* 使用继承后
    */
    class Animal {
    	String color;					//动物的颜色
    	int leg;						//动物腿的个数
    
    	public void eat() {				//吃饭的功能
    		System.out.println("吃饭");
    	}
    
    	public void sleep() {			//睡觉的功能
    		System.out.println("睡觉");
    	}
    }
    
    class Cat  {
    	String color;					//动物的颜色
    	int leg;						//动物腿的个数
    
    	public void eat() {				//吃饭的功能
    		System.out.println("吃饭");
    	}
    
    	public void sleep() {			//睡觉的功能
    		System.out.println("睡觉");
    	}
    	
    }
    
    class Dog  {
    		String color;					//动物的颜色
    	int leg;						//动物腿的个数
    
    	public void eat() {				//吃饭的功能
    		System.out.println("吃饭");
    	}
    
    	public void sleep() {			//睡觉的功能
    		System.out.println("睡觉");
    	}
    	
    }
    
    /*
    extends是继承的意思
    Animal是父类
    Cat和Dog都是子类
    */
    ```
  
    执行结果:  定义了三个功能重复的类,麻烦
  
    ```java
    吃饭
    睡觉
    4...花
    请按任意键继续. . .
    ```
  
    
* D:案例演示

  * 使用继承后

    ```java
    class Demo1_Extends {
    	public static void main(String[] args) {
    		Cat c = new Cat();
    		c.color = "花";
    		c.leg = 4;
    		c.eat();
    		c.sleep();
    
    		System.out.println(c.leg  + "..." + c.color);
    	}
    }
    /*
    * A:继承(extends)
    	* 让类与类之间产生关系,子父类关系 
    * B:继承案例演示：
    	* 动物类,猫类,狗类
    	* 定义两个属性(颜色,腿的个数)两个功能(吃饭，睡觉)
    * C:案例演示
    	* 使用继承前
    * D:案例演示
    	* 使用继承后
    */
    class Animal {
    	String color;					//动物的颜色
    	int leg;						//动物腿的个数
    
    	public void eat() {				//吃饭的功能
    		System.out.println("吃饭");
    	}
    
    	public void sleep() {			//睡觉的功能
    		System.out.println("睡觉");
    	}
    }
    
    class Cat extends Animal {
    	
    }
    
    class Dog extends Animal {
    	
    }
    
    /*
    extends是继承的意思
    Animal是父类
    Cat和Dog都是子类
    */
    ```
    
    执行结果:
    
    ```java
    吃饭
    睡觉
    4...花
    请按任意键继续. . .
    ```
    
    

### 08.04_面向对象(继承的好处和弊端)(掌握)

* A:继承的好处
	* a:提高了代码的复用性
	* b:提高了代码的维护性
	* c:让类与类之间产生了关系，是多态的前提
* B:继承的弊端
	* 类的耦合性增强了。
	
	* 开发的原则：高内聚，低耦合。
	* 耦合：类与类的关系
	* 内聚：就是自己完成某件事情的能力

### 08.05_面向对象(Java中类的继承特点)(掌握)

* A:Java中类的继承特点
	* a:Java只支持单继承，不支持多继承。(一个儿子只能有一个爹)
		* 有些语言(python)是支持多继承，格式：extends 类1,类2,...
	* b:Java支持多层继承(继承体系)
* B:案例演示
	* Java中类的继承特点
		* 如果想用这个体系的所有功能用最底层的类创建对象
		
		* 如果想看这个体系的共性功能,看最顶层的类 
		
		  ```java
		  class Demo2_Extends {
		  	public static void main(String[] args) {
		  		DemoC d = new DemoC();
		  		d.show();
		  		d.method();
		  		d.print();
		  
		  	}
		  }
		  /*
		  * A:Java中类的继承特点
		  	* a:Java只支持单继承，不支持多继承。(一个儿子只能有一个爹)
		  		* 有些语言是支持多继承，格式：extends 类1,类2,...
		  	* b:Java支持多层继承(继承体系)
		  * B:案例演示
		  	* Java中类的继承特点
		  		* 如果想用这个体系的所有功能用最底层的类创建对象
		  		* 如果想看这个体系的共性功能,看最顶层的类 
		  */
		  class DemoA {
		  	public void show() {
		  		System.out.println("DemoA");
		  	}
		  }
		  
		  class DemoB extends DemoA {
		  	public void method() {
		  		System.out.println("DemoB");
		  	}
		  }
		  
		  class DemoC extends DemoB {
		  	public void print() {
		  		System.out.println("DemoC");
		  	}
		  }
		  ```
		
		  执行结果:  继承所有父类的方法
		
		  ```java
		  DemoA
		  DemoB
		  DemoC
		  请按任意键继续. . .
		  ```
		
		  

### 08.06_面向对象(继承的注意事项和什么时候使用继承)(掌握)

* A:继承的注意事项
	* a:子类只能继承父类所有非私有的成员(成员方法和成员变量)
	
	  ```java
	  class Demo3_Extends {
	  	public static void main(String[] args) {
	  		Son s = new Son();
	  		s.show();
	  	}
	  }
	  /*
	  * A:继承的注意事项
	  	* a:子类只能继承父类所有非私有的成员(成员方法和成员变量)
	  	* b:子类不能继承父类的构造方法，但是可以通过super(马上讲)关键字去访问父类构造方法。
	  	* c:不要为了部分功能而去继承
	  	* 项目经理 姓名 工号 工资 奖金
	  	* 程序员	姓名 工号 工资
	  */
	  
	  class Father {
	  	private String name;
	  	private void show() {
	  		System.out.println("Hello World!");
	  	}
	  }
	  
	  class Son extends Father {
	  }
	  ```
	
	  执行报错: 不能使用父类的私有方法
	
	  
	
	* b:子类不能继承父类的构造方法，但是可以通过super(马上讲)关键字去访问父类构造方法。
	
	* c:不要为了部分功能而去继承
	
	* 项目经理 姓名 工号 工资 奖金
	
	* 程序员	姓名 工号 工资
* B:什么时候使用继承
  * 继承其实体现的是一种关系："is a"。
  	Person
  		Student
  		Teacher
  	水果
  		苹果
  		香蕉
  		橘子
  		

  采用假设法。
  	如果有两个类A,B。只有他们符合A是B的一种，或者B是A的一种，就可以考虑使用继承。

### 08.07_面向对象(继承中成员变量的关系)(掌握)

* A:案例演示
	* a:不同名的变量
	
* b:同名的变量
	
	  ```java
	  class Demo4_Extends {
	  	public static void main(String[] args) {
	  		Son s = new Son();
	  		s.print();
	  	}
	  }
	  /*
	  * A:案例演示
	  	* a:不同名的变量
	  	* b:同名的变量
	  		子父类出现同名的变量只是在讲课中举例子有,在开发中是不会出现这种情况的
	  		子类继承父类就是为了使用父类的成员,那么如果定义了同名的成员变量没有意义了
	  */
	  
	  class Father {
	  	int num1 = 10;
	  	int num2 = 30;
	  }
	  
	  class Son extends Father {
	  	int num2 = 20;
	  
	  	public void print() {
	  		System.out.println(this.num1);				//this既可以调用本类的,也可以调用父类的(本类没有的情况下)
	  		System.out.println(this.num2);				//就近原则,子类有就不用父类的了
	  		System.out.println(super.num2);             //利用super调用父类
	  	}
	  } 
	  ```
	
	  执行结果:
	
	  ```java
	  10   //父类的num1
	  20   //本类的num2,自己有就就近用
	  30   //使用super调用父类的num2
	  请按任意键继续. . .
	  ```
	
	  
	
### 08.08_面向对象(this和super的区别和应用)(掌握)
* A:this和super都代表什么
	* this:代表当前对象的引用,谁来调用我,我就代表谁
	* super:代表当前对象父类的引用
* B:this和super的使用区别
	* a:调用成员变量
		* this.成员变量 调用本类的成员变量,也可以调用父类的成员变量(本类与父类重名变量的就近调用本类)
		* super.成员变量 调用父类的成员变量
	* b:调用构造方法
		* this(...)	调用本类的构造方法
		* super(...)	调用父类的构造方法
	* c:调用成员方法
		* this.成员方法 调用本类的成员方法,也可以调用父类的方法
		* super.成员方法 调用父类的成员方法
		

### 08.09_面向对象(继承中构造方法的关系)(掌握)

* A:案例演示
	
	* 子类中所有的构造方法默认都会访问父类中空参数的构造方法
	
	  ```java
	  class Demo5_Extends {
	  	public static void main(String[] args) {
	  		Son s = new Son();
	  	}
	  }
	  /*
	  * A:案例演示
	  	* 子类中所有的构造方法默认都会访问父类中空参数的构造方法
	  * B:为什么呢?
	  	* 因为子类会继承父类中的数据，可能还会使用父类的数据。
	  	* 所以，子类初始化之前，一定要先完成父类数据的初始化。
	  	
	  	* 其实：
	  		* 每一个构造方法的第一条语句默认都是：super() Object类最顶层的父类。
	  */
	  
	  class Father extends Object {
	  	public Father() {
	  		super();
	  		System.out.println("Father 的构造方法");
	  	}
	  }
	  
	  class Son extends Father {
	  	public Son() {
	  		super();							//这是一条语句,如果不写,系统会默认加上,用来访问父类中的空参构造
	  		System.out.println("Son 的构造方法");
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  Father 的构造方法   //先执行父类的无参构造方法
	  Son 的构造方法      //执行本类的构造方法
	  请按任意键继续. . .
	  ```
	
	  
* B:为什么呢?
	* 因为子类会继承父类中的数据，可能还会使用父类的数据。
	* 所以，子类初始化之前，一定要先完成父类数据的初始化。
	
	* 其实：
		* 每一个构造方法的第一条语句默认都是：super() Object类最顶层的父类。

### 08.10_面向对象(继承中构造方法的注意事项)(掌握)

* A:案例演示
	* 父类没有无参构造方法,子类怎么办?
	* super解决
	* this解决
* B:注意事项
	
	* super(…)或者this(….)必须出现在构造方法的第一条语句上
	
	  ```java
	  class Demo6_Extends {
	  	public static void main(String[] args) {
	  		Son s1 = new Son();
	  		System.out.println(s1.getName() + "..." + s1.getAge());
	  		System.out.println("--------------------");
	  		Son s2 = new Son("张三",23);
	  		System.out.println(s2.getName() + "..." + s2.getAge());
	  	}
	  }
	  /*
	  * A:案例演示
	  	* 父类没有无参构造方法,子类怎么办?
	  	* super解决
	  	* this解决
	  * B:注意事项
	  	* super(…)或者this(….)必须出现在构造方法的第一条语句上
	  */
	  class Father {
	  	private String name;			//姓名
	  	private int age;				//年龄
	  
	  	public Father() {				//空参构造
	  		System.out.println("Father 空参构造");
	  	}
	  
	  	public Father(String name,int age) {	//有参构造
	  		this.name = name;
	  		this.age = age;
	  		System.out.println("Father 有参构造");
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
	  
	  class Son extends Father {
	  	public Son() {						//空参构造
	  		this("王五",25);				//本类中的有参构造方法
	  		//super("李四",24);				//调用父类中的构造方法     super跟this不能同时用
	  		
	  		System.out.println("Son 空参构造");
	  	}
	  
	  	public Son(String name,int age) {	//有参构造
	  		super(name,age);   //调用父类的有参构造方法(解决父类没有无参构造方法的问题)
	  		System.out.println("Son 有参构造");
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  Father 有参构造    
	  Son 有参构造
	  Son 空参构造
	  王五...25
	       //首先空参构造创建对象,在创建本类对象时开始执行本类的空参构造方法,空参构造方法中使用了this()调用本类的有参构造方法,进入到有参构造方法中,有参构造方法使用了super()调用了父类的有参构造方法,因此进入父类的有参构造方法.所以打印的顺序如上
	  --------------------
	  Father 有参构造
	  Son 有参构造
	  张三...23
	  请按任意键继续. . .
	  ```
	
	  

### 08.11_面向对象(继承中的面试题)(掌握)

* A:案例演示

* ```java
  class Fu{
  	public int num = 10;
  	public Fu(){
  		System.out.println("fu");
  	}
  }
  class Zi extends Fu{
  	public int num = 20;
  	public Zi(){
  		//super();   //默认项
  		System.out.println("zi");
  	}
  	public void show(){
  		int num = 30;
  		System.out.println(num);
  		System.out.println(this.num);  //本类
  		System.out.println(super.num);  //父类
  	}
  }
  class Test1_Extends {
  	public static void main(String[] args) {
  		Zi z = new Zi();   //先输出构造方法中的内容
  		z.show();
  	}
  }
  
  ```

* 执行结果:

  ```java
  fu
  zi
  30
  20
  10
  请按任意键继续. . .
      //首先空参构造对象,先去调用父类的空参构造方法,输出的是fu,然后执行本类的空参构造方法输出的是zi,然后执行的是show函数,一开始打印的是num就是30,然后使用this调用本类的num属性20,最后使用super调用父类的num属性
  ```

  * B案例演示

  ```java
  class Test2_Extends {
  	public static void main(String[] args) {
  		Zi z = new Zi();
  	}
  	/*
  	1,jvm调用了main方法,main进栈
  	2,遇到Zi z = new Zi();
  	会先将Fu.class和Zi.class分别加载进内存,再创建对象,
  	当Fu.class加载进内存
  	父类的静态代码块会随着Fu.class一起加载,当Zi.class加载进内存,子类的静态代码块会随着Zi.class一起加载
  	
  	第一个输出,静态代码块Fu,第二个输出静态代码块Zi
  	3,走Zi类的构造方法,因为java中是分层初始化的,先初始化父类,再初始化子类,所以先走的父类构造,但是在执行
  	父类构造时,发现父类有构造代码块,构造代码块是优先于构造方法执行的所以
  	第三个输出构造代码块Fu,第四个输出构造方法Fu
  	4,Fu类初始化结束,子类初始化,第五个输出的是构造代码块Zi,构造方法Zi
  	*/
  }
  class Fu {
  	static {
  		System.out.println("静态代码块Fu");
  	}
  
  	{
  		System.out.println("构造代码块Fu");
  	}
  
  	public Fu() {
  		System.out.println("构造方法Fu");
  	}
  }
  
  class Zi extends Fu {
  	static {
  		System.out.println("静态代码块Zi");
  	}
  
  	{
  		System.out.println("构造代码块Zi");
  	}
  
  	public Zi() {
  		System.out.println("构造方法Zi");
  	}
  }
  
  
  ```

  执行结果:

  ```java
  静态代码块Fu
  静态代码块Zi
  构造代码块Fu
  构造方法Fu
  构造代码块Zi
  构造方法Zi
  请按任意键继续. . .
      	/*
  	1,jvm调用了main方法,main进栈
  	2,遇到Zi z = new Zi();
  	会先将Fu.class和Zi.class分别加载进内存,再创建对象,
  	当Fu.class加载进内存
  	父类的静态代码块会随着Fu.class一起加载,当Zi.class加载进内存,子类的静态代码块会随着Zi.class一起加载
  	
  	第一个输出,静态代码块Fu,第二个输出静态代码块Zi
  	3,走Zi类的构造方法,因为java中是分层初始化的,先初始化父类,再初始化子类,所以先走的父类构造,但是在执行
  	父类构造时,发现父类有构造代码块,构造代码块是优先于构造方法执行的所以
  	第三个输出构造代码块Fu,第四个输出构造方法Fu
  	4,Fu类初始化结束,子类初始化,第五个输出的是构造代码块Zi,构造方法Zi
  	*/
  ```

  

### 08.12_面向对象(继承中成员方法关系)(掌握)

* A:案例演示
	* a:不同名的方法
	
	* b:同名的方法
	
	  ```java
	  class Demo7_Extends {
	  	public static void main(String[] args) {
	  		Son s = new Son();
	  		s.print();
	  		s.method();
	  	}
	  }
	  /*
	  * a:不同名的方法
	  * b:同名的方法
	  */
	  
	  class Father {
	  	public void print() {
	  		System.out.println("Fu print");
	  	}
	  }
	  
	  class Son extends Father {
	  	public void method() {
	  		System.out.println("Zi Method");
	  	}
	  
	  	public void print() {
	  		super.print();							//super可以调用父类的成员方法
	  		System.out.println("Zi print");
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  Fu print
	  Zi print
	  Zi Method
	  请按任意键继续. . .
	      //优先使用的是本类中有的方法
	  ```
	
	  

### 08.13_面向对象(方法重写概述及其应用)(掌握)

* A:什么是方法重写
	
	* 重写:子父类出现了一模一样的方法(注意:返回值类型可以是子父类,这个我们学完面向对象讲) 
* B:方法重写的应用：
	
	* 当子类需要父类的功能，而功能主体子类有自己特有内容时，可以重写父类中的方法。这样，即沿袭了父类的功能，又定义了子类特有的内容。
* C:案例演示
	
	* a:定义一个手机类。
	
	  ```java
	  class Demo7_Phone {
	  	public static void main(String[] args) {
	  		Ios8 i = new Ios8();
	  		i.siri();
	  		i.call();
	  	}
	  }
	  
	  /*
	  B:方法重写的应用：
	  	* 当子类需要父类的功能，而功能主体子类有自己特有内容时，可以重写父类中的方法。这样，即沿袭了父类的功能，又定义了子类特有的内容。
	  	ios7系统 siri speak English
	  	ios8系统 siri 说中文
	  */
	  
	  class Ios7 {
	  	public void call() {
	  		System.out.println("打电话");
	  	}
	  
	  	public void siri() {
	  		System.out.println("speak English");
	  	}
	  }
	  
	  class Ios8 extends Ios7 {
	  	public void siri() {
	  		
	  		System.out.println("说中文");
	  		super.siri();
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  说中文
	  speak English
	  打电话
	  请按任意键继续. . .
	      //重写方法的同时使用super.方法调用父类的方法,既继承了父类的方法,又有自己特殊的功能
	  ```
	
	  

### 08.14_面向对象(方法重写的注意事项)(掌握)

* A:方法重写注意事项
	* a:父类中私有方法不能被重写
		* 因为父类私有方法子类根本就无法继承
	* b:子类重写父类方法时，访问权限不能更低
		* 最好就一致
	* c:父类静态方法，子类也必须通过静态方法进行重写
		* 其实这个算不上方法重写，但是现象确实如此，至于为什么算不上方法重写，多态中我会讲解(静态只能覆盖静态)
		
	* 子类重写父类方法的时候，最好声明一模一样。
* B:案例演示
	
	* 方法重写注意事项
	
	  
	
	  ```java
	  class Demo8_双桨 {
	  	public static void main(String[] args) {
	  		DayOne d = new DayOne();
	  		d.泡妞();
	  		d.print();
	  	}
	  }
	  /*
	  	* a:父类中私有方法不能被重写
	  		* 因为父类私有方法子类根本就无法继承
	  	* b:子类重写父类方法时，访问权限不能更低
	  		* 最好就一致
	  	* c:父类静态方法，子类也必须通过静态方法进行重写
	  		* 其实这个算不上方法重写，但是现象确实如此，至于为什么算不上方法重写，多态中我会讲解(静态只能覆盖静态)
	  		
	  	* 子类重写父类方法的时候，最好声明一模一样。
	  */
	  class 双桨 {
	  	public void sing() {
	  		System.out.println("唱红歌");
	  	}
	  
	  	public void 泡妞() {
	  		System.out.println("唱红歌搞定林夕合鸟女士");
	  	}
	  
	  	public static void print() {
	  		System.out.println("Fu print");
	  	}
	  }
	  
	  class DayOne extends 双桨 {
	  	public void 泡妞() {
	  		System.out.println("霸王硬上弓");
	  	}
	  
	  	public static void print() {				//静态只能覆盖静态,其实不算重写,多态时候详细讲解
	  		System.out.println("Zi print");
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  霸王硬上弓
	  Zi print
	  请按任意键继续. . .
	      //子类的方法覆盖了父类的方法
	  ```
	
	  

### 08.15_面向对象(方法重写的面试题)(掌握)

* A:方法重写的面试题
	* Override和Overload的区别?Overload能改变返回值类型吗?
	* overload可以改变返回值类型,只看参数列表
	* 方法重写：子类中出现了和父类中方法声明一模一样的方法。与返回值类型有关,返回值是一致(或者是子父类)的
	
	* 方法重载：本类中出现的方法名一样，参数列表不同的方法。与返回值类型无关。

	* 子类对象调用方法的时候：
		* 先找子类本身，再找父类。

### 08.16_面向对象(使用继承前的学生和老师案例)(掌握)

* A:案例演示
	* 使用继承前的学生和老师案例
	
	* 属性:姓名,年龄
	
	* 行为:吃饭
	
	* 老师有特有的方法:讲课
	
	* 学生有特有的方法:学习
	
	  ```java
	  class Test3_Person {
	  	public static void main(String[] args) {
	  		System.out.println("Hello World!");
	  	}
	  }
	  /*
	  * 使用继承前的学生和老师案例
	  	* 属性:姓名,年龄
	  	* 行为:吃饭
	  	* 老师有特有的方法:讲课
	  	* 学生有特有的方法:学习
	  */
	  
	  class Student {
	  	private String name;					//姓名
	  	private int age;						//年龄
	  
	  	public Student() {}						//空参构造
	  
	  	public Student(String name,int age) {	//有参构造
	  		this.name = name;
	  		this.age = age;
	  	}
	  
	  	public void setName(String name) {		//设置姓名
	  		this.name = name;
	  	}
	  
	  	public String getName() {				//获取姓名
	  		return name;
	  	}
	  
	  	public void setAge(int age) {			//设置年龄
	  		this.age = age;
	  	}
	  
	  	public int getAge() {					//获取年龄
	  		return age;
	  	}
	  
	  	public void eat() {						//吃饭
	  		System.out.println("学生吃饭");
	  	}
	  
	  	public void study() {					//学习
	  		System.out.println("学生学习");
	  	}
	  }
	  
	  class Teacher {
	  	private String name;					//姓名
	  	private int age;						//年龄
	  
	  	public Teacher() {}						//空参构造
	  
	  	public Teacher(String name,int age) {	//有参构造
	  		this.name = name;
	  		this.age = age;
	  	}
	  
	  	public void setName(String name) {		//设置姓名
	  		this.name = name;
	  	}
	  
	  	public String getName() {				//获取姓名
	  		return name;
	  	}
	  
	  	public void setAge(int age) {			//设置年龄
	  		this.age = age;
	  	}
	  
	  	public int getAge() {					//获取年龄
	  		return age;
	  	}
	  
	  	public void eat() {						//吃饭
	  		System.out.println("老师吃饭");
	  	}
	  
	  	public void teach() {					//学习
	  		System.out.println("老师讲课");
	  	}
	  }
	  ```
	
	  

### 08.17_面向对象(使用继承后的学生和老师案例)(掌握)

* A:案例演示
	
	* 使用继承后的学生和老师案例
	
	  ```java
	  class Test4_Person {
	  	public static void main(String[] args) {
	  		Student s1 = new Student();
	  		s1.setName("张三");
	  		s1.setAge(23);
	  		System.out.println(s1.getName() + "..." + s1.getAge());
	  		s1.eat();
	  		s1.study();
	  
	  		System.out.println("------------------");
	  		Student s2 = new Student("李四",24);
	  		System.out.println(s2.getName() + "..." + s2.getAge());
	  		s2.eat();
	  		s2.study();
	  	}
	  }
	  /*
	  * 使用继承后的学生和老师案例
	  */
	  
	  class Person {
	  	private String name;					//姓名
	  	private int age;						//年龄
	  
	  	public Person() {}						//空参构造
	  
	  	public Person(String name,int age) {	//有参构造
	  		this.name = name;
	  		this.age = age;
	  	}
	  
	  	public void setName(String name) {		//设置姓名
	  		this.name = name;
	  	}
	  
	  	public String getName() {				//获取姓名
	  		return name;
	  	}
	  
	  	public void setAge(int age) {			//设置年龄
	  		this.age = age;
	  	}
	  
	  	public int getAge() {					//获取年龄
	  		return age;
	  	}
	  
	  	public void eat() {						//吃饭
	  		System.out.println(name  + "吃饭");
	  	}
	  }
	  
	  class Student extends Person {
	  	public Student() {}						//空参构造
	  
	  	public Student(String name,int age) {
	  		super(name,age);
	  	}
	  
	  	public void study() {
	  		System.out.println(this.getName() + "学习");
	  	}
	  }
	  
	  class Teacher extends Person {
	  	public Teacher() {}						//空参构造
	  
	  	public Teacher(String name,int age) {
	  		super(name,age);     //调用父类的有参构造
	  	}
	  
	  	public void teach() {
	  		System.out.println(this.getName() + "讲课");
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  张三...23
	  张三吃饭
	  张三学习
	  ------------------
	  李四...24
	  李四吃饭
	  李四学习
	  请按任意键继续. . .
	  ```
	
	  

### 08.18_面向对象(猫狗案例分析,实现及测试)(掌握)

* A:猫狗案例分析
* B:案例演示
	* 猫狗案例继承版
	
	* 属性:毛的颜色,腿的个数
	
	* 行为:吃饭
	
	* 猫特有行为:抓老鼠catchMouse
	
	* 狗特有行为:看家lookHome
	
	  ```java
	  class Test5_Animal {
	  	public static void main(String[] args) {
	  		Cat c1 = new Cat("花",4);
	  		System.out.println(c1.getColor() + "..." + c1.getLeg());
	  		c1.eat();
	  		c1.catchMouse();
	  
	  		Dog d1 = new Dog("黑",2);
	  		System.out.println(d1.getColor() + "..." + d1.getLeg());
	  		d1.eat();
	  		d1.lookHome();
	  	}
	  }
	  /*
	  * A:猫狗案例分析
	  * B:案例演示
	  	* 猫狗案例继承版
	  	* 属性:毛的颜色,腿的个数
	  	* 行为:吃饭
	  	* 猫特有行为:抓老鼠catchMouse
	  	* 狗特有行为:看家lookHome
	  */
	  
	  class Animal {
	  	private String color;					//毛的颜色
	  	private int leg;						//腿的个数
	  
	  	public Animal(){}
	  
	  	public Animal(String color,int leg) {
	  		this.color = color;
	  		this.leg = leg;
	  	}
	  
	  	public void setColor(String color) {	//设置颜色
	  		this.color = color;
	  	}
	  
	  	public String getColor() {				//获取颜色
	  		return color;
	  	}
	  
	  	public void setLeg(int leg) {			//设置腿的个数
	  		this.leg = leg;
	  	}
	  
	  	public int getLeg() {					//获取腿的个数
	  		return leg;
	  	}
	  
	  	public void eat() {						//吃饭
	  		System.out.println("吃饭");
	  	}
	  }
	  
	  class Cat extends Animal {
	  	public Cat() {}							//空参构造
	  
	  	public Cat(String color,int leg) {		//有参构造
	  		super(color,leg);
	  	}
	  
	  	public void eat() {						//吃鱼
	  		System.out.println("猫吃鱼");
	  	}
	  
	  	public void catchMouse() {				//抓老鼠
	  		System.out.println("抓老鼠");
	  	}
	  }
	  
	  class Dog extends Animal {
	  	public Dog() {}							//空参构造
	  
	  	public Dog(String color,int leg) {		//有参构造
	  		super(color,leg);
	  	}
	  
	  	public void eat() {						//吃肉
	  		System.out.println("狗吃肉");
	  	}
	  
	  	public void lookHome() {				//看家
	  		System.out.println("看家");
	  	}
	  }
	  ```
	
	  

### 08.19_面向对象(final关键字修饰类,方法以及变量的特点)(掌握)

* A:final概述
* B:final修饰特点
	* 修饰类，类不能被继承
	* 修饰变量，变量就变成了常量，只能被赋值一次
	* 修饰方法，方法不能被重写
* C:案例演示
	
	* final修饰特点
	
	  ```java
	  class Demo1_Final {
	  	public static void main(String[] args) {
	  		Son s = new Son();
	  		s.print();
	  	}
	  }
	  /*
	  * A:final概述
	  	final是最终的
	  * B:final修饰特点
	  	* 修饰类，类不能被继承
	  	* 修饰变量，变量就变成了常量，只能被赋值一次
	  	* 修饰方法，方法不能被重写
	  * C:案例演示
	  	* final修饰特点
	  */
	  
	  /*final class Father {
	  	public void print() {
	  		System.out.println("访问底层数据资源");
	  	}
	  }*/
	  
	  class Son /*extends Father*/ {
	  	final int NUM = 10;						//常量命名规范,如果是一个单词,所有字母大写,如果是多个单词,每个单词都大写,中间用下划线隔开
	  	public static final double PI = 3.14;	//final修饰变量叫做常量,一般会与public static共用
	  	public void print() {
	  		//NUM = 20;  //使用了final关键字不能再次赋值
	  		System.out.println(NUM);
	  	}
	  }
	  ```
	
	  

### 08.20_面向对象(final关键字修饰局部变量)(掌握)

* A:案例演示
	* 方法内部或者方法声明上都演示一下(了解)

	* 基本类型，是值不能被改变
	
	* 引用类型，是地址值不能被改变,对象中的属性可以改变
	
	  ```java
	  class Demo2_Final {
	  	public static void main(String[] args) {
	  		final int num = 10;
	  		//num = 20;
	  		System.out.println(num);
	  
	  		final Person p = new Person("张三",23);
	  		//p = new Person("李四",24);
	  		p.setName("李四");
	  		p.setAge(24);
	  
	  		System.out.println(p.getName() + "..." + p.getAge());
	  
	  		method(10);
	  		method(20);
	  	}
	  
	  	public static void method(final int x) {
	  		System.out.println(x);
	  	}
	  }
	  /*
	  * A:案例演示
	  	* 方法内部或者方法声明上都演示一下(了解)
	  
	  	* 基本类型，是值不能被改变
	  	* 引用类型，是地址值不能被改变,对象中的属性可以改变
	  */
	  
	  class Person {
	  	private String name;			//姓名
	  	private int age;				//年龄
	  
	  	public Person(){}				//空参构造
	  
	  	public Person(String name,int age) {
	  		this.name = name;
	  		this.age = age;
	  	}
	  
	  	public void setName(String name) {	//设置姓名
	  		this.name = name;
	  	}
	  
	  	public String getName() {		//获取姓名
	  		return name;
	  	}
	  
	  	public void setAge(int age) {	//设置年龄
	  		this.age = age;
	  	}
	  
	  	public int getAge() {			//获取年龄
	  		return age;
	  	}
	  }
	  ```
	
	  执行结果:
	
	  ```java
	  10  //num是基本数据类型,值不能被改变,因此使用final修饰后不能再次赋值
	  李四...24   //对象属于引用数据类型,创建了新的对象后不能再次创建对象,但是这个对象的属性可以被重新的赋值改变.
	  10
	  20   //method方法中的x也是引用数据类型,因此可以改变属性值
	  请按任意键继续. . .
	  ```
	
	  

### 08.21_面向对象(final修饰变量的初始化时机)(掌握)

* A:final修饰变量的初始化时机
	* 显示初始化 
	
	* 在对象构造完毕前即可
	
	  ```java
	  class Demo3_Final {
	  	public static void main(String[] args) {
	  		Demo d = new Demo();
	  		d.print();
	  	}
	  }
	  /*
	  * A:final修饰变量的初始化时机
	  	* 显示初始化 
	  	* 在对象构造完毕前即可
	  */
	  
	  class Demo {
	  	final int num;						//成员变量的默认初始化值是无效值,所以初始化必须赋值
	  	
	  	public Demo() {   //构造方法初始化
	  		num = 10;
	  	}
	  	public void print() {
	  		System.out.println(num);
	  	}
	  }
	  ```
	
	  
	

执行结果:

```java
10
请按任意键继续. . .
```

