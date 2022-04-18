#include <stdio.h>

int main(void) {
    int variavelParaAlterar = 10;

    int *ponteiro;

    ponteiro = &variavelParaAlterar; // recebe a referencia do valor na memoria;

    printf("Utilizando ponteiros, seja o que Deus quiser =D\n");
    printf("Conteúdo da variável: %i\n", variavelParaAlterar);
    printf("Endereço da váriavel na memória: %x\n", &variavelParaAlterar); //foi utilizado x por ser um valor hexadecimal;
    printf("Conteúdo da váriavel ponteiro: %x\n", ponteiro); 

    return 0;
}