from sympy import *
from sympy.physics.mechanics import msubs
x = symbols("x")

a = Integral(cos(x), x)
b =Eq(a, a.doit())
print("input number of variables:")
#number = int(input())
#for i in range(number):
#    print(i)
my_symbols = symbols('x0:3')
print(str(my_symbols))
experession = my_symbols[0] + 5.0*my_symbols[1] + my_symbols[2]
variables = dict()
for i in range(3):
    variables[my_symbols[i]] = i
#print(variables)
print(experession)
print(variables)
ex = experession.subs([(my_symbols[0],1),(my_symbols[1],2),(my_symbols[2],3)])
print(ex)

#answer = expression.sub

#print(number)
#print(str(b))