#include <stdio.h>
#include <string.h>

void main()
{

    char array[50][3] = {"Adalberto", "Alice", "Bob"};

    printf("Digite o nome que deseja encontrar: ");
    char nomeProcurado[50];
    scanf("%s", &nomeProcurado);

    for (int i = 0; i < sizeof(array); i++)
    {
        if (strcmp(nomeProcurado, array[i]) == 0)
        {
            printf("\nNome encontrado!!\n\n");

            printf("Nome na posicão %i\n\n", i);
        }
    }
}