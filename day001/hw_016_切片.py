# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 20:30
# 文件名称: hw_016_切片.py
# 开发工具: PyCharm

list2 = [1, 2, 3, 4, 5]

# 切片  就是截取其中的一个片段
# 0.....n
# 取第0个数到 第三个数
print(list2[0:3])  # 切片不会把结尾的数切下来
print(list2[3])

# 可以跳着且
list2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ]
print(list2[0:10:2])

# 比较特殊用法 反着切片
list2 = [1, 2, 3, 4, 5]
# 怎么把它倒过来
print(list2[::-1])
