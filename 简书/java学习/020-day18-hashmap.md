# Map接口概述

- Map接口概述

  •    将键映射到值的对象

  •    一个映射不能包含重复的键

  •    每个键最多只能映射到一个值

- Map接口和Collection接口的不同

  •    Map是双列的,Collection是单列的

  •    Map的键唯一,Collection的子体系Set是唯一的

  •    Map集合的数据结构值针对键有效，跟值无关

Collection集合的数据结构是针对元素有效

# Map接口成员方法

- V put(K key,V value)

- V remove(Object key)

- void clear()

- boolean containsKey(Object key)

- boolean containsValue(Object value)

- boolean isEmpty()
-  int size()

# Map接口成员方法

 V get(Object key)

 Set<K> keySet()

 Collection<V> values()

 Set<Map.Entry<K,V>> entrySet()
```java
package cn.itcast_01;

import java.util.HashMap;
import java.util.Map;

/*
 * 作为学生来说，是根据学号来区分不同的学生的，那么假设我现在已经知道了学生的学号，我要根据学号去获取学生姓名，请问怎么做呢?
 * 如果采用前面讲解过的集合，我们只能把学号和学生姓名作为一个对象的成员，然后存储整个对象，将来遍历的时候，判断，获取对应的名称。
 * 但是呢，如果我都能把学生姓名拿出来了，我还需要根据编号去找吗?
 * 针对我们目前的这种需求：仅仅知道学号，就想知道学生姓名的情况，Java就提供了一种新的集合 Map。
 * 通过查看API，我们知道Map集合的一个最大的特点，就是它可以存储键值对的元素。这个时候存储我们上面的需求，就可以这样做
 * 		学号1		姓名1
 * 		学号2 	姓名2
 * 		学号3		姓名3
 * 		学号2(不行)姓名4
 * 		学号4               姓名4
 * Map集合的特点：
 * 		将键映射到值的对象。一个映射不能包含重复的键；每个键最多只能映射到一个值。 
 * 
 * Map集合和Collection集合的区别?
 * 		Map集合存储元素是成对出现的，Map集合的键是唯一的，值是可重复的。可以把这个理解为：夫妻对
 * 		Collection集合存储元素是单独出现的，Collection的儿子Set是唯一的，List是可重复的。可以把这个理解为：光棍(11.11)
 * 
 * 注意：
 * 		Map集合的数据结构值针对键有效，跟值无关	
 * 			HashMap，TreeMap等会讲。
 *		Collection集合的数据结构是针对元素有效
 * 
 * Map集合的功能概述：
 * 1:添加功能
 * 		V put(K key,V value):添加元素。这个其实还有另一个功能?先不告诉你，等会讲
 * 			如果键是第一次存储，就直接存储元素，返回null
 * 			如果键不是第一次存在，就用值把以前的值替换掉，返回以前的值
 * 2:删除功能
 * 		void clear():移除所有的键值对元素
 * 		V remove(Object key)：根据键删除键值对元素，并把值返回
 * 3:判断功能
 * 		boolean containsKey(Object key)：判断集合是否包含指定的键
 * 		boolean containsValue(Object value):判断集合是否包含指定的值
 * 		boolean isEmpty()：判断集合是否为空
 * 4:获取功能
 * 		Set<Map.Entry<K,V>> entrySet():???
 * 		V get(Object key):根据键获取值
 * 		Set<K> keySet():获取集合中所有键的集合
 * 		Collection<V> values():获取集合中所有值的集合
 * 5：长度功能
 * 		int size()：返回集合中的键值对的对数
 */
public class MapDemo {
	public static void main(String[] args) {
		// 创建集合对象
		Map<String, String> map = new HashMap<String, String>(); // 一个是键一个是值

		// 添加元素
		// V put(K key,V value):添加元素。这个其实还有另一个功能?先不告诉你，等会讲
		// System.out.println("put:" + map.put("文章", "马伊俐"));
		// System.out.println("put:" + map.put("文章", "姚笛"));

		map.put("邓超", "孙俪");
		map.put("黄晓明", "杨颖");
		map.put("周杰伦", "蔡依林");
		map.put("刘恺威", "杨幂");

		// void clear():移除所有的键值对元素
		// map.clear();

		// V remove(Object key)：根据键删除键值对元素，并把值返回
		// System.out.println("remove:" + map.remove("黄晓明"));
		// System.out.println("remove:" + map.remove("黄晓波"));

		// boolean containsKey(Object key)：判断集合是否包含指定的键
		// System.out.println("containsKey:" + map.containsKey("黄晓明"));
		// System.out.println("containsKey:" + map.containsKey("黄晓波"));

		// boolean isEmpty()：判断集合是否为空
		// System.out.println("isEmpty:"+map.isEmpty());

		// int size()：返回集合中的键值对的对数
		System.out.println("size:" + map.size());

		// 输出集合名称
		System.out.println("map:" + map);
	}
}
```
```java
package cn.itcast_01;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/*
 * 获取功能：
 * V get(Object key):根据键获取值
 * Set<K> keySet():获取集合中所有键的集合
 * Collection<V> values():获取集合中所有值的集合
 */
public class MapDemo2 {
	public static void main(String[] args) {
		// 创建集合对象
		Map<String, String> map = new HashMap<String, String>();

		// 创建元素并添加元素
		map.put("邓超", "孙俪");
		map.put("黄晓明", "杨颖");
		map.put("周杰伦", "蔡依林");
		map.put("刘恺威", "杨幂");

		// V get(Object key):根据键获取值
		System.out.println("get:" + map.get("周杰伦")); //get功能
		System.out.println("get:" + map.get("周杰")); // 返回null
		System.out.println("----------------------");

		// Set<K> keySet():获取集合中所有键的集合
		Set<String> set = map.keySet();
		for (String key : set) {
			System.out.println(key);
		}
		System.out.println("----------------------");

		// Collection<V> values():获取集合中所有值的集合
		Collection<String> con = map.values();
		for (String value : con) {
			System.out.println(value);
		}
	}
}
```
# Map集合遍历

