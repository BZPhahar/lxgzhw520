# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 20:18
# 文件名称: hw_013_打印今天是星期几.py
# 开发工具: PyCharm

# if 是最常用的判断法


# 如果要你判断今天是星期几


# 让用户输入 1-7 七个数字,根据这个数字,去判断,今天是星期几


# 输入函数  录入数据  输出函数 输出数据

day = input("请输入今天是一周的第几天:")

if day == '1':
    print('星期一')
# ..........
elif day == '7':
    print('星期天')
else:
    print('输入错误')
