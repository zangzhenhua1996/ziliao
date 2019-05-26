转载于:https://www.jianshu.com/p/2ad360edd219
- 精确率、召回率、F1-score、准确率
   首先来一个我们熟悉的混淆矩阵的图，这是一个二分类的混淆矩阵的图：

  

![ 混淆矩阵](https://upload-images.jianshu.io/upload_images/14555448-7824167eece78542.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


 

| Item  |               说明               | 预测正确与否 |
| :---: | :------------------------------: | :----------: |
|  TP   | 将实际为正样例预测为正样例的个数 |  对，真正类  |
|  TN   | 将实际为负样例预测为负样例的个数 |  对，真负类  |
|  FP   | 将实际为正样例预测为负样例的个数 |  错，假正类  |
|  FN   | 将实际为负样例预测为正样例的个数 |  错，假负类  |
| TP+FP | 总的样例被预测为**正样例**的个数 |              |
| FN+TN | 总的样例被预测为**负样例**的个数 |              |
| TP+FN |         实际的正样例个数         |              |
| FP+TN |         实际的负样例个数         |              |

下标对一些度量的概念和公式进行说明

|     性能度量      |                             公式                             |                             说明                             |
| :---------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 精确率(precision) | $\frac{TP}{TP+FP}$| 分母为预测为正样例的个数，分子为预测为实际正样例被预测准的个数 |
|  召回率(recall)   | $\frac{TP}{TP+FN}$ | 分母为实际正样例的个数，分子为预测为实际正样例被预测准的个数 |
|     F1-score      | $\frac{2TP}{2TP+FP+FN}$ |               混合的度量，对不平衡类别非常有效               |
| 准确率(accuracy)  | $\frac{TP+TN}{TP+FN+FP+FP}$ |                    模型的整体的性能的评估                    |
|    Specificity    | $\frac{TN}{TN+FP}$ | 分母为实际负样例的个数，分子为预测为实际负样例被预测准的个数 |

举个例子：
 我们实际有50个样例，50个负样例，然后经过分类器分类之后。50个正样例中有45个预测为正样例(预测准了)，5个被预测成为了负样例。50个负样例中(预测错误)，有40个被预测为了负样例(预测准了)，10个被预测为了正样例(预测错误)。

| 实际情况 | 预测为正 | 预测为负 |
| :------: | :------: | :------: |
|   50正   |    45    |    5     |
|   50负   |    10    |    40    |

根据这个例子，我们可以计算出：

|     性能度量      |                             公式                             |
| :---------------: | :----------------------------------------------------------: |
| 精确率(precision) | $\frac{TP}{TP+FP}=\frac{45}{55}=0.82$|
|  召回率(recall)   | $\frac{TP}{TP+FN}=\frac{45}{50}=0.90$|
|     F1-score      | $\frac{2TP}{2TP+FP+FN}=\frac{2*45}{2*45+10+5}=0.86$ |
| 准确率(accuracy)  | $\frac{TP+TN}{TP+FN+FP+FP}=\frac{85}{100}=0.85$|
|    Specificity    | $\frac{TN}{TN+FP}=\frac{40}{50}=0.80$ |

下图很形象的说明了精确率和召回率的计算



![image.png](https://upload-images.jianshu.io/upload_images/14555448-b5e538c1c06b66b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




- ROC和AUC曲线

   ROC = The receiver operating curve，翻译过来就是受试者工作曲线，这条曲线的横轴为假正例率、纵轴是真正例率。
$\begin{aligned} T P R &=\frac{T P}{T P+F N} \\ T P R &=\frac{F P}{T N+F N} \end{aligned}$
  

  

   AUC = the area under the receiving operating curve。也就下图中蓝色部分的区域
![image.png](https://upload-images.jianshu.io/upload_images/14555448-74d73c5d90505512.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  


 
   理想目标：TPR=1，FPR=0,即图中(0,1)点，故ROC曲线越靠拢(0,1)点，越偏离45度对角线越好。

