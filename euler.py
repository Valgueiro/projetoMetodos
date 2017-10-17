from sympy import * 
def euler(f): 
    t0 = int(input("Digite o numero correspondente a T0:"))
    y0 = int(input("Digite o numero correspondente a y0:"))
    h = int(input("Digite o numero correspondente ao tamanho dos passos:"))
    n = int(input("Digite o numero correspondente ao numero de passos:"))

    for j in range(1, n):
        print ("We're on time %d" % (j))
        #y = f(j)    
        #print (y + '\n')
    return

def main():
    # f = lambda x: eval(input())
    euler(5)


#defina f(t,y)
#Passo 2. alimente os valores iniciais 10 e y0
#Passo 3. alimente o tamanho do passo h e o ntImero de passos n
# Passo 4. escreva tO e y0
# Passo 5. para j de 1 ate n calcule
# Passo 6. k 1 = f (t,y)
# y=y+h*kl
# t =t +h
# Pass() 7. escreva*/

if __name__ == "__main__":
     main()