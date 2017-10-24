from __future__ import division
from sympy import * 
y, t, x = symbols('y t x');

def euler(expr): 
    t0 = float(input("Digite T0:"))
    y0 = float(input("Digite y0:"))
    h = float(input("Digite o tamanho dos passos:"))
    n = int(input("Digite o numero de passos:"))
    print ("T = " + str(t0) + "   F(y,t) = " + str(y0))
    
    yNow = y0
    tNow = t0

    for j in range(1, n):
        derivate = expr.subs([(y, yNow), (t, tNow)])
        yNow += h*derivate
        tNow += h
        if(j%(0.1/h)==0):
            print ("T = " + str(tNow) + "   Y = " + str(yNow));

    #print("Final value to y(t)")
    return

def main():
    str_expr = input("Digite sua F(y,t):\n")
    expr = sympify(str_expr)
    euler(expr)


if __name__ == "__main__":
     main()