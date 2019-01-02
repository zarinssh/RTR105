# -*- coding: utf-8 -*-
from numpy import sin, linspace

x = linspace(0,7,70)
y = sin(x/2)*sin(x/2)
legend = []
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("$sin(x/2)*sin(x/2)$")
plt.plot(x,y,color = "#000000"); legend.append("$sin(x/2)*sin(x/2)$")
plt.legend(legend, loc = 3)
plt.show()
