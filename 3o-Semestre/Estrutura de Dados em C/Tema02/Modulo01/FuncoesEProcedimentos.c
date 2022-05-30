#include <stdio.h>

int media(int num1, int num2)
{
    return (num1 + num2)/2;
}

void mostre(int element)
{
    printf("A média foi: %d", element);
}

void main()
{
    int val1, val2;

    printf("Insira dois valores para calcular a média: ");
    scanf("%d", &val1);
    scanf("%d", &val2);

    int resultado = media(val1, val2);
    mostre(resultado);
}