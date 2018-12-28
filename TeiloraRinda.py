import math

def sinus_kvadrata(x):
    summa = 0
    for k in range (1, 500):
        a = (((-1)**(k+1))*x**(2*k))/(2*math.factorial(2*k))
        summa = summa + a
    return summa

x = int(input("Ievadi argumenta vertibu: "))

y = math.sin(x/2)*math.sin(x/2)
          
mansy = sinus_kvadrata(x)

print(y)
print(mansy)
