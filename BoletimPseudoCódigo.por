programa {
  funcao inicio() {
    escreva ("--- BOLETIM DE NOTAS ---\n")

    cadeia nome
    cadeia curso 
    cadeia semestre
    cadeia disciplina
    inteiro nota 

    escreva ("\nNome do(a) aluno(a): ")
    leia (nome)

    escreva ("Curso inserido(a): ")
    leia (curso)

    escreva ("Semestre: ")
    leia (semestre)

    escreva ("Disciplina: ")
    leia (disciplina)

    escreva ("Nota: ")
    leia (nota)

    se (nota > 59 e nota < 101){
      escreva ("Aprovado!")
    }
    senao se (39 < nota e nota < 60){
      escreva ("Recuperação.")
    }
    senao {
      escreva ("Reprovado.")
    }
  }
}
