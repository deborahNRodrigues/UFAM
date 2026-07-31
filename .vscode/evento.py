"""Evento europeu
Objetivo: Contar a quantidade de pessoas de cada país.

Em um congresso europeu, levantaram o país de origem das pessoas ali presentes. Essas informações foram armazenadas em uma string, onde os países de cada pessoa são separados por vírgulas.

Escreva um programa que leia essa string. Como saída, determine:

A maior quantidade de pessoas do mesmo país.
Um vetor contendo a quantidade de pessoas de cada país, nesta ordem: BE,ES,FR,IT,PT.
Os países são representados pelas seguintes siglas:

BE – Bélgica
ES – Espanha
FR – França
IT – Itália
PT – Portugal
Use o método .split(',') para transformar a string de entrada em vetor, usando o argumento (neste exemplo, a vírgula) como critério de separação dos elementos.
Durante a leitura, use o método .upper() para converter todas as letras em MAIÚSCULAS.
Utilize um vetor de contagem para guardar a quantidade de pessoas de cada um dos países.
Exemplos adicionais (não exaustivos):

Entrada: ES,BE,ES,PT,ES

Saída:

3

[1 3 0 0 1]"""

def contador_pais(pais):
 pais = pais.upper()
 vetor = []
 vetor = pais.split(",")
 contagem = [0,0,0,0,0]

 for i in range(len(vetor)):
  if vetor[i] == "BE":
   contagem[0]+=1
   
  elif vetor[i] == "ES":
   contagem[1]+=1
  
  if vetor[i] == "FR":
     contagem[2]+=1
    
  elif vetor[i] == "IT":
     contagem[3]+=1
    
  elif vetor[i] == "PT":
     contagem[4]+=1

 return contagem

entrada = ("ES,BE,ES,PT,ES")
resultado = contador_pais(entrada)
maior = max(resultado)
print(maior)
print(resultado)