- 方式1：根据键找值

  •    获取所有键的集合

  •    遍历键的集合，获取到每一个键

  •    根据键找值
```java
package cn.itcast_01;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/*
 * Map集合的遍历。
 * Map -- 夫妻对
 * 思路：
 * 		A:把所有的丈夫给集中起来。
 * 		B:遍历丈夫的集合，获取得到每一个丈夫。
 * 		C:让丈夫去找自己的妻子。
 * 
 * 转换：
 * 		A:获取所有的键
 * 		B:遍历键的集合，获取得到每一个键
 * 		C:根据键去找值
 */
public class MapDemo3 {
	public static void main(String[] args) {
		// 创建集合对象
		Map<String, String> map = new HashMap<String, String>();

		// 创建元素并添加到集合
		map.put("杨过", "小龙女");
		map.put("郭靖", "黄蓉");
		map.put("杨康", "穆念慈");
		map.put("陈玄风", "梅超风");

		// 遍历
		// 获取所有的键
		Set<String> set = map.keySet();
		// 遍历键的集合，获取得到每一个键
		for (String key : set) {
			// 根据键去找值
			String value = map.get(key);  //get方法
			System.out.println(key + "---" + value);
		}
	}
}
```
- 方式2：根据键值对对象找键和值

  •    获取所有键值对对象的集合

  •    遍历键值对对象的集合，获取到每一个键值对对象

  •    根据键值对对象找键和值
```java
package cn.itcast_01;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/*
 * Map集合的遍历。
 * Map -- 夫妻对
 * 
 * 思路：
 * 		A:获取所有结婚证的集合
 * 		B:遍历结婚证的集合，得到每一个结婚证
 * 		C:根据结婚证获取丈夫和妻子
 * 
 * 转换：
 * 		A:获取所有键值对对象的集合
 * 		B:遍历键值对对象的集合，得到每一个键值对对象
 * 		C:根据键值对对象获取键和值
 * 
 * 这里面最麻烦的就是键值对对象如何表示呢?
 * 看看我们开始的一个方法：
 * 		Set<Map.Entry<K,V>> entrySet()：返回的是键值对对象的集合
 */
public class MapDemo4 {
	public static void main(String[] args) {
		// 创建集合对象
		Map<String, String> map = new HashMap<String, String>();

		// 创建元素并添加到集合
		map.put("杨过", "小龙女");
		map.put("郭靖", "黄蓉");
		map.put("杨康", "穆念慈");
		map.put("陈玄风", "梅超风");

		// 获取所有键值对对象的集合
		Set<Map.Entry<String, String>> set = map.entrySet();
		// 遍历键值对对象的集合，得到每一个键值对对象
		for (Map.Entry<String, String> me : set) { //Map.Entry<String, String>键值对对象
			// 根据键值对对象获取键和值
			String key = me.getKey();
			String value = me.getValue();
			System.out.println(key + "---" + value);
		}
	}
}
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-3a9eeabef6987b12.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# HashMap类概述

- HashMap类概述

  •    键是哈希表结构，可以保证键的唯一性

- HashMap案例

  •    HashMap<String,String>

  •    HashMap<Integer,String>

  •    HashMap<String,Student>

  •    HashMap<Student,String>
```java
package cn.itcast_02;

import java.util.HashMap;
import java.util.Set;

/*
 * HashMap:是基于哈希表的Map接口实现。
 * 哈希表的作用是用来保证键的唯一性的。
 * 
 * HashMap<String,String>
 * 键：String
 * 值：String
 */
public class HashMapDemo {
	public static void main(String[] args) {
		// 创建集合对象
		HashMap<String, String> hm = new HashMap<String, String>();

		// 创建元素并添加元素
		// String key1 = "it001";
		// String value1 = "马云";
		// hm.put(key1, value1);

		hm.put("it001", "马云");
		hm.put("it003", "马化腾");
		hm.put("it004", "乔布斯");
		hm.put("it005", "张朝阳");
		hm.put("it002", "裘伯君"); // wps
		hm.put("it001", "比尔盖茨");

		// 遍历
		Set<String> set = hm.keySet();
		for (String key : set) {
			String value = hm.get(key);
			System.out.println(key + "---" + value);
		}
	}
}

```
测试2
```java
package cn.itcast_02;

import java.util.HashMap;
import java.util.Set;

/*
 * HashMap<Integer,String>
 * 键：Integer
 * 值：String
 */
