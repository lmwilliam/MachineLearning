# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:58:59 2020

@author: WilliamLiang
"""

import matplotlib.pyplot as plt
import numpy as np

# Show Chinese in your plot
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus']=False

# In[1] plot 1

# Grammar：plot(X axis, Y axis, format)
plt.plot([5,10,15,20],[2,4,6,8],"rH")
# format:
# color            markers styles
# r for red        o for cicle marker
# g for green      s for square
# b for blue       h/H for hexagon
# y for yellow     p for pentagon
# c for cyan       x for x marker
# m for magenta    D for diamond 
# k for black      * for star
# w for white      ^/v/>/< for triangle 

# More: https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.plot.html
plt.show()

# In[2] plot 2

X = np.arange(0., 5., 0.2)

plt.title("X, X square, X cubic plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.plot(X, X, "r--",label="X")
plt.plot(X, X**2, "bs",label="X 平方")
plt.plot(X, X**3, "g^", label="X cubic")
plt.legend(loc='best')

plt.show()

# In[3] bar

xAxis = ["Apple","Samsung","OPPO","Huawei"]
yAxis = [24.1, 23.3, 9.2, 8.9]

plt.title("Taiwanese mobile phone market share")
plt.xlabel("Brand")
plt.ylabel("Percent")

plt.bar(xAxis,yAxis)
plt.show()

# In[4] scatter

# Size of Sample Data
n = 150

# Group1 Data around (-1, 2) as Normal Distribution
X1 = np.random.normal(-1, 1, n)
Y1 = np.random.normal(2, 1, n)

# Group2 Data around (2, 1) as Normal Distribution
X2 = np.random.normal(2, 1, n)
Y2 = np.random.normal(-1, 1, n)

# Scatter Chart with Size(s), color(c), Style(marker) of marker
plt.scatter(X1, Y1, s=75, c="red", marker="+")
plt.scatter(X2, Y2, s=75, c="blue", marker="o")
plt.show()
