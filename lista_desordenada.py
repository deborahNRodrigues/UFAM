
alunos = ["Carlos", "Ana", "Bruno", "Diana", "Eduardo"]
def busca_lenta(nome, lista):
     for aluno in lista:
         if aluno == nome: 
            return f"{nome} encontrado!"
            return f"{nome} não está na lista."
print(busca_lenta("Diana",alunos))