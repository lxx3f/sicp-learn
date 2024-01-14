

# problem 2.2
注意:只要有一个臂是不平衡的就可以直接判定整个系统不平衡了,我一开始犯了一个错误,
就是在检查完左臂后再检查右臂时没有考虑res可能已经被修改成False了,这时若继续检查
右臂,且右臂是平衡的,就会导致res被覆盖为True导致出错

# problem 3.1
(参考)[https://www.cnblogs.com/xddxd/p/17250785.html#_label0]

# problem 4
在preorder两层list转一层list这一步卡了很久,一直没想到要怎么处理
