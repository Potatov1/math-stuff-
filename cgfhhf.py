a = float(input("please enter value of coefficent of x^2 "))
b = float(input("please enter value of coefficent of x "))
c = float(input("please enter value of the constant term "))

D = (b**2 - 4*a*c)

sol_1 = ( b + D**0.5)/2*a

sol_2 = ( D**0.5 - b)/2*a

print("the first soln is",sol_1)
print("the second soln is",sol_2)
