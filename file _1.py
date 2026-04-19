import matplotlib.pyplot as plt
import cmath
a = float(input("please enter value of coefficent of x^2 "))
b = float(input("please enter value of coefficent of x "))
c = float(input("please enter value of the constant term "))

D = (b**2 - 4*a*c)



sol_1 = (-b + cmath.sqrt(D)) / (2*a)  #using cmath to handle exeception cases
sol_2 = (-b - cmath.sqrt(D)) / (2*a)


print("the first soln is",sol_1)
print("the second soln is",sol_2)
t = []

z=[]

for i in range(-100,101):
    u = a*i**2 + b*i + c
    z.append(u)
    t.append(i)
plt.grid()
plt.plot(t,z)
plt.show()



