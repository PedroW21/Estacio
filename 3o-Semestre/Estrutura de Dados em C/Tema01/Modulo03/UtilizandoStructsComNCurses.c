#include <stdio.h>
#include <ncurses.h>

void main()
{
    // Struct

    struct cadastroAluno
    {
        int matricula;
        char nome[50];
        char disciplina[30];
        float notas[4];
    };

    // Fazendo o cadastro do aluno


    struct cadastroAluno aluno;

    printf("========================== Cadastro de Aluno ==========================\n\n");

    printf("Matrícula: ");
    scanf("%i", &aluno.matricula);
    
    getchar(); // comera a linha em branco do buffer e prossegue normal para coletar a linha do fgets

    printf("Nome do aluno: ");
    fgets(aluno.nome, sizeof(aluno.nome), stdin);
    fflush(stdin);

    printf("Disciplina: ");
    fgets(aluno.disciplina, sizeof(aluno.disciplina), stdin);

    printf("Nota 1: ");
    scanf("%f", &aluno.notas[0]);
    printf("Nota 2: ");
    scanf("%f", &aluno.notas[1]);
    printf("Nota 3: ");
    scanf("%f", &aluno.notas[2]);
    printf("Nota 4: ");
    scanf("%f", &aluno.notas[3]);

    float media = (aluno.notas[0] + aluno.notas[1] + aluno.notas[2] + aluno.notas[3])/4;

    printf("\n========================== Dados da Struct ==========================\n\n");

    printf("Matrícula: %i\n", aluno.matricula);
    printf("Nome: %s", aluno.nome);
    printf("Disciplina: %s", aluno.disciplina);
    printf("Média: %.2f\n\n", media);

}  