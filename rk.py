import matplotlib.pyplot as plt
from sympy import * 
t, y, h = symbols('t y h')


def f(t, y): return 1 - t + 4 * y
def ka(t, y): return f(t, y)
def kb(t, y, h): return f(t + 0.5 * h, y + 0.5 * h * ka(t, y)  )
def kc(t, y, h): return f(t + 0.5 * h , y + 0.5 * h * kb(t, y, h) )
def kd(t, y, h): return f(t + h ,y + h * kc(t, y, h))
def rungekutta(t, y, h): return y + ((h/6) * (ka(t, y) + (2 * kb(t, y, h)) + (2* kc(t, y, h)) + kd(t, y, h)))

def main():
    i = 1
    vx = []
    vy = []
    tn = float(input("Digite o numero correspondente a T0:"))
    yn = float(input("Digite o numero correspondente a y0:"))
    p = float(input("Digite o numero correspondente ao tamanho dos passos:"))
    n = int(input("Digite o numero correspondente ao numero de passos:"))
    for i in range (1, n):
       print ("tn:")
       vx.append(tn)
       print (tn) 
       print (" yn: ") 
       print (yn) 
       vy.append(yn)
       print ("\n") 
       yn = rungekutta(tn, yn, p)
       tn = tn + p
       i = i + 1
    plt.plot(vx, vy, 'go')
    plt.plot(vx, vy, 'k:', color='blue')
    plt.title("Runge-Kutta")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.show()





#defina f(t,y)
#Passo 2. alimente os valores iniciais t0 e y0
#Passo 3. alimente o tamanho do passo h e o numero de passos n
# Passo 4. escreva tO e y0
# Passo 5. para j de 1 ate n calcule
# Passo 6. k1 = f(t,y)
# k2 = f(t + 0.5 * h,y + 0,5 * h * kl)
# k3 = f(t + 0.5 * h,y + 0,5 *h * k2)
# k4 = f(t + h,y + h * k3)
# y = y + (h/6)* (kl + 2* k2 +2* k3 + k4)
# t=t+h

if __name__ == "__main__":
     main()