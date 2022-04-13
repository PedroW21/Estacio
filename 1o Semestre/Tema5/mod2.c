#include <stdio.h>


void main() {

    // Qual o maior, usando o while

    int maiorNumero, numeroDigitado, iterador;
    
    maiorNumero = 0;
    iterador = 0;

    while(iterador < 5) {

        iterador++;

        printf("Por favor, digite um número: ");
        scanf("%i", &numeroDigitado);

        if(numeroDigitado > maiorNumero) maiorNumero = numeroDigitado;

    }

    printf("O maior numero digitado foi: %i\n", maiorNumero);
}