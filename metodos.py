# -*- coding: utf-8 -*-
from __future__ import division
import matplotlib as plt
from sympy import * 
y, t, x, g = symbols('y t x g');

vx = []
vy = []

calculatedF = []

def F(expr, yn, tn):
    return expr.subs([(y, yn), (t, tn)])


def FAdamsBash(expr, i, grau):#formulas e mais formulas
    if(grau==2):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        return (h/2)*(3*F0-F1) 
    elif(grau==3):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        return ((h/12)*(23*F0-16*F1+5*F3))  
    elif(grau==4):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        F3 = F(expr, calculatedF[i-3][0], calculatedF[i-3][1])
        return ((h/24)*(55*F0-59*F1+37*F2-9*F3)) 
    elif(grau==5):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        F3 = F(expr, calculatedF[i-3][0], calculatedF[i-3][1])
        F4 = F(expr, calculatedF[i-4][0], calculatedF[i-4][1])
        return ((h/720)*(1901*F0-2774*F1+2616*F2-1274*F3+251*F4)) 
    elif(grau==6):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        F3 = F(expr, calculatedF[i-3][0], calculatedF[i-3][1])
        F4 = F(expr, calculatedF[i-4][0], calculatedF[i-4][1])
        F5 = F(expr, calculatedF[i-5][0], calculatedF[i-5][1])
        return (h/1440)*(4277*F0-7923*F1+9982*F2-7298*F3+2877*F4-475*F5) #calcula o yn   

def FAdamsMoulton(expr, i, grau):#formulas e mais formulas
    if(grau==2):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        return (h/2)*(F0+F1) 
    elif(grau==3):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        return ((h/12)*(5*F0+8*F1-F3))  
    elif(grau==4):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        F3 = F(expr, calculatedF[i-3][0], calculatedF[i-3][1])
        return ((h/24)*(9*F0+19*F1-5*F2+F3)) 
    elif(grau==5):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        F3 = F(expr, calculatedF[i-3][0], calculatedF[i-3][1])
        F4 = F(expr, calculatedF[i-4][0], calculatedF[i-4][1])
        return ((h/720)*(251*F0+646*F1-264*F2+106*F3-19*F4)) 
    elif(grau==6):
        F0 = F(expr, calculatedF[i][0], calculatedF[i][1])
        F1 = F(expr, calculatedF[i-1][0], calculatedF[i-1][1])
        F2 = F(expr, calculatedF[i-2][0], calculatedF[i-2][1])
        F3 = F(expr, calculatedF[i-3][0], calculatedF[i-3][1])
        F4 = F(expr, calculatedF[i-4][0], calculatedF[i-4][1])
        F5 = F(expr, calculatedF[i-5][0], calculatedF[i-5][1])
        return (h/1440)*(475*F0+1427*F1-798*F2+482*F3-173*F4+27*F5) #calcula o yn   

def euler(expr, t0, y0, h, n):
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

def rk(expr, t0, y0, h, n, fromAdams):
    print ("T = " + str(t0) + "   Y = " + str(y0))
    
    yNow = y0
    tNow = t0
    calculatedF.append((0, 0)) 
    
    for j in range(1, n):
        half = 0.5 * h
        k1 = F(expr, yNow, tNow);
        k2 = F(expr, yNow + half * k1, tNow + half)
        k3 = F(expr, yNow + half * k2, tNow + half)
        k4 = F(expr, yNow + h * k3, tNow + h)

        Ftotal = (h * ((k1 + (2 * k2) + (2 * k3) + k4)/6))
        yNow = yNow + Ftotal
        tNow = tNow+h

        if(fromAdams):
            calculatedF.append((yNow, tNow))
                 
        if(j%(0.1/h)==0):
            print ("T = " + str(tNow) + "   Y = " + str(yNow));

    print(calculatedF)
    print(calculatedF[1][0])
    return

def adamsBashforth(expr, t0, y0, h, n, grau):

    print ("T = " + str(t0) + "   Y = " + str(y0));
    
    rk(expr, t0, y0, h, grau-1, 1) # Utilizamos rk pra calcular o valor dos f's 
    tNow=t0+(grau-1)*h
    print(calculatedF)
    for i in range (grau-1, n):
        yNow = calculatedF[i][0] + FAdamsBash(expr, i, grau)
        tNow = tNow + h 
        print ("T = " + str(tNow) + "   Y = " + str(yNow));     
    return

def adamsMoulton(expr, t0, y0, h, n, grau):
    print ("T = " + str(t0) + "   Y = " + str(y0));
    
    rk(expr, t0, y0, h, grau-2, 1) # Utilizamos rk pra calcular o valor dos f's 
    tNow=t0+(grau-2)*h

    for i in range (o-2, n):
        yNow = calculatedF[i][0] + FAdamsMoulton(expr, i, grau)  
        tNow = tNow + h 
        print ("T = " + str(tNow) + "   Y = " + str(yNow));           
    return    

def main():
    # str_expr = input("Digite sua expressao:\n")
    # expr = lambdify((t,y), solve(sympify(str_expr), g).pop());
    # print(str(expr))

    
    # print("Digite o metodo que você deseja calcular:")
    # print("1 - Euler Simples")
    # print("2 - Euler Inverso")
    # print("3 - Euler Modificado")
    # print("4 - Runge-Kutta")
    # method = int(input("Sua escolha:"))


    # str_expr = input("Digite sua expressao:\n")
    # expr = sympify(str_expr)
    # t0 = float(input("Digite T0:"))
    # y0 = float(input("Digite y0:"))
    # h = float(input("Digite o tamanho dos passos:"))
    # tf = float(input("Digite a variável t que você deseja calcular f(t):"))
    
    #------ Apenas para testes =------
    expr = sympify("1 - t + 4 * y");
    t0 = 0
    y0 = 1
    tf = 2
    h = 0.05   
    method = 5;

    n = int((tf-t0)/h) + 1
    
    if (method == 1):
        print("Valores calculados por Euler simples:\n");
        euler(expr, t0, y0, h, n)
        #plt.title("Euler Simples")
    elif (method == 2):
        print("\nValores calculados por Euler inverso:\n");
        eulerInverso(expr, t0, y0, h, n)
       # plt.title("Euler Inverso")
    elif (method == 3):
        print("\nValores calculados por Euler modificado:\n");
        eulerModificado(expr, t0, y0, h, n)
        #plt.title("Euler Modificado")
    elif (method == 4):
        print("\nValores calculados por Runge-Kutta:\n");
        rk(expr, t0, y0, h, n, 0)
        #plt.title("Runge-Kutta")
    elif (method == 5):
        #grau = int(input("Digite o grau:\n"))
        grau = 4;
        print("\nValores calculados por Adams-Bashforth:\n");
        adamsBashforth(expr, t0, y0, h, n, grau)
        #plt.title("Adams-Bashforth")
    elif (method == 6):
        grau = int(input("Digite o grau:\n"))
        print("\nValores calculados por Adams-Moulton:\n");
        adamsMoulton(expr, t0, y0, h, n, grau)
        #plt.title("Adams-Moulton") 
        
    # plt.plot(vx, vy, 'go')
    # plt.plot(vx, vy, 'k:', color='blue')
    # 
    # plt.xlabel("t")
    # plt.ylabel("y")
    # plt.show()
    

if __name__ == "__main__":
     main()