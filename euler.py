from __future__ import division
from sympy import * 
y, t, x = symbols('y t x');

def F(expr, yn, tn):
    return expr.subs([(y, yn), (t, tn)])


def euler(expr, t0, y0, h, n):     
    print ("T = " + str(t0) + "   Y = " + str(y0))
    
    yNow = y0
    tNow = t0

    for j in range(1, n):
        yNow += h*F(expr, yNow, tNow)
        tNow += h
        if(j%(0.1/h)==0):
            print ("T = " + str(tNow) + "   Y = " + str(yNow));

    return

def eulerInverso(expr, t0, y0, h, n):     
    print ("T = " + str(t0) + "   Y = " + str(y0))
    
    yNow = y0
    tNow = t0

    for j in range(1, n):
        Fn = F(expr, yNow, tNow)
        yNext = yNow + h*Fn
        tNext = tNow+h
         
        yNow += h*F(expr,  yNext, tNext)
        tNow += h
        if(j%(0.1/h)==0):
            print ("T = " + str(tNow) + "   Y = " + str(yNow));

    return

def eulerModificado(expr, t0, y0, h, n):
    print ("T = " + str(t0) + "   Y = " + str(y0))
    
    yNow = y0
    tNow = t0

    for j in range(1, n):
        Fn = F(expr, yNow, tNow)
        yNext = yNow + h*Fn
        tNext = tNow+h
        diff = (Fn + F(expr,  yNext, tNext))/2
        
        yNow += h*diff
        tNow += h
        
        if(j%(0.1/h)==0):
            print ("T = " + str(tNow) + "   Y = " + str(yNow));

    return


    return

def main():
    str_expr = input("Digite sua F(y,t):\n")
    expr = sympify(str_expr)

    t0 = float(input("Digite T0:"))
    y0 = float(input("Digite y0:"))
    h = float(input("Digite o tamanho dos passos:"))
    n = int(input("Digite o numero de passos:"))
    
    print("Valores calculados por Euler simples:\n");
    euler(expr, t0, y0, h, n)

    print("\nValores calculados por Euler inverso:\n");
    eulerInverso(expr, t0, y0, h, n)

    print("\nValores calculados por Euler modificado:\n");
    eulerModificado(expr, t0, y0, h, n)


if __name__ == "__main__":
     main()