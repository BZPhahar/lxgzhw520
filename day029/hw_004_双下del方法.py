# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:52
# 文件名称: hw_004_双下del方法.py
# 开发工具: PyCharm

class A:
    # 析构函数 再删除一个文件之前进行一些收尾的工作
    def __del__(self):
        print("执行销毁方法")


a = A()
# 主动删除
del a
# 程序结束删除
b = A()
