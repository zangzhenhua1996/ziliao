# 五、数据的完整性

作用：保证用户输入的数据保存到数据库中是正确的。

确保数据的完整性 = 在创建表时给表中添加约束

完整性的分类：

- 实体完整性:
- 域完整性:
- 引用完整性:

 

## 1、实体完整性

实体：即表中的一行(一条记录)代表一个实体（entity）

实体完整性的作用：标识每一行数据不重复。

**约束类型：** **主键约束（primary key)**  **唯一约束(unique)**  **自动增长列(auto_increment)**

 

### 1.1主键约束（primary key）

注：每个表中要有一个主键。

特点：数据唯一，且不能为null

例：

第一种添加方式：

```sql
CREATE TABLE student(

id int primary key,

name varchar(50)

);
```



第二种添加方式：此种方式优势在于，可以创建联合主键

```sql
CREATE TABLE student(

id int,

name varchar(50),

primary key(id)

);  #主键直接方法primary key()的函数中

CREATE TABLE student(

classid int,

stuid int,

name varchar(50),

primary key(classid，stuid)

);  #这里就可以使用联合主键(不可分割)类似于二进制
```



第三种添加方式：

```sql
CREATE TABLE student(
id int,
name varchar(50)
);
ALTER TABLE student  ADD  PRIMARY  KEY (id);
```



### 1.2唯一约束(unique)：         

### 特点：数据不能重复。

```sql
CREATE TABLE student(

Id int primary key,

Name varchar(50) unique

);
```



### 1.3自动增长列(auto_increment)  

### sqlserver数据库 (identity)  oracle数据库( sequence)

 

给主键添加自动增长的数值，列只能是整数类型

```sql
CREATE TABLE student(
Id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(50)
);
INSERT INTO student(NAME) VALUES('tom');
```





## 2、域完整性

域完整性的作用：限制此单元格的数据正确，不对照此列的其它单元格比较

域代表当前单元格

域完整性约束：数据类型 非空约束（not null） 默认值约束(default)  

​								check约束（mysql不支持）check(sex='男' or  sex='女')

### 1.1 数据类型:（数值类型、日期类型、字符串类型）

### 1.2 非空约束：not null

```sql
CREATE TABLE student(
Id INT PRIMARY KEY,
NAME VARCHAR(50) NOT NULL,
Sex VARCHAR(10)
);
INSERT INTO student VALUES(1,'tom',NULL);
```



 

### 1.3 默认值约束 default

```sql
DROP TABLE student;
CREATE TABLE student(
Id INT PRIMARY KEY,
NAME VARCHAR(50) NOT NULL,
Sex VARCHAR(10) DEFAULT '男'
);
INSERT INTO student VALUES(1,'tom','女');
INSERT INTO student VALUES(2,'jerry',DEFAULT);
```



## 3、引用完整性（参照完整性）

外键约束：FOREIGN KEY 

例：

```sql
-- 外键约束：FOREIGN KEY 
CREATE TABLE stu1(
sid INT PRIMARY KEY,
NAME VARCHAR(50) NOT NULL,
sex VARCHAR(10) DEFAULT '男'
);
-- CONSTRAINT fk_stu1_score1_sid FOREIGN KEY (sid) REFERENCES student(id)
-- 一个约束,约束的名字叫fk_stu1_score1_sid 是外键约束sid 参照学生表stu1的sid
CREATE TABLE score1(
id INT,
score INT,
sid INT , -- 外键列的数据类型一定要与主键的类型一致
CONSTRAINT fk_stu1_score1_sid FOREIGN KEY (sid) REFERENCES stu1(sid)
);

```

第二种添加外键方式。

```sql
ALTER TABLE score1 ADD CONSTRAINT fk_stu1_score1_sid FOREIGN KEY(sid) REFERENCES stu1(id);
```


![图片.png](https://upload-images.jianshu.io/upload_images/14555448-b1d8346530590f06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




## 4、　表与表之间的关系

- 一对一：例如t_person表和t_card表，即人和身份证。这种情况需要找出主从关系，即谁是主表，谁是从表。人可以没有身份证，但身份证必须要有人才行，所以人是主表，而身份证是从表。设计从表可以有两种方案：

  Ø  在t_card表中添加外键列（相对t_user表），并且给外键添加唯一约束；

  Ø  给t_card表的主键添加外键约束（相对t_user表），即t_card表的主键也是外键。

- 一对多（多对一）：最为常见的就是一对多！一对多和多对一，这是从哪个角度去看得出来的。t_user和t_section的关系，从t_user来看就是一对多，而从t_section的角度来看就是多对一！这种情况都是在多方创建外键！


- 多对多：例如t_stu和t_teacher表，即一个学生可以有多个老师，而一个老师也可以有多个学生。这种情况通常需要创建中间表来处理多对多关系。例如再创建一张表t_stu_tea表，给出两个外键，一个相对t_stu表的外键，另一个相对t_teacher表的外键。

![图片.png](https://upload-images.jianshu.io/upload_images/14555448-75318895e83d0738.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![图片.png](https://upload-images.jianshu.io/upload_images/14555448-9e1bd7a4d100cc02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```sql
-- 多对多的关系
use mydb1;
-- 老师表
create table teacher(
tid int primary key,
tname varchar(20)
);
 -- 学生表
create table stu2(
sid int primary key,
sname varchar(20) 
);
 -- 外键表
 create table tea_stu_rel(
tid int,
sid int 
 );
-- 修改外键的表,添加外键
alter table tea_stu_rel add constraint fk_tid foreign key(tid) references teacher(tid);

ALTER TABLE tea_stu_rel ADD CONSTRAINT fk_sid FOREIGN KEY(sid) REFERENCES stu2(sid);



-- 一对一
-- QQ表
create table QQ(
qqid int primary key,
password varchar(50)
);
-- 详细信息
create table QQDetail(
qqid int primary key,
name varchar(50),
address varchar(200)
);
alter table QQDetail add constraint fk_QQ foreign key(qqid) references QQ(qqid);
```
拆表是方便查询存储方便
![图片.png](https://upload-images.jianshu.io/upload_images/14555448-6ba30ec22eb691b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

