'''
Programa que recebe a nota do aluno e 
retorna o estado de aprovação do mesmo
através de uma condicional
''' 

print("--- BOLETIM DE NOTAS ---\n")

nome = input("Nome do(a) aluno(a): ")
curso = input("Curso inserido(a): ")
semestre = int(input("Semestre: "))
disciplina = input("Disciplina: ")
nota = int(input("Nota: "))

if nota > 59:
    print("Aprovado!")
elif 39 < nota < 60:
    print("Recuperação.")
else:
    print("Reprovado!")
