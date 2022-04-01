from argparse import ArgumentError
from tokenize import Double
from sympy import *
from sympy.physics.mechanics import msubs
from matplotlib import use
import re
import itertools
import functools

table = [[2,3,1,0,0,0],[2,1,0,1,0,0],[0,3,0,0,1,0],[3,0,0,0,0,1]]
b_tmp = [19.0,13.0,15.0,18.0]
c = [-7,-5,0,0,0,0]
s =  symbols(f'x0:{len(c)}')
v = [0,1,3,5]

def functional():
    expr = 0
    for i in range(len(c)):
        expr = expr + c[i] * s[i]
    return expr

#func = functional(c)

def canonical_form_another_variable(m,b,variables):
    pass


def symplex_method(m,b, start_variables, func):
    var = start_variables
    m,b = change_variables(m,b,start_variables)


def symplex_table(m,b,variables,func):
    
    variables = sorted(variables)
    (m,b) = change_variables(m,b,variables)
    str = "basis "
    for i in range(0,len(m[0])):
        str = str + f' x_{i}'
    
    
    print(str + " _")
    for var in variables:
        str = f'x_{var}'
        for i in range(0, len(m[0])):
            str = str + " " +  f'{m[var][i]}'
        print(str)
        

def change_variables(m,b,variables,func):
    variables = sorted(variables)
    prev = []
    for var in variables:
      #  print(prev)
        not_zero = 0
        for i in range(0,len(m)):
            if(m[i][var] != 0 and (i not in prev)):
                not_zero = i
                break
      #  print(not_zero)
        b[not_zero] = b[not_zero]/m[not_zero][var]
        m[not_zero] = list(map(lambda x:x/m[not_zero][var], m[not_zero]))
        
     #   print(b[not_zero])
        for i in range(0, len(m)):
            if(i!= not_zero):
                tmp_not_zero = list(map(lambda x: x*m[i][var], m[not_zero]))
                tmp = zip(m[i],tmp_not_zero)
                tmp1 = [x - y for (x,y) in tmp]
                m_tmp = m[i]
                m[i] = tmp1
                b[i] = b[i] - b[not_zero]*m_tmp[var]
            #    print(b[i])
            else:
                pass
        prev.append(not_zero)
    
      #  show(m)
      #  print("")
    tmp2 = list(range(0,len(m[0])))
    tmp_map = list(map(lambda x: (s[x],), variables))
    substraction = [x for x in tmp2 if x not in variables]
    my_subs = []
    for i in range(len(variables)):
        tmp_expr = b[i]
        for j in substraction:
            tmp_expr = tmp_expr - m[i][j]*s[j]
        my_subs.append((s[variables[i]], tmp_expr))
    print(my_subs)
    #func = func.subs([(s[])])
    func = func.subs(my_subs)

    return (m,b,variables,func)
        

def show(m):
    for row in m:
        print(row)
#t = [[1,2,3,4],[1,5,7,2],[2,2,1,11],[2,3,3,4]]


my_str = str(change_variables(table,b_tmp,v,  functional())[3])
my_str = my_str.replace(" ", "")
#my_str = my_str.split("*")
print(my_str)
varbl = re.findall("x\d*",my_str)
asd = []
for varbl_ in varbl:
    #print(re.findall(re.compile("\+?\-?(\d+).(\d+)"+varbl_),my_str))
    asd_tmp = re.findall(re.compile("\-?\+?\d+.\d+\*"+varbl_),my_str)
    
    asd_tmp2 = asd_tmp[0].split("*")
    asd.append((asd_tmp2[1],asd_tmp2[0]))
    my_str = my_str.replace(asd_tmp[0],"")

  #  asd.append((varbl,asd_tmp[0].split("*")[0]))
asd.append(("free", my_str))
print(asd)
#print(varbl)
#print()

#tmp2 = list(range(0,len(table[0])))
#substraction = [x for x in tmp2 if x not in [0,1,4,5]]
#print(substraction)
#show(standard_form_to_canonical(t,[0,1,2,3],[3,0,1]))
#symplex_table(t,[1,2,3,4],[0,1,2])
#standard_form_to_canonical(t,[0,1,2],[0,1])
#functional1 = input()
#coef =  list(map(lambda x: float(x),list(functional1.split(" "))))
#print(coef)



#x0,x1, x2 = symbols("x0 x1 x2")


#show(change_variables(table,b_tmp,[0,1,4,5])[1])

#print(functional(coef))
