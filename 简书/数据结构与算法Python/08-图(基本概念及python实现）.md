## 图的基本术语
* 有向图：图中的每条边都有方向的图叫有向图。此时，边的两个顶点有次序关系，有向边 < u,v>成为从顶点u到顶点v的一条弧，u成为弧尾（始点），v成为弧头（终点），即有向图中弧 < u,v>和弧 < v,u> 表示不同的两条边。
* 无向图：图中的每条边没有方向的图。边的两个顶点没有次序关系，无向图用边(u,v)表示对称弧< u,v>和< v,u>。
* 权：图中的边或弧上有附加的数量信息，这种可反映边或弧的某种特征的数据成为权。
* 网：图上的边或弧带权则称为网。可分为有向网和无向网。
* 邻接和关联：若边e=(u,v)或弧e= < u,v>，则称点u和v互为邻接顶点，并称边e或弧e关联于顶点u和v。
* 度：在无向图中，与顶点v关联的边的条数成为顶点v的度。有向图中，则以顶点v为弧尾的弧的条数成为顶点v的出度，以顶点v为弧头的弧的条数成为顶点v的入度，而顶点v的度=出度+入度。图中各点度数之和是边（或弧）的条数的2倍。
* 圈：图中联接同一个顶点的边叫圈。
* 平行边：图中两个顶点之间若有两条或两条以上的边，称这些边为平行边。
* 简单图：没有圈也没有平行边的图。
* 有向完全图：有n个顶点，n(n-1)条弧的有向图。每两个顶点之间都有两条方向相反的边连接的图。
* 完全图：有n个顶点，n(n-1)/2条边的无向图。若一个图的每一对不同顶点恰有一条边相连，则称为完全图。完全图是每对顶点之间都恰连有一条边的简单图。
* 路径长度：路径上边或弧的数目。若路径上的各顶点均不相同，则称这条路经为简单路经（或路），除第一个和最后一个顶点相同外，其他各顶点均不相同的路径成为回路（或环）。
* 连通图：在无向图G中，对与图中的任意两个顶点u、v都是连通的，则称图G为连通图。
* 强连通图：在有向图G中，如果对于每一对Vi和Vj 属于顶点集V，Vi不等于Vj ，从Vi到Vj和从Vj到Vi都存在路径，则称G是强连通图。
* 强连通分量：有向图中的极大强连通子图称做有向图的强连通分量。
* 生成树：一个连通图的生成树是一个极小的连通子图，它含有图中全部的n个顶点，但只有足以构成一棵树的n-1条边。
* 有向树：如果一个有向图恰有一个顶点的入度为0，其余顶点的入度为1，则是一棵有向树。
## 图的存储结构
图的存储结构，常用的是”邻接矩阵”和”邻接表”。
### 邻接矩阵
邻接矩阵是指用矩阵来表示图。它是采用矩阵来描述图中顶点之间的关系(及弧或边的权)。 
假设图中顶点数为n，则邻接矩阵定义为： 
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4c9bdf5fa6d15382.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
下面通过示意图来进行解释。 
![image.png](https://upload-images.jianshu.io/upload_images/14555448-1e9880ff3c5d0e9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
图中的G1是无向图和它对应的邻接矩阵。

![image.png](https://upload-images.jianshu.io/upload_images/14555448-47ad7ab9f295c32c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
图中的G2是无向图和它对应的邻接矩阵。

通常采用两个数组来实现邻接矩阵：一个一维数组用来保存顶点信息，一个二维数组来用保存边的信息。 
邻接矩阵的缺点就是比较耗费空间。
### 2. 邻接表
邻接表是图的一种链式存储表示方法。它是改进后的”邻接矩阵”，它的缺点是不方便判断两个顶点之间是否有边，但是相对邻接矩阵来说更省空间。 
![image.png](https://upload-images.jianshu.io/upload_images/14555448-382001959ed45866.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图中的G1是无向图和它对应的邻接矩阵。 

![image.png](https://upload-images.jianshu.io/upload_images/14555448-18c058e2f81479d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
图中的G2是无向图和它对应的邻接矩阵。
## 图的python实现
在Python中，图主要是通过列表和词典来构造。比如说下面这张图，
```python
     A --> B
     A --> C
     B --> C
     B --> D
     C --> D
     D --> C
     E --> F
     F --> C
```
就是通过下面这个字典和列表的结合进行构造
```python
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
```
### 实现的功能：

* 寻找一条路径
* 查找所有的路径
* 查找最短路径
#### 完整的代码实现：
```python
#!/usr/bin/env python3

# -*- encoding:utf-8 -*-
''' A --> B
 A --> C
 B --> C
 B --> D
 C --> D
 D --> C
 E --> F
 F --> C



'''


def find_path(graph, start, end, path=[]):
        '寻找一条路径'
        #首先从起始点开始遍历他指向的下一个节点的路径，直到找到终点的路径，然后返回
        path = path + [start]  #一开始的路径默认是空[],首先将start其实点进行添加,列表加列表还是同维度的列表
        if start == end: #进行递归操作的终止条件,遍历到了最后的终止点就返回路径
            return path  #返回的路径都是要满足有起始点和终点的
        if not start in graph.keys(): #如果start不是起始的点的话，也就不在字典的键中，这条路径就是错的，不能到达指定的终点的路径          
            return None #返回空
        for node in graph[start]: #node是start键指向的多个路径点，graph[start]对应的值
            if node not in path: #如果说这个node没有在路径path中的话，对它进行遍历路径，找到终点，在的话就不用了
                newpath = find_path(graph, node, end, path) #node就是新的需要遍历的起始值，同时将前面的已经产生的路径进传递
                if newpath:
                    return newpath 
        return path #只要是找到了一条路径那么就返回没有进行所有路径的存储

def find_all_paths(graph, start, end, path=[]):
        '查找所有的路径'
        path = path + [start]
        if start == end:
            return [path] #这里返回的是一个列表
        if not start in graph.keys():
            return [] #返回的不是空而是一个空的列表
        paths = [] #这是最终返回的所有的路径
        for node in graph[start]: #进行遍历
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)  #返回的是多个路径
                for newpath in newpaths: #将返回的路径进行添加到最后需要返回的路径中
                    paths.append(newpath)
        return paths #返回最后的总的路径

def find_shortest_path(graph, start, end, path=[]):
        '查找最短路径'
        #跟找一条路径是类似的，只不过设置了一个最短的值进行记录最后将最短的路径进行返回即可
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath: #进行最短路径的更新
                    if not shortest or len(newpath) < len(shortest):  #not shortest 将首先返回的路径作为初始的最短的路径
                        shortest = newpath
        return shortest
    
# 寻找的是不包含自己到自己本身的图中的全部的路径
def find_all_graph_path(graph):
    list_key=list(graph.keys()) # 将所有的起始点存到一个列表中
    result =[]  
    for i in range(len(list_key)):
        list_temp=list_key[:i]+list_key[i+1:] #不包含自己到自己的图的路径
        for num in list_temp:
            temp_path=find_all_paths(graph,list_key[i],num) #不同节点之间遍历返回的路径
            if temp_path!=[] : #如果存在的话,存到最后的结果中
                for temp_path_1 in temp_path:
                    if len(temp_path_1)>1:
                        result.append(temp_path_1)
    return result
if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D','A'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    print (find_path(graph,'A','D'))
    print (find_all_paths(graph,'A','D'))
    print(find_shortest_path(graph, 'A', 'D'))
    print(find_all_graph_path(graph))

```
