SymPy是Python的数学符号计算库，用它可以进行数学公式的符号推导 
安装不介绍了 [官方文档](http://docs.sympy.org/) 这里还是建议使用anaconda

```
from sympy import *
init_printing(use_unicode=True)
x,y = symbols('x y')  #用符号代表变量，多个变量可以空格，可以逗号隔开。
expr = x + 2*y
expanded_expr = expand(x*expr) #expand 展开
factor(expanded_expr) # factor合并
diff(sin(x)*exp(x), x) #对x求导
integrate(exp(x)*sin(x) + exp(x)*cos(x), x) #对x求不定积分
integrate(sin(x**2), (x, -oo, oo)) #对x求定积分
limit(sin(x)/x, x, 0) #x趋于0的极限
solve(x**2 - 2,x) #求方程的解
Matrix([[1, 2], [2, 2]]).eigenvals() #求矩阵特征值
latex(Integral(cos(x)**2, (x, 0, pi))) #查看latex格式
expr = x + 1
expr.subs(x,y) # y+1 替代方法subs
Eq(x + 1, 4) # 建立方程 x+1 = 4 
a = (x + 1)**2
b = x**2 + 2*x + 1
simplify(a-b) # 0 用这个方法验证两个方程是否相等
a.equals(b) #或者equals方法验证
Rational(1, 2) 分数表示

expr = expr = sqrt(8)
expr.evalf(chop =True) #小数表示，去掉 Round-off error

expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
collect(expr, x) #collect，对x合并同类项
cancel((x**2 + 2*x + 1)/(x**2 + x)) #cancel函数约分
expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x) 
apart(expr) #拆分
asin(1) #反三角函数
trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4) #trigsimp简化三角函数
expand_trig(sin(x + y)) #分解三角函数
powsimp(x**a*x**b) #简化指数运算
```
解方程： 
7）solveset()可以对方程进行符号求解，它的第一个参数是表示方程的表达式，其后的参数是表示方程中未知量的符号。

求导： 
8）Derivative是表示导函数的类，它的第一个参数是需要进行求导的数学函数，第二个参数是求导的自变量，注意：Derivative所得到的是一个导函数，它不会进行求导运算。t=Derivative(sin(x),x) 
9）调用doit()方法求出导函数。t.doit() 
10）也可以直接使用diff()函数或表达式的diff()方法来计算导函数。diff(sin(2*x),x)或sin(2*x).diff(x)。 
11）添加更多的符号参数可以表示高阶导函数，如：Derivative(f(x),x,x,x)，也可以表示多个变量的导函数，如：Derivative(f(x,y),x,2,y,3)

求微分： 
12）dsolve()可以对微分方程进行符号求解，它的第一个参数是一个带未知函数的表达式，第二个参数是需要进行求解的未知函数。它在解微分方程中可以传递hint参数，指定微分方程的解法，若设置为“best”则放dsolve()尝试所有的方法并返回最简单的解。 
求积分： 
13）integrate(f,x):计算不定积分；integrate(f,(x,a,b)):计算定积分；integrate(f,x,y):计算双重不定积分；integrate(f,(x,a,b),(y,a,b)):计算双重定积分。
