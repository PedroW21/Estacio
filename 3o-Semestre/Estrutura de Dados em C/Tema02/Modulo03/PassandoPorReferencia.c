#include <stdio.h>

void trocar(int *x, int *y)
{
    int auxiliar;

    if(x != NULL && y != NULL)
    {
        auxiliar = *x;
        *x = *y;
        *y = auxiliar;
    }
}

void main()
{
    int valor1 = 12, valor2 = 2;

    trocar(&valor1, &valor2);

    printf("Valor 1: %d\nValor 2: %d\n", valor1, valor2);
}