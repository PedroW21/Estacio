#include <stdio.h>
#include <conio.h>

int main(void) {
    int variavelParaAlterar = 10;

    int *ponteiro;

    ponteiro = &variavelParaAlterar; // recebe a referencia do valor na memoria;

    printf("Utilizando ponteiros, seja o que Deus quiser =D\n");
    printf("Conteúdo da variável: %i\n", variavelParaAlterar);
    printf("Endereço da váriavel na memória: %x\n", &variavelParaAlterar);
    printf("Conteúdo da váriavel ponteiro: %x", ponteiro);

    getch();

    return 0;
}