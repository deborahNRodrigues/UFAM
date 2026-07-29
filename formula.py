"""    Qual o valor da fórmula?

    Escreva um programa que leia três variáveis reais a, b, c, nesta ordem.

    Como saída, o programa deve imprimir o resultado da seguinte fórmula matemática:

    a+b+ca2+b2+c2​
    Arredonde os resultados com 07 casas decimais. 

        Primeiro leia as variáveis, depois aplique a fórmula e, por fim, imprima o resultado.
        Considere que a soma a + b + c nunca será igual a zero, ou seja, não terá divisão por zero
        Dentro do comando print, use o comando round(x, n) para arredondar a resposta x com até n casas decimais.
    Caso de Teste 1
    Entrada	

    100
    50
    0

    Saída	

    83.3333333

    Caso de Teste 2
    Entrada	

    -1.0
    -2.0
    -5.0

    Saída	

    -3.75

    Caso de Teste 3
    Entrada	

    1.0
    2.0
    3.0

    Saída	

    2.3333333

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
⌄
⌄
a = 0
b = 0
c = 0

def funcao(a,b,c):
  soma = a + b + c
if (soma != 0):
  resultado = (a * a + b * b + c * c) / soma
return resultado
 


a = (int(input("Informe o valor de a :")))
b = (int(input("Informe o valor de b : ")))
c = (int(input("Informe o valor de C :")))
print(funcao(round(a,b,c)))
  
  
  git"""