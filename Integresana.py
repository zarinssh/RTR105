from numpy import random, sin
from matplotlib import pyplot as plt

N = 10000

a = 0
b = 10
c = 5

x = random.uniform(a, b, N)
y = random.uniform(a, c, N)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.title('F-cija un tās integrālis')
plt.plot(x, y, 'ko')

N1 = 0

for i in range(N):
    if y[i] < sin(x[i] / 2)*sin(x[i]/2):
        plt.plot(x[i], y[i], 'go')
        N1 = N1 + 1
    else:
        plt.plot(x[i], y[i], 'ro')
        
plt.show()

S = (b - a) * (c - a)
jaunaS = float(S * N1 / N)
print("Laukuma skaitliskā vertība:", jaunaS)
