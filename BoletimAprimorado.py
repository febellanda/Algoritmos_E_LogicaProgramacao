print("--- BOLETIM DE NOTAS ---")

# Armazena as informações do usuário em variáveis

nome = input("\nNome do aluno(a): ")
curso = input("\nCurso: ")
semestre = int(input("\nSemestre: "))
disciplina = input("\nDisciplina: ")
nota1 = float(input("\nNota 1 bimestre: "))
nota2 = float(input("\nNota 2 bimestre: "))
media = (nota1 + nota2) / 2

 
# Laço de repetição para nao permitir que o usuário coloque notas 
# que fogem do padrão da instituição

while media > 100 or media < 0:
    print("Esse número é inválido, tente novamente")
    nota1 = int(input("\nDigite a nota 1 bimestre novamente: "))
    nota2 = int(input("\nDigite a nota 2 bimestre novamente: "))
    media = (nota1 + nota2) / 2
    break

# Função para armazenar os dados do aluno inseridos pelo usuário

def dados():
    print(f"Aluno(a): {nome}\n"
    f"Curso: {curso} \n"
    f"Semestre: {semestre}\n"
    f"Disciplina: {disciplina}\n"
    f"Média: {media}\n"
    )    


# Condicional que verifica o estado de aprovação do aluno
# com base na sua média semestral

if media > 59:
    dados()
    print("APROVADO!")

elif 39 < media < 60:
    dados()
    print("RECUPERAÇÂO!")

else:
    dados()
    print("REPROVADO!")
     
