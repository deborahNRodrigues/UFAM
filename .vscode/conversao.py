"""Conversão de Números Decimais para Binários

Carlos está estudando sistemas de numeração e deseja criar um programa que converta de números decimais para binários. Ele acredita que essa habilidade será útil em seu próximo projeto. Ajude Carlos a criar um programa que faça essa conversão. A representação binária de um número consiste em uma sequência de dígitos binários (0's e 1's) que representam o número em base 2.

Considere apenas números inteiros positivos.

Instruções

Divida o número decimal pela base 2 e registre o resto dessa divisão.
Divida o resultado da etapa anterior novamente por 2 e registre o resto.
Continue dividindo o resultado das divisões anteriores por 2 até que o resultado seja zero.
Os restos obtidos nas divisões formam a representação binária do número decimal. 
Lembre-se de ler os restos de baixo para cima.
Entrada:

O programa deve solicitar ao usuário que insira um decimal inteiro.

Saída:

O programa deve imprimir a representação binária do número decimal inserido pelo usuário.

Use um loop while para realizar a conversão até que o número decimal seja zero.
Você pode criar uma string para armazenar os restos e concatená-los enquanto os calcula.
No caso do número 0 a saída deve ser 0.
Caso de Teste 1
Entrada	
10
Saída	
1010
Caso de Teste 2
Entrada	
90
Saída	
1011010
Caso de Teste 3
Entrada	
20
Saída	
10100"""



def conversao_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero != 0:
        resto = numero % 2
        binario = str(resto) + binario   # concatena no início
        numero = numero // 2             # atualiza o número (divisão inteira)
    
    return binario


user = input("Informe um número para a conversão: ")
numero = int(user)
print(conversao_binario(numero))