# problem 1
返回输入数字中6出现的次数，简单

# problem 2
pingpong数列首项为1，随后每项在前一项的基础上加1或减1，初始时为加1，若第n（从1开始）项的n满足`n%6 == 0`或n（十进制）中含有数字6，则加减转换。

题目要求使用递归法。（提示：两个函数互相调用也可构成递归）

# problem 3
返回给定整数中满足条件的数字的个数，简单

# problem 4
给定货币面额系统，返回面值等于total的货币组合个数

思路：
1. 递推公式：设组合个数为count(total,m),其中m为货币面额,令total = m + total',则有:`count(total,m) = count(total',m) + count(total,m')`,其中m'=next(m)(即货币系统中下一个比m大的面额)
2. 结束条件：`total < m or m is None`

# problem 5
经典汉诺塔问题

思路：设除start和end外的第三根柱子为mid,则move_stack(n,start,end)可分解为三步：
1. move_stack(n-1,start,mid)
2. move_stack(1,start,end)
3. move_stack(n-1,mid,end)
终止条件：n==1时为最简形式，直接移动即可

# problem 6
要求返回高阶函数，carrying问题

尝试了大概两个小时，最后参考[stackoverflow](https://stackoverflow.com/questions/39544604/python-recursion-challenge)解决这道题。

这题的关键是认识到这一点：`n>1`时每层返回的函数阶数加1,另外还需要传参，因此返回要有两层lambda。

# problem 7
在不给函数命名的情况下实现阶乘函数

思路：用一个匿名函数实现函数调用自身，另一个匿名函数实现递归的逻辑，后者作为前者的参数
[参考](https://zhuanlan.zhihu.com/p/661364887)

# problem 8
Y是实现匿名递归的通用函数

