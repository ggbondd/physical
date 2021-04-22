import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import sympy
# ------------------------------------配置区------------------------------------------------------

# 这里的路径都是相对路径，当然你也可以写绝对路径
# 原文件
FILE_INPUT = 'res/data.xlsx'
# 图片保存路径
IMAGE_OUTPUT = 'res'
# ------------------------------------配置区-------------------------------------------------------

# 读入文件
physical = pd.read_excel(FILE_INPUT)


# 图像处理


def processGraphics(start, stop):
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差,x,y
    slope, intercept, r_value, p_value, std_err, x, y = getLinregress(
        start, stop)
    # 散点图
    plt.scatter(x, y, color='green')
    # 期望函数
    exp = x * slope + intercept
    # 画出回归直线
    plt.plot(x, exp, color='orange')
    plt.xlabel('10^14HZ')
    plt.ylabel('U')
    # 结果保留三位小数
    plt.title(
        f'y={round(slope, 3)}x+{round(intercept, 3)}    R^2={round(r_value ** 2, 3)}',
        fontsize=16)
    plt.tight_layout()
    # plt.show()
    plt.savefig(IMAGE_OUTPUT + '/data.jpg')
    plt.close()

# 获取线性回归方程


def getLinregress(start, stop):
    fp = pd.read_excel(FILE_INPUT)
    x = fp.iloc[start:stop, 0]
    y = fp.iloc[start:stop, 1]
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
    slope, intercept, r_value, p_value, std_err = st.linregress(x, y)
    return slope, intercept, r_value, p_value, std_err, x, y


processGraphics(0, None)
