#include <stdio.h>

int main () {

    // Qual o maior salário e sua média?

    int salario, media, guardaMaiorSalario, acumulaSalarios, iterador;

    guardaMaiorSalario = 0;

    for(iterador = 0; iterador < 15; iterador++) {

        printf("Por obséquio, digite o salário: ");
        scanf("%i", &salario);

        acumulaSalarios += salario;

        if(salario > guardaMaiorSalario) guardaMaiorSalario = salario;
        
    }

     media = acumulaSalarios / 15;
     printf("A média dos salarios de sua empresa é: R$%i\n", media);
     printf("Sendo o maior deles: R$%i\n", guardaMaiorSalario);


}