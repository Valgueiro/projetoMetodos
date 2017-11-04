# -*- coding: utf-8 -*-
from __future__ import division
import matplotlib.pyplot as plt
from sympy import * 
y, t, x = symbols('y t x');

def F(expr, yn, tn):
    return expr.subs([(y, yn), (t, tn)])

def euler(expr, t0, y0, h, n):     #ok
    print ("T = " + str(t0) + "   Y = " + str(y0))
    
    vEulerx = []
    vEulery = []
    yNow = y0
    tNow = t0

    for j in range(1, n):
        yNow += h*F(expr, yNow, tNow)
        tNow += h
        if(j%(0.1/h)==0):
            print ("T = " + str(tNow) + "   Y = " + str(yNow));
            vx.append(tNow)
            vy.append(yNow)

    return

def eulerInverso(expr, t0, y0, h, n):     
    print ("T = " + str(t0) + "   Y = " + str(y0))
    
    yNow = y0
    tNow = t0

    for j in range(1, n):
        tNow = tNow+h
        Fop =+ yNow + h*F(expr, y, tNow) 
        fn = Eq(Fop, y)
        
        yNow = solve(fn,y).pop()

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
    tf = float(input("Digite a variável t que você deseja calcular f(t):"))
    
    #------ Apenas para testes =------
    # expr = sympify("1 - t + 4 * y");
    # t0 = 0
    # y0 = 1
    # tf = 2
    # h = 0.025    

    # n = int((tf-t0)/h) + 1
    
    print("Valores calculados por Euler simples:\n");
    euler(expr, t0, y0, h, n)

    # plt.plot(vx, vy, 'go')
    # plt.plot(vx, vy, 'k:', color='blue')
    # plt.title("Euler")
    # plt.xlabel("t")
    # plt.ylabel("y")
    # plt.show()

    print("\nValores calculados por Euler inverso:\n");
    eulerInverso(expr, t0, y0, h, n)

    print("\nValores calculados por Euler modificado:\n");
    eulerModificado(expr, t0, y0, h, n)


if __name__ == "__main__":
     main()