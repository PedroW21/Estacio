#include <stdio.h>

// Vendo se o caboco passou de semestre

void main () {

    int bi1, bi2, bi3,bi4;
    float media;

    printf("Olá meu lindissimo estudante! Quer ver se passou de ano?\n");
    printf("Então por obséquio me informe suas 4 notas bimestrais:\n");

    scanf("%i%i%i%i", &bi1, &bi2, &bi3, &bi4);

    media = (bi1 + bi2 + bi3 + bi4)/4;

    if(media == 7) {
        printf("Passou no pau da rabiola em meu amigo, sua média foi: %.2e\n", media);
    } else if(media > 7) {
        printf("Meus parabéns!!! Sua média foi %.2e e você passou com folga!!!\n", media);
    } else {
        printf("Vai da não amigão, que irineu te abençoe nas provas finais de recuperação, aliás, tua média foi %0.2e\n", media);
    }

}