import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import sympy
# ------------------------------------配置区------------------------------------------------------
# 数据
L = 33
D1 = 0.02
D2 = 15.7
R0 = 47.82
# 这里的路径都是相对路径，当然你也可以写绝对路径
# 原文件
FILE_INPUT = 'res/physical.xlsx'
# 处理后的文件
FILE_OUTPUT = 'res/fucking-physical.xlsx'
# 图片保存路径
IMAGE_OUTPUT = 'res'
# ------------------------------------配置区-------------------------------------------------------

# 读入文件
physical = pd.read_excel(FILE_INPUT)


# 表格数据处理
def processTableData():
    # UI=U*I,四舍五入保留三位小数
    physical['UI'] = round(physical['U'] * physical['I'] * 1e-3, 3)
    # U/I=U/I,四舍五入保留一位小数
    physical['U/I'] = round(physical['U'] / (physical['I'] * 1e-3), 1)
    # 迭代
    for i in physical.index:
        # dQ/dt=UI-P(真空)
        if i > 0:
            physical['dQ/dt'].at[i] = physical['UI'].at[i] - \
                physical['UI'].at[0]
        # P^-1=1/P,四舍五入保留两位小数
        if i > 0:
            physical['P^-1'].at[i] = round(1 / physical['P'].at[i], 2)
        # (dQ/dt)^-1,四舍五入保留三位小数
        if i > 0:
            physical['(dQ/dt)^-1'].at[i] = round(1 /
                                                 physical['dQ/dt'].at[i], 3)
    # print(physical)
    # 导出文件
    physical.to_excel(FILE_OUTPUT, index=False)

# 其他数据处理


def processOtherData():
    fp = pd.read_excel(FILE_OUTPUT)
    # R1
    R1 = round(fp['U/I'].mean(), 2)
    print("R1:", R1)
    # t1,T1
    a = 5.1e-3
    t1 = round((R1 - R0) / (a * R0), 1)
    T1 = round(273.15 + t1, 2)
    print("t1：", t1)
    print("T1：", T1)
    # t2,T2
    t2 = round(fp['t2'].mean(), 1)
    T2 = round(273.15 + t2, 2)
    print('t2：', t2)
    print('T2：', T2)
    # 平均热导系数λ_
    y0 = 2.38e-2
    # 首先定义 `T`为一个符号，代表一个未知数
    T = sympy.Symbol('T')
    # 把函数式赋给一个变量
    f = y0 * ((T / 273.15) ** (3 / 2))
    # 传入函数表达式和积分变量、积分下限、上限
    y_ = sympy.integrate(f, (T, T2, T1)) * 1 / (T1 - T2)
    print("λ_：", round(y_, 5))
    # λ1
    y1 = gety(1, None, T1, T2)
    # 百分差Ep1
    Ep1 = (y1 - y_) / y_
    print("Ep1：", round(Ep1, 4))
    # λ2
    y2 = gety(1, 10, T1, T2)
    # 百分差Ep2
    Ep2 = (y2 - y_) / y_
    print("Ep2：", round(Ep2, 4))
    # λ3
    y3 = gety(9, 20, T1, T2)
    # 百分差Ep3
    Ep3 = (y3 - y_) / y_
    print("Ep3：", round(Ep3, 4))

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
    plt.xlabel('P^-1 (1/kPa)')
    plt.ylabel('(∆Q/∆t)^-1 (1/W)')
    # 结果保留三位小数
    plt.title(
        f'y={round(slope, 3)}x+{round(intercept, 3)}    R^2={round(r_value ** 2, 3)}',
        fontsize=16)
    plt.tight_layout()
    # plt.show()
    if stop is None:
        fileName = '0.10-1.00kPa'
    elif stop == 10:
        fileName = '0.10-0.50kPa'
    else:
        fileName = '0.50-1.00kPa'
    plt.savefig(IMAGE_OUTPUT + '/' + fileName + '.jpg')
    plt.close()

# 获取线性回归方程


def getLinregress(start, stop):
    fp = pd.read_excel(FILE_OUTPUT)
    # 获取数据
    # 0.10-1.00
    # x = fp.iloc[1:, 5]
    # y = fp.iloc[1:, 6]
    # 0.10-0.50
    # x = fp.iloc[1:10, 5]
    # y = fp.iloc[1:10, 6]
    # 0.50-1.00
    # x = fp.iloc[9:20, 5]
    # y = fp.iloc[9:20, 6]
    x = fp.iloc[start:stop, 5]
    y = fp.iloc[start:stop, 6]
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
    slope, intercept, r_value, p_value, std_err = st.linregress(x, y)
    return slope, intercept, r_value, p_value, std_err, x, y

# 获取导热系数


def gety(start, stop, T1, T2):
    # λ1
    slope, intercept, r_value, p_value, std_err, x, y = getLinregress(
        start, stop)
    y1 = (1 / (intercept * 2 * 3.1416 * L * 1e-2)) * \
         (np.log(15 / 0.02) / (T1 - T2))
    if stop is None:
        name = 'λ1：'
    elif stop == 10:
        name = 'λ2：'
    else:
        name = 'λ3：'
    print(name, round(y1, 5))
    return y1


processTableData()
processOtherData()
processGraphics(1, None)
processGraphics(1, 10)
processGraphics(9, 20)
