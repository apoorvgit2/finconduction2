from cmath import cosh, e
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from matplotlib.pyplot import subplot, figure
print ("1-Infinitely long fin")
print ("2-Insulated fin tip")
print ("3-Convective heat loss from tip")
print ("4-Prescribed temperature at tip")
x=np.linspace(0,0.03,1000)
x3=np.linspace(0,1,1000)
x1=np.linspace(0,0.03,1000)
k=370
h=10
m=2.32495278
L=0.03
p=0.008
a=0.00004
THb=45
f4=THb*((((k*m)-h)*(e**(m*(x-L))))+(((k*m)+h)*e**(m*(L-x))))/((h*(e**(m*L)-e**(-m*L)))+(k*m*(e**(m*L)+e**(-m*L))))
f3=THb*(e**(-m*x3))
f2= THb*(((e**(m*(L-x)))+(e**(-m*(L-x))))/((e**(m*(L)))+(e**(-m*(L)))))
n=random.randint((26+273),(69+273))-298
f1=THb*((((n/THb)*((e**(m*x1))-(e**(-m*x1))))+(e**(m*(L-x1)))-(e**(-m*(L-x1))))/((e**(m*(L)))-(e**(-m*(L)))))
figure(1)
subplot(2,2,1)
plt.plot(x1,f1)
plt.title("Prescribed temperature at tip", loc = "left")
plt.xlabel("Length of fin", loc = "right")
plt.ylabel("Temperature")
subplot(2,2,2)
plt.plot(x,f2)
plt.title("Insulated fin tip", loc = "left")
plt.xlabel("Length of fin", loc = "right")
plt.ylabel("Temperature")
subplot(2,2,3)
plt.plot(x3,f3)
plt.title("Infinitely long fin", loc = "left")
plt.xlabel("Length of fin", loc = "right")
plt.ylabel("Temperature")
subplot(2,2,4)
plt.plot(x,f4)
plt.title("Convective heat loss from tip", loc = "left")
plt.xlabel("Length of fin", loc = "right")
plt.ylabel("Temperature")
plt.show()

