[] is None
Out[19]: False

not []
Out[20]: True

not [[]]
Out[21]: False

[[]] is None
Out[23]: False


is None 比较实用判断树的节点存在不存在,但是判断列表是不是空绝对不能使用is None
要是用 not list
while list 等等的条件
