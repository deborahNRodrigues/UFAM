def adicionar_aluno(lista, nome):
    #adiciona nome do aluno na lista
    lista.append(nome)
    return lista
turma = ["Vera, Agenor, Diogo, Maria"]
print("Informe o nome do novo aluno da turma", adicionar_aluno(turma,"Teste"))


def remover_aluno(lista, nome):
  #remover um aluno da turma
 lista.remove(nome)
 return lista
print("Informe o nome do aluno que será removido", remover_aluno(lista=turma,nome='Teste'))

def listar_alunos(lista):
#listar todos os alunos da turma
