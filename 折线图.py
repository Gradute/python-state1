# -*- coding:utf-8 -*-
# @Time:    2022/11/5 10:14
# @Author:  FangYi
# @File:    折线图.py

import numpy as np
import matplotlib.pyplot as plt

time = list(range(1, 13))
time_RMSE = np.load('time_RMSE_n_hour.npy')
xgb_RMSE = time_RMSE[:, 1].astype(float)
MOS_RMSE = time_RMSE[:, 3].astype(float)
NWP_RMSE = time_RMSE[:, 4].astype(float)

plt.figure(figsize=(12, 8), dpi=300)  # 设置画布的尺寸
in1, = plt.plot(time, xgb_RMSE, color="deeppink", linewidth=2, linestyle=':', marker='o', markersize=10)
in2, = plt.plot(time, MOS_RMSE, color="goldenrod", linewidth=2, linestyle='-', marker='*', markersize=10)
in3, = plt.plot(time, NWP_RMSE, color="green", linewidth=2, linestyle='--', marker='^', markersize=10)
plt.xlabel(u'Forecast lead time(h)', fontsize=20)  # 设置x轴，并设定字号大小
plt.ylabel(u'RMSE', fontsize=20)  # 设置y轴，并设定字号大小
plt.tick_params(labelsize=18)
fontdict = {"size":20,'family':'Times New Roman'}
plt.legend(handles=[in1, in2, in3,], prop=fontdict, labels=['XGBoost', 'MOS', 'NWP'], loc=2)  # 图例展示位置，数字代表第几象限
plt.savefig('折线图.png', bbox_inches='tight')
plt.show()  # 显示图像
