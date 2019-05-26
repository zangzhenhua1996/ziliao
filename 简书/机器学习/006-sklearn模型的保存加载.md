这次主要介绍两种保存Model的模块pickle与joblib。
## 使用 pickle 保存 [](https://morvanzhou.github.io/tutorials/machine-learning/sklearn/3-5-save/#使用-pickle-保存 "Permalink to this headline")

首先简单建立与训练一个`SVC`Model。

```python
from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X,y)

```

使用`pickle`来**保存**与**读取**训练好的Model。

```python
import pickle #pickle模块

#保存Model(注:save文件夹要预先建立，否则会报错)
with open('save/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)

#读取Model
with open('save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)
    #测试读取后的Model
    print(clf2.predict(X[0:1]))



```
执行结果:
```python
# [0]
```

## 使用 joblib 保存 [](https://morvanzhou.github.io/tutorials/machine-learning/sklearn/3-5-save/#使用-joblib-保存 "Permalink to this headline")

`joblib`是`sklearn`的外部模块。

```
from sklearn.externals import joblib #jbolib模块

#保存Model(注:save文件夹要预先建立，否则会报错)
joblib.dump(clf, 'save/clf.pkl')

#读取Model
clf3 = joblib.load('save/clf.pkl')

#测试读取后的Model
print(clf3.predict(X[0:1]))

# [0]

```

最后可以知道`joblib`在使用上比较容易，读取速度也相对`pickle`快
