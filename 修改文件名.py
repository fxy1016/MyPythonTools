# _*_ coding:utf-8 _*_
# @Time : 2022/9/30 20:09
# @Author : fx
# @File : 修改文件名
# @Project : MyPythonTools
# 来源：https://blog.csdn.net/m0_51126511/article/details/124433311

import re
import os

# 输入你要更改文件的目录 注意最后没有\
# E:\视频\bilibili
path = ""

originalName = '原名'  # 1234是要查找文件名里包含123的文件
replaceName = '我要改成的名字'  # 4321是要被替换的字符串，如果就是删除originalName，那么replaceName = ''就可以


def main1(path1):
    files = os.listdir(path1)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        if os.path.isdir(path1 + '\\' + file):
            main1(path1 + '\\' + file)
        else:
            files2 = os.listdir(path1 + '\\')
            for file1 in files2:
                if originalName in file1:
                    n = str(path1 + '\\' + file1.replace(originalName, replaceName))
                    n1 = str(path1 + '\\' + str(file1))
                    try:
                        os.rename(n1, n)
                    except IOError:
                        continue


main1(path)
