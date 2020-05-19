# -*- coding: utf-8 -*-
"""
step03_multi_line.py

marker, color, line style, label
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot") # 차트 격자 제공

# data 생성
data1 = 0.5 + 0.1 * np.random.randn(100) # mean = 0, standard deviation = 1
data2 = 0.7 + 0.2 * np.random.randn(100)
data3 = 0.9 + 0.1 * np.random.randn(100)
data4 = 0.3 + 0.3 * np.random.randn(100)

fig = plt.figure(figsize = (12, 5)) # figsize = tuple
chart = fig.add_subplot()

chart.plot(data1, marker = "o", color = "blue", linestyle = "-", label ="data1")
chart.plot(data2, marker = "+", color = "red", linestyle = "--", label ="data2")
chart.plot(data3, marker = "*", color = "green", linestyle = "-.", label ="data3")
chart.plot(data4, marker = "s", color = "hotpink", linestyle = ":", label ="data4")
chart.set_title("Multi-line chart")
chart.set_xlabel("색인")
chart.set_ylabel("random number")
plt.legend(loc = "best")
plt.show()















