public class HashMapDemo2 {
	public static void main(String[] args) {
		// 创建集合对象
		HashMap<Integer, String> hm = new HashMap<Integer, String>();

		// 创建元素并添加元素
		// Integer i = new Integer(27);
		// Integer i = 27;
		// String s = "林青霞";
		// hm.put(i, s);

		hm.put(27, "林青霞");
		hm.put(30, "风清扬");
		hm.put(28, "刘意");
		hm.put(29, "林青霞");

		// 下面的写法是八进制，但是不能出现8以上的单个数据
		// hm.put(003, "hello");
		// hm.put(006, "hello");
		// hm.put(007, "hello");
		// hm.put(008, "hello");

		// 遍历
		Set<Integer> set = hm.keySet();
		for (Integer key : set) {
			String value = hm.get(key);
			System.out.println(key + "---" + value);
		}

		// 下面这种方式仅仅是集合的元素的字符串表示
		// System.out.println("hm:" + hm);
	}
}

```
创建自定义的对象
student类
```java
package cn.itcast_02;

public class Student {
	private String name;
	private int age;

	public Student() { // alt+shift+s 选c
		super();
	}

	public Student(String name, int age) { // alt+shift+s 选o
		super();
		this.name = name;
		this.age = age;
	}

	public String getName() { // alt+shift+s 选r
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + age;
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Student other = (Student) obj;
		if (age != other.age)
			return false;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		return true;
	}

}
```
测试的类
```java
package cn.itcast_02;

import java.util.HashMap;
import java.util.Set;

/*
 * HashMap<String,Student>
 * 键：String	学号
 * 值：Student 学生对象
 */
public class HashMapDemo3 {
	public static void main(String[] args) {
		// 创建集合对象
		HashMap<String, Student> hm = new HashMap<String, Student>();

		// 创建学生对象
		Student s1 = new Student("周星驰", 58);
		Student s2 = new Student("刘德华", 55);
		Student s3 = new Student("梁朝伟", 54);
		Student s4 = new Student("刘嘉玲", 50);

		// 添加元素
		hm.put("9527", s1);
		hm.put("9522", s2);
		hm.put("9524", s3);
		hm.put("9529", s4);

		// 遍历
		Set<String> set = hm.keySet(); // 获取所有的键值
		for (String key : set) {
			// 注意了：这次值不是字符串了
			// String value = hm.get(key);
			Student value = hm.get(key); // 是student对象
			System.out.println(key + "---" + value.getName() + "---"
					+ value.getAge());
		}
	}
}

```
执行
```java
9524---梁朝伟---54
9522---刘德华---55
9527---周星驰---58
9529---刘嘉玲---50
```

 * HashMap<Student,String>
 * 键：Student
 * 要求：如果两个对象的成员变量值都相同，则为同一个对象。
 * 值：String
 这里的学生类是要重写hashcode的方法的使用的是快捷键 :alt+shift+s 选h
测试:
```java
package cn.itcast_02;

import java.util.HashMap;
import java.util.Set;

/*
 * HashMap<Student,String>
 * 键：Student
 * 		要求：如果两个对象的成员变量值都相同，则为同一个对象。
 * 值：String
 */
public class HashMapDemo4 {
	public static void main(String[] args) {
		// 创建集合对象
		HashMap<Student, String> hm = new HashMap<Student, String>();

		// 创建学生对象
		Student s1 = new Student("貂蝉", 27);
		Student s2 = new Student("王昭君", 30);
		Student s3 = new Student("西施", 33);
		Student s4 = new Student("杨玉环", 35);
		Student s5 = new Student("貂蝉", 27);

		// 添加元素 //s1根s5应该是同一个需要重写方法
		hm.put(s1, "8888");
		hm.put(s2, "6666");
		hm.put(s3, "5555");
		hm.put(s4, "7777");
		hm.put(s5, "9999");

		// 遍历
		Set<Student> set = hm.keySet();
		for (Student key : set) {
			String value = hm.get(key);
			System.out.println(key.getName() + "---" + key.getAge() + "---"
					+ value);
		}
	}
}
```

# LinkedHashMap类概述

-  Map 接口的哈希表和链接列表实现，具有可预知的迭代顺序。

```java
package cn.itcast_03;

import java.util.LinkedHashMap;
import java.util.Set;

/*
 * LinkedHashMap:是Map接口的哈希表和链接列表实现，具有可预知的迭代顺序。
 * 由哈希表保证键的唯一性
 * 由链表保证键盘的有序(存储和取出的顺序一致)
 */
public class LinkedHashMapDemo {
	public static void main(String[] args) {
		// 创建集合对象
		LinkedHashMap<String, String> hm = new LinkedHashMap<String, String>();

		// 创建并添加元素
		hm.put("2345", "hello");
		hm.put("1234", "world");
		hm.put("3456", "java");
		hm.put("1234", "javaee");
		hm.put("3456", "android");

		// 遍历
		Set<String> set = hm.keySet();
		for (String key : set) {
			String value = hm.get(key);
			System.out.println(key + "---" + value);
		}
	}
}

```
# TreeMap类概述

- TreeMap类概述

  •    键是红黑树结构，可以保证键的排序和唯一性

- TreeMap案例

  •    HashMap<String,String>
```java
package cn.itcast_04;

import java.util.Set;
import java.util.TreeMap;

/*
 * TreeMap:是基于红黑树的Map接口的实现。
 * 
 * HashMap<String,String>
 * 键：String
 * 值：String
 */
