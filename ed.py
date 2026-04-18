import matplotlib.pyplot as plt 
import numpy as np
base= int(input("value of base constant "))
a = int(input("low limit of exponential value "))
b = int(input("high limit of exponential value  "))

c=[]
y=[]
for i in range (a,b):
    c.append(i)
for o in c:
    ex_val=(base**o)
    y.append(ex_val)

plt.plot(c, y)

plt.xlabel("x")
plt.ylabel("2^x")
plt.title("Exponential Function")
plt.grid()



plt.show()


c = np.linspace(a, b, 100)
y = base**c


plt.plot(c, y)

plt.xlabel("x")
plt.ylabel("base^x")
plt.title("Exponential Function")
plt.grid()



plt.show()
