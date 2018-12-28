# -*- coding: utf-8 -*-
from numpy import sin, linspace
def f1(x):
    return x
def f2(x):
    return f1(x) - x**3/(1*2*3)
def f3(x):
    return f2(x) + x**5/(1*2*3*4*5)
def f4(x):
    return f3(x) - x**7/(1*2*3*4*5*6*7)
x = linspace(0,4,41)
y = sin(x/2)*sin(x/2); y1 = f1(x); y2 = f2(x); y3 = f3(x); y4 = f4(x)
legend = []
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("$sin(x)$ funkcija un tās izvirzījumi rindā")
plt.plot(x,y,color = "#000000"); legend.append("$sin(x)$")
plt.plot(x,y1,color = "#FF0000"); legend.append("$x$")
plt.plot(x,y2,color = "#00FF00"); legend.append("$x - x^3/3!$")
plt.plot(x,y3,color = "#0000FF"); legend.append("$x - x^3/3! + x^5/5!$")
plt.plot(x,y4,color = "#FFFF00"); legend.append("$x - x^3/3! + x^5/5! - x^7/7!$")
plt.legend(legend, loc = 3)
plt.show()
