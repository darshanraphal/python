import cmath
a=int(input("enter the a value:\n"))
b=int(input("enter the b value:\n"))
c=int(input("enter the c value:\n"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('the solution are {0} and {1}'.format(sol1,sol2))
