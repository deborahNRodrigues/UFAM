import ast

def pontos_jogo(vetor_aneis):
    pontuacao = 10000
    for i in range(len(vetor_aneis)):
        anel = vetor_aneis[i]
        if anel == 1:
            pontuacao = pontuacao * 2
        elif anel == 2:
            pontuacao = pontuacao
        elif anel == 3:
            pontuacao = pontuacao / 2
        elif anel == 4:
            pontuacao = pontuacao / 4
    return pontuacao

entrada = input("Digite o valor nesse formato -> 3,2,1,2,4  :  ")                          # usuário digita: [3,2,1,2,4]
vetor = ast.literal_eval(entrada)
resultado = pontos_jogo(vetor)
print(round(resultado, 2))               # quantas casas decimais o enunciado pede?