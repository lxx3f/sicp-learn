
# problem 7 
参考:https://www.cnblogs.com/echoT/p/16032880.html

我的思路:显然可以用递归解决,
1. 递推条件:对于给定的start和goal,若两者第一个字母相同,则不需要修改,即`minimum_mewtations(start,goal,limit) = minimum_mewtations(start[1:],goal[1:],limit)`;
若不同,则分别尝试三种操作,得到新的start记为start',即`minimum_mewtations(start,goal,limit) = 1 + minimum_mewtations(start',goal,limit-1)`;
2. 递归基:当len(goal)==0或len(start)==0时返回另一个的长度即可,当差异超过limit时直接返回limit+1即可(确保时间复杂度较低)

# extension:final diff
考虑交换相邻字符的操作,未测试