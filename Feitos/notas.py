#Condição principal
def notaDoAluno(nota):
    if(nota >= 8):
        return True
    else:
        return False

#Nome do aluno
nome = input("Qual o nome do estudante ? \n")
#Idade do aluno
idade = int(input("Qual a sua idade ? \n"))
#Nota do aluno
nota = float(input("Digite a nota ? \n"))
print("\n")


#Avaliação da nota do aluno
if notaDoAluno(nota):
    print("Você foi aprovado")
else:
    print("Infelimente você foi reprovado")
