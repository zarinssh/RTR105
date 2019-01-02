from math import sin, fabs
from time import sleep

def f(x):
    return sin(x/2)*sin(x/2)

#Definejam argumenta x robezhas:
a = 0
b = 10

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dotajaa intervaalaa ir saknes:
if (funa * funb > 0.0):
    print ("Dotajaa intervala [%s, %s] saknju nav"% (a,b))
    sleep(1); exit()  #zinjo uz ekraana 1 sec
else:
    print ("dotajaa intervaalaa sakne(s) ir!")

# Defineejam  precizitaati , ar kaadu mekleesim sakni :
deltax = 0.01

# Sashaurinam saknes mekleeshanas robezhas:
while ( fabs(b-a) > deltax ) :
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0.) :
        b = x
    else :
        a = x
print ("Sakne ir: ", x)
