import ast

def bubble_sort(lista):
    n = len(lista)

    for i in range(n-1):              # n-1 passadas são suficientes
        for j in range(0, n-i-1):     # evita estourar o índice j+1
            if lista[j] > lista[j+1]:
              lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

entrada = input("Digite a lista: (ex: 11,4,3,8,2): ")          # o prompt some daqui, ou vira input("Digite a lista: ")
entrada = ast.literal_eval(entrada)
resultado = bubble_sort(entrada)
print(resultado)