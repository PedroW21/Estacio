#include <stdio.h>
#include <stdlib.h>

struct Aluno
{
    int numMatric;
    float notas[3];
    float media;
};

int main()
{
    struct Aluno Pierre;

    Pierre.numMatric = 12345;
    Pierre.notas[0] = 7.6;
    Pierre.notas[1] = 8.4;
    Pierre.notas[2] = 6.9;
    Pierre.media = (Pierre.notas[0] + Pierre.notas[1] + Pierre.notas[2])/3;

    printf("Matrícula: %i\n", Pierre.numMatric);
    printf("Média: %.2f\n", Pierre.media);

    system("pause");

    return(0);

}
