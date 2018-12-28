

def mana_funkcija(x):
    return sin(x/2)*sin(x/2)



from numpy import sin, linspace
from matplotlib import pyplot as plt

x = linspace(0,4,11)

y = mana_funkcija(x)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.title('Funkcija un taas atvasinaajumi')
plt.plot(x,y)
plt.plot(x,y,'ro')



N = len(x)
delta_x = x[1] - x[0]
derivative = []

for i in range(N):
    temp = (mana_funkcija(x[i] + delta_x) - mana_funkcija(x[i])) / delta_x
    derivative.append(temp)
    
    
plt.plot(x,derivative)
plt.plot(x,derivative,'go')
legend = []

legend.append('fn ar starpvertibam')
legend.append('fn dazas vertibas')
legend.append('atvasinaajums ar starpvertibam')
legend.append('atvasinaajuma dazas veertibas')




derivative_trough_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_trough_array.append(temp)

plt.plot(x[0:N-1],derivative_trough_array)
plt.plot(x[0:N-1],derivative_trough_array,'bo')

legend.append('atvasinaajums ar starpveertiibaam (masivs)')
legend.append('atvasinaajuma dazhas veertibas (masivs)')


plt.legend(legend, loc=3)
plt.show()
