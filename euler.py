from __future__ import division
from sympy import * 


def euler(expr): 
    t0 = int(input("Digite o numero correspondente a T0:"))
    y0 = int(input("Digite o numero correspondente a y0:"))
    h = int(input("Digite o numero correspondente ao tamanho dos passos:"))
    n = int(input("Digite o numero correspondente ao numero de passos:"))

    for j in range(1, n):
        res = expr.subs([y, n], [t, tAux])
        print (res)
    return

def main():
    y, t, x = symbols('y t x');
    str_expr = input("Digite sua F(y,t):\n");
    expr = sympify(str_expr);
    
    res = expr.subs([(y, 1), (t, 3)]);
    print ("Para F(1,3):");
    print (res);


if __name__ == "__main__":
     main()