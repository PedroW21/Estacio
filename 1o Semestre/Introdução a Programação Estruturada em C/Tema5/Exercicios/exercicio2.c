#include <stdio.h>

// O maior numero entre 15 entradas


int main() {
    int cont, num, maior;
    maior = 0;

    for(cont=1; cont <= 15; cont++) {
        printf("Digite um numero: ");
        scanf("%i", &num);

        if(num > maior) maior = num;
    }

    printf("O maior dos números é: %i\n", maior);
}