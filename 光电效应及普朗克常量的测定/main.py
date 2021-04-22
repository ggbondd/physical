import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.interpolate import make_interp_spline  # 散点图的光滑曲线
import numpy as np
import sympy
# ------------------------------------配置区------------------------------------------------------
# 这里的路径都是相对路径，当然你也可以写绝对路径
# 原文件
FILE_INPUT = 'res/physical.xlsx'
# 图片保存路径
IMAGE_OUTPUT = 'res'
# ------------------------------------配置区-------------------------------------------------------
# 读入文件
physical = pd.read_excel(FILE_INPUT)

# 图像处理


def processGraphics(start, stop, name):
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差,x,y
    slope, intercept, r_value, p_value, std_err, x, y = getLinregress(
        start, stop)
    # 散点图
    plt.scatter(x, y, color='green')
    plt.plot(x, y)
    plt.vlines(0, 0, 0.5, colors="c", linestyles="dashed")

    plt.xlabel('I (10^-11A)')
    plt.ylabel('V (U)')

    # 获取图像中当y=0时，x的值z
    def getx(x1, y1, x2, y2, y):
        return (y - y1) * (x2 - x1) / (y2 - y1) + x1
    for i in range(1, len(x)):
        x1 = x[i - 1]
        y1 = y[i - 1]
        x2 = x[i]
        y2 = y[i]
        if y1 * y2 <= 0 and y1 != 0:
            x0 = getx(x1, y1, x2, y2, 0)
            z = round(x0, 2)
    # print(z)

    # 结果保留三位小数
    plt.title(name + "    " + f"U={z}",
              fontsize=16)
    plt.tight_layout()
    # plt.show()
    plt.savefig(IMAGE_OUTPUT + '/' + name + '.jpg')
    plt.close()


# 获取线性回归方程


def getLinregress(start, stop):
    fp = pd.read_excel(FILE_INPUT)
    x = fp.iloc[0:None, start]
    y = fp.iloc[0:None, stop]
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
    slope, intercept, r_value, p_value, std_err = st.linregress(x, y)
    return slope, intercept, r_value, p_value, std_err, x, y

# processGraphics(0, 1,"365nm")
# processGraphics(2, 3,"405nm")
# processGraphics(4, 5,"436nm")
# processGraphics(6, 7,"546nm")
# processGraphics(8, 9,"577nm")
