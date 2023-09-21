# -*- coding:utf-8 -*-
# @Time:    2022/11/5 10:14
# @Author:  FangYi
# @File:    柱状图.py

import matplotlib.pyplot as plt
import numpy as np


name = ['Wind10M','V10M','DC','V1000hpa','T2M','RH2M','U10M','U1000hpa','T1000hpa','HM10M','PSFC','CLDT','RAINT01h',]
data = [47.35, 12.73, 9.97, 7.45, 4.2, 4.11, 3.71, 2.17, 2.04, 1.91, 1.61, 1.51, 1.24]
# 创建一个点数为 19 x 8 的画布, 并设置分辨率为 900像素/每英寸
plt.figure(figsize=(19, 8), dpi=400)
# 柱子总数
N = 13
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.8
# 绘制柱状图, 并指定柱子的颜色
p1 = plt.bar(index, data, width,  color="skyblue")
plt.bar_label(p1, label_type='edge',fontsize=13)   # label_type=‘edge’表示将数据值标签放在柱子顶端，label_type=‘center’表示将数据值标签放在柱子中间。
# 设置横轴标签
plt.xlabel('Features', fontsize=16)
# 设置纵轴标签
plt.ylabel('Importance (%)',fontsize=16)
# 添加横轴的刻度
plt.xticks(index, name, fontsize=15)
# 添加纵轴的刻度
plt.yticks(np.arange(0, 50, 10), fontsize=15)
# 添加图例
font1 = {'family':'Times New Roman','size': 16}
plt.legend(["Importance"], loc="upper right", prop=font1)   # 设置字体大小
plt.savefig('柱状图.png', bbox_inches='tight')   # 去除画布留白
plt.show()  # 显示图像
