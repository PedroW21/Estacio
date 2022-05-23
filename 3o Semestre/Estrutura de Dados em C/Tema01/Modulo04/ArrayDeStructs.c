#include <stdio.h>

typedef struct
{
    int Matricula;
    char Nome[50];
    char Materia[50];
    float notas[4];
    float Media;
} CadastroAluno;

void main()
{

    printf("---------- CADASTRO ALUNO ----------\n\n");

    int qtdCadastro;

    printf("Quantos alunos deseja cadastrar? ");
    scanf("%i", &qtdCadastro);

    printf("\n");

    CadastroAluno aluno[qtdCadastro];

    int fimCadastro = qtdCadastro;

    for (int i = 0; i < qtdCadastro; i++)
    {
        printf("Digite a matricula do aluno: ");
        scanf("%i", &aluno[i].Matricula);
        
        getchar();

        printf("Digite o nome do aluno: ");
        fgets(aluno[i].Nome, sizeof(aluno[i].Nome), stdin);

        // funciona, scanf safado

        // getchar();

        printf("Digite a matéria: ");
        fgets(aluno[i].Materia, sizeof(aluno[i].Materia), stdin);
        
        // getchar();

        printf("Digite as 4 notas do aluno: ");

        // getchar();

        scanf("%f", &aluno[i].notas[0]);
        scanf("%f", &aluno[i].notas[1]);
        scanf("%f", &aluno[i].notas[2]);
        scanf("%f", &aluno[i].notas[3]);

        aluno[i].Media = (aluno[i].notas[0] + aluno[i].notas[1] + aluno[i].notas[2] + aluno[i].notas[3]) / 4;

        fimCadastro -= 1;

        if (i < qtdCadastro-1)
            printf("\nFim do %io cadastro, faltam %i\n\n", i + 1, fimCadastro);
    }

    printf("\n\n------------ DADOS DOS ALUNOS ------------\n\n");

    for (int i = 0; i < qtdCadastro; i++)
    {
        printf("%io ALUNO\n\n", i + 1);

        printf("Matricula: %i\n", aluno[i].Matricula);
        printf("Nome: %s\n", aluno[i].Nome);
        printf("Matéria: %s\n", aluno[i].Materia);
        printf("Média Final: %.2f\n\n", aluno[i].Media);
    }

    printf("FIM!");
}