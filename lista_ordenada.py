"""Você está desenvolvendo um sistema de chamada para uma escola.
Agora, sua missão é: Criar uma lista ordenada de alunos.
Implementar uma busca eficiente para encontrar um aluno rapidamente. 
Comparar o tempo de execução da busca lenta e da busca rápida."""

lista = ["Carlos", "Ana", "Bruno", "Diana", "Eduardo"]
import bisect
def busca_alunos(nome,lista):
    lista.sort()
    index = bisect.bisect_left(lista, nome)
    if index <len(lista) and lista[index] == nome:
        return f"{nome} encontrado.!"
    return f"{nome} não está na lista.!"
print(busca_alunos("Carlos", lista))