public class TreeMapDemo {
	public static void main(String[] args) {
		// 创建集合对象
		TreeMap<String, String> tm = new TreeMap<String, String>();

		// 创建元素并添加元素
		tm.put("hello", "你好");
		tm.put("world", "世界");
		tm.put("java", "爪哇");
		tm.put("world", "世界2");
		tm.put("javaee", "爪哇EE");

		// 遍历集合
		Set<String> set = tm.keySet();
		for (String key : set) {
			String value = tm.get(key);
			System.out.println(key + "---" + value);
		}
	}
}

```
执行
```java
hello---你好
java---爪哇
javaee---爪哇EE
world---世界2
```
  •    HashMap<Student,String>
student类
```java
package cn.itcast_04;

public class Student {
	private String name;
	private int age;

	public Student() {
		super();
	}

	public Student(String name, int age) {
		super();
		this.name = name;
		this.age = age;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}
}
```
使用要实现Comparator
```java
package cn.itcast_04;

import java.util.Comparator;
import java.util.Set;
import java.util.TreeMap;

/*
 * TreeMap<Student,String>
 * 键:Student
 * 值：String
 */
public class TreeMapDemo2 {
	public static void main(String[] args) {
		// 创建集合对象
		TreeMap<Student, String> tm = new TreeMap<Student, String>(
				new Comparator<Student>() {
					@Override
					public int compare(Student s1, Student s2) {
						// 主要条件
						int num = s1.getAge() - s2.getAge();
						// 次要条件
						int num2 = num == 0 ? s1.getName().compareTo(
								s2.getName()) : num;
						return num2;
					}
				});

		// 创建学生对象
		Student s1 = new Student("潘安", 30);
		Student s2 = new Student("柳下惠", 35);
		Student s3 = new Student("唐伯虎", 33);
		Student s4 = new Student("燕青", 32);
		Student s5 = new Student("唐伯虎", 33);

		// 存储元素
		tm.put(s1, "宋朝");
		tm.put(s2, "元朝");
		tm.put(s3, "明朝");
		tm.put(s4, "清朝");
		tm.put(s5, "汉朝");

		// 遍历
		Set<Student> set = tm.keySet();
		for (Student key : set) {
			String value = tm.get(key);
			System.out.println(key.getName() + "---" + key.getAge() + "---"
					+ value);
		}
	}
}
```
# Map集合案例

- "aababcabcdabcde",获取字符串中每一个字母出现的次数要求结果:a(5)b(4)c(3)d(2)e(1)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-7bd58e900471c7db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```java
package cn.itcast_05;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

/*
 * 需求 ："aababcabcdabcde",获取字符串中每一个字母出现的次数要求结果:a(5)b(4)c(3)d(2)e(1)
 * 
 * 分析：
 * 		A:定义一个字符串(可以改进为键盘录入)
 * 		B:定义一个TreeMap集合
 * 			键:Character
 * 			值：Integer
 * 		C:把字符串转换为字符数组
 * 		D:遍历字符数组，得到每一个字符
 * 		E:拿刚才得到的字符作为键到集合中去找值，看返回值
 * 			是null:说明该键不存在，就把该字符作为键，1作为值存储
 * 			不是null:说明该键存在，就把值加1，然后重写存储该键和值
 * 		F:定义字符串缓冲区变量
 * 		G:遍历集合，得到键和值，进行按照要求拼接
 * 		H:把字符串缓冲区转换为字符串输出
 * 
 * 录入：linqingxia
 * 结果：result:a(1)g(1)i(3)l(1)n(2)q(1)x(1)
 */
public class TreeMapDemo {
	public static void main(String[] args) {
		// 定义一个字符串(可以改进为键盘录入)
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入一个字符串：");
		String line = sc.nextLine();

		// 定义一个TreeMap集合
		TreeMap<Character, Integer> tm = new TreeMap<Character, Integer>();

		// 把字符串转换为字符数组
		char[] chs = line.toCharArray();

		// 遍历字符数组，得到每一个字符
		for (char ch : chs) {
			// 拿刚才得到的字符作为键到集合中去找值，看返回值
			Integer i = tm.get(ch);

			// 是null:说明该键不存在，就把该字符作为键，1作为值存储
			if (i == null) {
				tm.put(ch, 1);
			} else {
				// 不是null:说明该键存在，就把值加1，然后重写存储该键和值
				i++; // 尽管i是引用类型但是有自动拆箱装箱,Integer的功能
				tm.put(ch, i);
			}
		}

		// 定义字符串缓冲区变量StringBuilder,可变长度
		StringBuilder sb = new StringBuilder();

		// 遍历集合，得到键和值，进行按照要求拼接
		Set<Character> set = tm.keySet();
		for (Character key : set) {
			Integer value = tm.get(key);
			sb.append(key).append("(").append(value).append(")");
		}

		// 把字符串缓冲区转换为字符串输出
		String result = sb.toString();
		System.out.println("result:" + result);
	}
}

```
执行
```java
请输入一个字符串：
zangzhenhua
result:a(2)e(1)g(1)h(2)n(2)u(1)z(2)
```

- 集合的嵌套遍历

  •    HashMap嵌套HashMap
```java
package cn.itcast_05;

import java.util.HashMap;
import java.util.Set;

/*
 * HashMap嵌套HashMap
 * 
 * 传智播客
 * 		jc	基础班
 * 				陈玉楼		20
 * 				高跃			22
 * 		jy	就业班
 * 				李杰			21
 * 				曹石磊		23
 * 
 * 先存储元素，然后遍历元素
 */
