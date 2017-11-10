# ProjetoMetodos
Todas as aplicações dos Métodos Númericos feitos por Mateus Valgueiro (mvt@cin.ufpe.br) utilizando Python

## Informações Gerais
Essas instruções irão ajudar em como compilar e executar o código presente neste repositório.

### Dependências
Para rodar este programa você deve estar em um ambiente ***Linux*** e com a biblioteca [Simpy](http://docs.sympy.org/latest/install.html) e [MatplotLib](https://matplotlib.org/users/installing.html) instaladas em sua máquina.

### Executando o código
Assim, quando quiser executá-lo, com todas as dependências devidamente instaladas, você deve rodar o comando: 
```
$ python3 metodos.py
```


## Como o programa Funciona

### Escolhendo o Método que será utilizado
Assim que rodamos o programa, nos deparamos com este menu em nossa tela:

```
Digite o metodo que você deseja calcular:                                                           
1 - Euler Simples                                                                                  
2 - Euler Inverso                                 
3 - Euler Modificado               
4 - Runge-Kutta     
5 - Adams-Bashforth
6 - Adams-Moulton                               
Sua escolha:  
```

Onde aqui escolheremos qual dos métodos disponíveis utilizaremos.

### Enviando os parâmetros necessários
Logo após a escolha do método, devemos informar ao programa os devidos valores dos parâmetros necessários, como a própria função *dF(y,t)/dt*, *t0*, *Y(t0)*, *h*(o tamanho dos passos) e *tf*, que seram utilizados para achar o valor no qual queremos calcular, isto é, ***Y(tf)*** .

### Recebendo os resultados
Após todo cáculo feito pelo programa, recebemos os *valores calculados em todo o intervalo*, bem como nossa ***Y(tf)*** e um *gráfico* que surge em nossa tela, onde plotamos todas as informações obtidas no programa e vemos como se comporta a função *Y(t)* baseada nos parâmetros passados pelo usuário e pelo método escolhido pelo mesmo.
