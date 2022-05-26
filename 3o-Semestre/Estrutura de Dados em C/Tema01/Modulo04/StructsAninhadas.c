#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h> // entendera caracteres especificos do alfabeto br (ex.: ç)

typedef struct
{
    int matricula;
    char nome[50];

    struct
    {
        char nomeDaMae[50];
        char nomeDoPai[50];
        int telMae;
        int telPai;
    };

} DadosAluno;

void main()
{
    setlocale(LC_ALL, "portuguese");

    DadosAluno aluno;

    /* Cadastro do Aluno (na mao gorda)*/

    aluno.matricula = 123456;
    strcpy(aluno.nome, "Pierre"); // pierre sera copiado para aluno.nome
    strcpy(aluno.nomeDaMae, "Jabiscreia");
    strcpy(aluno.nomeDoPai, "Jabiscreio");
    aluno.telMae = 897652;
    aluno.telPai = 576845;

    printf("---------- Mostrando os Dados de Structs Aninhadas ----------\n\n");

    printf("Matricula: %i\n", aluno.matricula);
    printf("Nome: %s\n", aluno.nome);
    printf("Nome dos pais: %s e %s\n", aluno.nomeDaMae, aluno.nomeDoPai);
    printf("Telefones da mãe e do pai: %i / %i\n\n", aluno.telMae, aluno.telPai);

}