public class HashMapDemo2 {
	public static void main(String[] args) {
		// 创建集合对象 传智播客 键是jc 值是又一个hashmap
		HashMap<String, HashMap<String, Integer>> czbkMap = new HashMap<String, HashMap<String, Integer>>();

		// 创建基础班集合对象
		HashMap<String, Integer> jcMap = new HashMap<String, Integer>();
		// 添加元素
		jcMap.put("陈玉楼", 20);
		jcMap.put("高跃", 22);
		// 把基础班添加到大集合
		czbkMap.put("jc", jcMap);

		// 创建就业班集合对象
		HashMap<String, Integer> jyMap = new HashMap<String, Integer>();
		// 添加元素
		jyMap.put("李杰", 21);
		jyMap.put("曹石磊", 23);
		// 把基础班添加到大集合
		czbkMap.put("jy", jyMap);

		// 遍历集合 遍历比较复杂一点
		Set<String> czbkMapSet = czbkMap.keySet();
		for (String czbkMapKey : czbkMapSet) {
			System.out.println(czbkMapKey);
			HashMap<String, Integer> czbkMapValue = czbkMap.get(czbkMapKey);
			Set<String> czbkMapValueSet = czbkMapValue.keySet();
			for (String czbkMapValueKey : czbkMapValueSet) {
				Integer czbkMapValueValue = czbkMapValue.get(czbkMapValueKey);
				System.out.println("\t" + czbkMapValueKey + "---"
						+ czbkMapValueValue);
			}
		}
	}
}
```
执行
```java
jc
	高跃---22
	陈玉楼---20
jy
	曹石磊---23
	李杰---21
```

  •    HashMap嵌套ArrayList
```java
package cn.itcast_05;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

/*
 *需求：
 *假设HashMap集合的元素是ArrayList。有3个。
 *每一个ArrayList集合的值是字符串。
 *元素我已经完成，请遍历。
 *结果：
 *		 三国演义
 *		 	吕布
 *		 	周瑜
 *		 笑傲江湖
 *		 	令狐冲
 *		 	林平之
 *		 神雕侠侣
 *		 	郭靖
 *		 	杨过  
 */
public class HashMapIncludeArrayListDemo {
	public static void main(String[] args) {
		// 创建集合对象
		HashMap<String, ArrayList<String>> hm = new HashMap<String, ArrayList<String>>();

		// 创建元素集合1
		ArrayList<String> array1 = new ArrayList<String>();
		array1.add("吕布");
		array1.add("周瑜");
		hm.put("三国演义", array1);

		// 创建元素集合2
		ArrayList<String> array2 = new ArrayList<String>();
		array2.add("令狐冲");
		array2.add("林平之");
		hm.put("笑傲江湖", array2);

		// 创建元素集合3
		ArrayList<String> array3 = new ArrayList<String>();
		array3.add("郭靖");
		array3.add("杨过");
		hm.put("神雕侠侣", array3);
		
		//遍历集合
		Set<String> set = hm.keySet();
		for(String key : set){
			System.out.println(key);
			ArrayList<String> value = hm.get(key);
			for(String s : value){
				System.out.println("\t"+s);
			}
		}
	}
}
```
执行
  •    ArrayList嵌套HashMap
```java
package cn.itcast_05;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

/*
 ArrayList集合嵌套HashMap集合并遍历。
 需求：
 假设ArrayList集合的元素是HashMap。有3个。
 每一个HashMap集合的键和值都是字符串。
 元素我已经完成，请遍历。
 结果：
 周瑜---小乔
 吕布---貂蝉

 郭靖---黄蓉
 杨过---小龙女

 令狐冲---任盈盈
 林平之---岳灵珊
 */
public class ArrayListIncludeHashMapDemo {
	public static void main(String[] args) {
		// 创建集合对象
		ArrayList<HashMap<String, String>> array = new ArrayList<HashMap<String, String>>();

		// 创建元素1
		HashMap<String, String> hm1 = new HashMap<String, String>();
		hm1.put("周瑜", "小乔");
		hm1.put("吕布", "貂蝉");
		// 把元素添加到array里面
		array.add(hm1);

		// 创建元素1
		HashMap<String, String> hm2 = new HashMap<String, String>();
		hm2.put("郭靖", "黄蓉");
		hm2.put("杨过", "小龙女");
		// 把元素添加到array里面
		array.add(hm2);

		// 创建元素1
		HashMap<String, String> hm3 = new HashMap<String, String>();
		hm3.put("令狐冲", "任盈盈");
		hm3.put("林平之", "岳灵珊");
		// 把元素添加到array里面
		array.add(hm3);

		// 遍历
		for (HashMap<String, String> hm : array) {
			Set<String> set = hm.keySet();
			for (String key : set) {
				String value = hm.get(key);
				System.out.println(key + "---" + value);
			}
		}
	}
}
```
更复杂的嵌套
```java
package cn.itcast_06;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

/*
 * 为了更符合要求：
 * 		这次的数据就看成是学生对象。
 * 
 * 传智播客
 * 		bj	北京校区
 * 			jc	基础班
 * 					林青霞		27
 * 					风清扬		30
 * 			jy	就业班	
 * 					赵雅芝		28
 * 					武鑫		29
 * 		sh	上海校区
 * 			jc	基础班
 * 					郭美美		20
 * 					犀利哥		22
 * 			jy	就业班	
 * 					罗玉凤		21
 * 					马征		23
 * 		gz	广州校区
 * 			jc	基础班
 * 					王力宏		30
 * 					李静磊		32
 * 			jy	就业班	
 * 					郎朗		31
 * 					柳岩		33
 * 		xa	西安校区
 * 			jc	基础班
 * 					范冰冰		27
 * 					刘意		30
 * 			jy	就业班	
 * 					李冰冰		28
 * 					张志豪		29
 */
