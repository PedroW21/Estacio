#include <stdio.h>
#include <stdlib.h>

int main()
{

    int *p, i; // p = ponteiro

    p = malloc(10 * sizeof(int)); // 10x o tamanho de um int (4bytes) - Alocando

    if (p = NULL)
    { // verificando se é possivel alocar, caso não seja (o retorno é null) aparece a mensagem
        printf("Espaçõ Insuficiente");
        exit(1);
    }

    printf("Primeiros 10 números");
    for (i = 0; i < 10; i++)
    {
        p[i] = i + 10;

        printf("Índice atual: %d \n Conteúdo do índice atual: %d\n", i, p[i]);
    }

    // Realocando a memoria

    p = realloc(p, 20 * sizeof(int));

    printf("Realocando - aumentando - para mais 10 números\n");
    for (int i = 10; i < 20; i++)
    {
        p[i] = i + 20;
        printf("Índice atual --realocado--: %d \n Conteúdo do índice atual --realocado--: %d\n", i, p[i]);
    }

    printf("Todos os 20 números realocados\n");
    for (int i = 0; i < 20; i++)
    {
        printf("Índice atual: %d \n Conteúdo do índice atual: %d\n", i, p[i]);
    }

    free(p); // liberando a memoria no tapa

    printf("pause");
    return(0);
}