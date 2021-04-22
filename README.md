# Intro

经常百度的我们会发现，物理实验报告的处理是大同小异的，那么是否可以使用简单的程序来解决重复的复杂计算？这正是本repository的初衷

# Environment

python版本：Python 3.8.7

开发工具：pycharm

用到的模块：

```
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import sympy
```

> pandas：数据分析
>
> numpy：数学运算
>
> matplotlib：画图板
>
> scipy：线性回归计算
>
> sympy：积分运算

# Projects

## [1. 气体热导率的测量](https://github.com/ggbondd/fucking-physical/tree/main/%E6%B0%94%E4%BD%93%E7%83%AD%E5%AF%BC%E7%8E%87%E7%9A%84%E6%B5%8B%E9%87%8F)

运行前

1. 修改`res`目录下`physical.xlsx`中的初始数据
2. 修改代码配置区信息（实验参数及一些路径配置）

运行后

1. 数据处理后的表格及相关图片会出现在运行前配置区的目录中
2. 实验要求的其他数据会打印出来

------

## [2. **光电效应及普朗克常量的测定**](https://github.com/ggbondd/physical/tree/main/%E5%85%89%E7%94%B5%E6%95%88%E5%BA%94%E5%8F%8A%E6%99%AE%E6%9C%97%E5%85%8B%E5%B8%B8%E9%87%8F%E7%9A%84%E6%B5%8B%E5%AE%9A)