public class HashMapDemo {
	public static void main(String[] args) {
		// 创建大集合
		HashMap<String, HashMap<String, ArrayList<Student>>> czbkMap = new HashMap<String, HashMap<String, ArrayList<Student>>>();

		// 北京校区数据
		HashMap<String, ArrayList<Student>> bjCzbkMap = new HashMap<String, ArrayList<Student>>();
		ArrayList<Student> array1 = new ArrayList<Student>();
		Student s1 = new Student("林青霞", 27);
		Student s2 = new Student("风清扬", 30);
		array1.add(s1);
		array1.add(s2);
		ArrayList<Student> array2 = new ArrayList<Student>();
		Student s3 = new Student("赵雅芝", 28);
		Student s4 = new Student("武鑫", 29);
		array2.add(s3);
		array2.add(s4);
		bjCzbkMap.put("基础班", array1);
		bjCzbkMap.put("就业班", array2);
		czbkMap.put("北京校区", bjCzbkMap);

		// 晚上可以自己练习一下
		// 上海校区数据自己做
		// 广州校区数据自己做

		// 西安校区数据
		HashMap<String, ArrayList<Student>> xaCzbkMap = new HashMap<String, ArrayList<Student>>();
		ArrayList<Student> array3 = new ArrayList<Student>();
		Student s5 = new Student("范冰冰", 27);
		Student s6 = new Student("刘意", 30);
		array3.add(s5);
		array3.add(s6);
		ArrayList<Student> array4 = new ArrayList<Student>();
		Student s7 = new Student("李冰冰", 28);
		Student s8 = new Student("张志豪", 29);
		array4.add(s7);
		array4.add(s8);
		xaCzbkMap.put("基础班", array3);
		xaCzbkMap.put("就业班", array4);
		czbkMap.put("西安校区", xaCzbkMap);

		// 遍历集合
		Set<String> czbkMapSet = czbkMap.keySet();
		for (String czbkMapKey : czbkMapSet) {
			System.out.println(czbkMapKey);
			HashMap<String, ArrayList<Student>> czbkMapValue = czbkMap
					.get(czbkMapKey);
			Set<String> czbkMapValueSet = czbkMapValue.keySet();
			for (String czbkMapValueKey : czbkMapValueSet) {
				System.out.println("\t" + czbkMapValueKey);
				ArrayList<Student> czbkMapValueValue = czbkMapValue
						.get(czbkMapValueKey);
				for (Student s : czbkMapValueValue) {
					System.out.println("\t\t" + s.getName() + "---"
							+ s.getAge());
				}
			}
		}
	}
}

```
# 面试题

- HashMap和Hashtable的区别
- List,Set,Map等接口是否都继承子Map接口
```java
package cn.itcast_07;

import java.util.Hashtable;

/*
 * 1:Hashtable和HashMap的区别?
 * Hashtable:线程安全，效率低。不允许null键和null值
 * HashMap:线程不安全，效率高。允许null键和null值
 * 
 * 2:List,Set,Map等接口是否都继承子Map接口?
 * List，Set不是继承自Map接口，它们继承自Collection接口
 * Map接口本身就是一个顶层接口
 */
public class HashtableDemo {
	public static void main(String[] args) {
		// HashMap<String, String> hm = new HashMap<String, String>();
		Hashtable<String, String> hm = new Hashtable<String, String>();

		hm.put("it001", "hello");
		// hm.put(null, "world"); //NullPointerException
		// hm.put("java", null); // NullPointerException

		System.out.println(hm);
	}
}
```

# Collections类概述和成员方法

- Collections类概述

  •    针对集合操作的工具类

- Collections成员方法

  •    public static <T> void sort(List<T> list)

  •    public static <T> int binarySearch(List<?> list,T key)

  •    public static <T> T max(Collection<?> coll)

  •    public static void reverse(List<?> list)

  •    public static void shuffle(List<?> list)
```java
package cn.itcast_01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
 * Collections:是针对集合进行操作的工具类，都是静态方法。
 * 
 * 面试题：
 * Collection和Collections的区别?
 * Collection:是单列集合的顶层接口，有子接口List和Set。
 * Collections:是针对集合操作的工具类，有对集合进行排序和二分查找的方法
 * 
 * 要知道的方法
 * public static <T> void sort(List<T> list)：排序 默认情况下是自然顺序。
 * public static <T> int binarySearch(List<?> list,T key):二分查找
 * public static <T> T max(Collection<?> coll):最大值
 * public static void reverse(List<?> list):反转
 * public static void shuffle(List<?> list):随机置换
 */
