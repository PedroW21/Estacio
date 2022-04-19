#include <stdio.h>

// Estruturas de repetição
// For
void main()
{

    // for (int contador = 0; contador <= 10; contador++)
    // { // Mostre de 0 a 10
    //     printf("O numero atual é %i\n", contador);
    // }

    // Multiplicação

    int multiplicador, multiplicando, resultado;

    printf("Bem vindo! Qual a tabuada que deseja saber?\n");
    scanf("%i", &multiplicando);

        for (multiplicador = 0; multiplicador <= 10; multiplicador++)
    {

        resultado = multiplicando * multiplicador;
        printf("%i x %i = %i\n", multiplicando, multiplicador, resultado);
    }
}