public class CollectionsDemo {
	public static void main(String[] args) {
		// 创建集合对象
		List<Integer> list = new ArrayList<Integer>();

		// 添加元素
		list.add(30);
		list.add(20);
		list.add(50);
		list.add(10);
		list.add(40);

		System.out.println("list:" + list);

		// public static <T> void sort(List<T> list)：排序 默认情况下是自然顺序。
		Collections.sort(list);
		System.out.println("list:" + list);
		// [10, 20, 30, 40, 50]

		// public static <T> int binarySearch(List<?> list,T key):二分查找
		// System.out
		// .println("binarySearch:" + Collections.binarySearch(list, 30));
		// System.out.println("binarySearch:"
		// + Collections.binarySearch(list, 300));

		// public static <T> T max(Collection<?> coll):最大值
		// System.out.println("max:"+Collections.max(list));

		// public static void reverse(List<?> list):反转
		// Collections.reverse(list);
		// System.out.println("list:" + list);

		// public static void shuffle(List<?> list):随机置换
		Collections.shuffle(list);
		System.out.println("list:" + list);
	}
}

```
自定义对象
student类
```java
package cn.itcast_02;

/**
 * @author Administrator
 * 
 */
public class Student implements Comparable<Student> {
	private String name;
	private int age;

	public Student() {
		super();
	}

	public Student(String name, int age) {
		super();
		this.name = name;
		this.age = age;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override  //重写compareTo的方法
	public int compareTo(Student s) {
		int num = this.age - s.age;
		int num2 = num == 0 ? this.name.compareTo(s.name) : num;
		return num2;
	}
}

```
使用
```java
package cn.itcast_02;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/*
 * Collections可以针对ArrayList存储基本包装类的元素排序，存储自定义对象可不可以排序呢?
 */
public class CollectionsDemo {
	public static void main(String[] args) {
		// 创建集合对象
		List<Student> list = new ArrayList<Student>();

		// 创建学生对象
		Student s1 = new Student("林青霞", 27);
		Student s2 = new Student("风清扬", 30);
		Student s3 = new Student("刘晓曲", 28);
		Student s4 = new Student("武鑫", 29);
		Student s5 = new Student("林青霞", 27);

		// 添加元素对象
		list.add(s1);
		list.add(s2);
		list.add(s3);
		list.add(s4);
		list.add(s5);

		// 排序
		// 自然排序
		// Collections.sort(list); //这个是调用了student的自然排序
		// 比较器排序
		// 如果同时有自然排序和比较器排序，以比较器排序为主
		Collections.sort(list, new Comparator<Student>() {
			@Override
			public int compare(Student s1, Student s2) {
				int num = s2.getAge() - s1.getAge();
				int num2 = num == 0 ? s1.getName().compareTo(s2.getName())
						: num;
				return num2;
			}
		});

		// 遍历集合
		for (Student s : list) {
			System.out.println(s.getName() + "---" + s.getAge());
		}
	}
}
```
# Collections成员方法的使用

- 模拟斗地主洗牌和发牌

- 模拟斗地主洗牌和发牌

  •     对牌进行排序

  •     并同时使用Map,List,Set等集合，可以知道什么时候使用哪种集合
```java
package cn.itcast_03;

import java.util.ArrayList;
import java.util.Collections;

/*
 * 模拟斗地主洗牌和发牌
 * 
 * 分析：
 * 		A:创建一个牌盒
 * 		B:装牌
 * 		C:洗牌
 * 		D:发牌
 * 		E:看牌
 */
public class PokerDemo {
	public static void main(String[] args) {
		// 创建一个牌盒
		ArrayList<String> array = new ArrayList<String>();

		// 装牌
		// 黑桃A,黑桃2,黑桃3,...黑桃K
		// 红桃A,...
		// 梅花A,...
		// 方块A,...
		// 定义一个花色数组
		String[] colors = { "♠", "♥", "♣", "♦" };
		// 定义一个点数数组
		String[] numbers = { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
				"J", "Q", "K" };
		// 装牌 //循环完就能添加除了大小王的所有牌
		for (String color : colors) {
			for (String number : numbers) {
				array.add(color.concat(number));
			}
		}
		array.add("小王");
		array.add("大王");

		// 洗牌
		Collections.shuffle(array);

		System.out.println("array:" + array);

		// 发牌
		ArrayList<String> fengQingYang = new ArrayList<String>();
		ArrayList<String> linQingXia = new ArrayList<String>();
		ArrayList<String> liuYi = new ArrayList<String>();
		ArrayList<String> diPai = new ArrayList<String>();

		for (int x = 0; x < array.size(); x++) {
			if (x >= array.size() - 3) {
				diPai.add(array.get(x));
			} else if (x % 3 == 0) {
				fengQingYang.add(array.get(x));
			} else if (x % 3 == 1) {
				linQingXia.add(array.get(x));
			} else if (x % 3 == 2) {
				liuYi.add(array.get(x));
			}
		}

		// 看牌
		lookPoker("风清扬", fengQingYang);
		lookPoker("林青霞", linQingXia);
		lookPoker("刘意", liuYi);

		lookPoker("底牌", diPai);
	}

	public static void lookPoker(String name, ArrayList<String> array) {
		System.out.print(name + "的牌是：");
		for (String s : array) {
			System.out.print(s + " ");
		}
		System.out.println();
	}
}
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-c65df2fb2ff4ea9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```java
package cn.itcast_04;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.TreeSet;

/*
 * 思路：
 * 		A:创建一个HashMap集合
 * 		B:创建一个ArrayList集合
 * 		C:创建花色数组和点数数组
 * 		D:从0开始往HashMap里面存储编号，并存储对应的牌
 *        同时往ArrayList里面存储编号即可。
 *      E:洗牌(洗的是编号)
 *      F:发牌(发的也是编号，为了保证编号是排序的，就创建TreeSet集合接收)
 *      G:看牌(遍历TreeSet集合，获取编号，到HashMap集合找对应的牌)
 */
public class PokerDemo {
	public static void main(String[] args) {
		// 创建一个HashMap集合
		HashMap<Integer, String> hm = new HashMap<Integer, String>();

		// 创建一个ArrayList集合
		ArrayList<Integer> array = new ArrayList<Integer>();

		// 创建花色数组和点数数组
		// 定义一个花色数组
		String[] colors = { "♠", "♥", "♣", "♦" };
		// 定义一个点数数组
		String[] numbers = { "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
				"K", "A", "2", };

		// 从0开始往HashMap里面存储编号，并存储对应的牌,同时往ArrayList里面存储编号即可。
		int index = 0;

		for (String number : numbers) {
			for (String color : colors) {
				String poker = color.concat(number);
				hm.put(index, poker);
				array.add(index);
				index++;
			}
		}
		hm.put(index, "小王");
		array.add(index);
		index++;
		hm.put(index, "大王");
		array.add(index);

		// 洗牌(洗的是编号)
		Collections.shuffle(array);

		// 发牌(发的也是编号，为了保证编号是排序的，就创建TreeSet集合接收)
		TreeSet<Integer> fengQingYang = new TreeSet<Integer>();
		TreeSet<Integer> linQingXia = new TreeSet<Integer>();
		TreeSet<Integer> liuYi = new TreeSet<Integer>();
		TreeSet<Integer> diPai = new TreeSet<Integer>();

		for (int x = 0; x < array.size(); x++) {
			if (x >= array.size() - 3) {
				diPai.add(array.get(x));
			} else if (x % 3 == 0) {
				fengQingYang.add(array.get(x));
			} else if (x % 3 == 1) {
				linQingXia.add(array.get(x));
			} else if (x % 3 == 2) {
				liuYi.add(array.get(x));
			}
		}

		// 看牌(遍历TreeSet集合，获取编号，到HashMap集合找对应的牌)
		lookPoker("风清扬", fengQingYang, hm);
		lookPoker("林青霞", linQingXia, hm);
		lookPoker("刘意", liuYi, hm);
		lookPoker("底牌", diPai, hm);
	}

	// 写看牌的功能
	public static void lookPoker(String name, TreeSet<Integer> ts,
			HashMap<Integer, String> hm) {
		System.out.print(name + "的牌是：");
		for (Integer key : ts) {
			String value = hm.get(key);
			System.out.print(value + " ");
		}
		System.out.println();
	}
}
```
# 集合总结

- 集合

  •    Collection

  •    List • Set

  •    Map
```java
1:Map(掌握)
	(1)将键映射到值的对象。一个映射不能包含重复的键；每个键最多只能映射到一个值。 
	(2)Map和Collection的区别?
		A:Map 存储的是键值对形式的元素，键唯一，值可以重复。夫妻对
		B:Collection 存储的是单独出现的元素，子接口Set元素唯一，子接口List元素可重复。光棍
	(3)Map接口功能概述(自己补齐)
		A:添加功能
		B:删除功能
		C:判断功能
		D:获取功能
		E:长度功能
	(4)Map集合的遍历
		A:键找值
			a:获取所有键的集合
			b:遍历键的集合,得到每一个键
			c:根据键到集合中去找值
		
		B:键值对对象找键和值
			a:获取所有的键值对对象的集合
			b:遍历键值对对象的集合，获取每一个键值对对象
			c:根据键值对对象去获取键和值
			
		代码体现：
			Map<String,String> hm = new HashMap<String,String>();
			
			hm.put("it002","hello");
			hm.put("it003","world");
			hm.put("it001","java");
			
			//方式1 键找值
			Set<String> set = hm.keySet();
			for(String key : set) {
				String value = hm.get(key);
				System.out.println(key+"---"+value);
			}
			
			//方式2 键值对对象找键和值
			Set<Map.Entry<String,String>> set2 = hm.entrySet();
			for(Map.Entry<String,String> me : set2) {
				String key = me.getKey();
				String value = me.getValue();
				System.out.println(key+"---"+value);
			}
	(5)HashMap集合的练习
		A:HashMap<String,String>
		B:HashMap<Integer,String>
		C:HashMap<String,Student>
		D:HashMap<Student,String>
	(6)TreeMap集合的练习		
		A:TreeMap<String,String>
		B:TreeMap<Student,String>
	(7)案例
		A:统计一个字符串中每个字符出现的次数
		B:集合的嵌套遍历
			a:HashMap嵌套HashMap
			b:HashMap嵌套ArrayList
			c:ArrayList嵌套HashMap
			d:多层嵌套
			
2:Collections(理解)	
	(1)是针对集合进行操作的工具类
	(2)面试题：Collection和Collections的区别
		A:Collection 是单列集合的顶层接口，有两个子接口List和Set
		B:Collections 是针对集合进行操作的工具类，可以对集合进行排序和查找等
	(3)常见的几个小方法：
		A:public static <T> void sort(List<T> list)
		B:public static <T> int binarySearch(List<?> list,T key)
		C:public static <T> T max(Collection<?> coll)
		D:public static void reverse(List<?> list)
		E:public static void shuffle(List<?> list)
	(4)案例
		A:ArrayList集合存储自定义对象的排序
		B:模拟斗地主洗牌和发牌
		C:模拟斗地主洗牌和发牌并对牌进行排序

```
