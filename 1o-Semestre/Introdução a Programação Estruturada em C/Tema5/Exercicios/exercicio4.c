#include <stdio.h>

// Vendo se foi aprovado a turma de 40 alunos


void main() {
    
    float nota1, nota2, nota3, media;
    int iterador;

    for(iterador=1; iterador < 10; iterador++) {
        
        printf("Por obséquio insira a 1a nota do %io aluno: ", iterador);
        scanf("%f", &nota1);

        printf("Por obséquio insira a 2a nota do %io aluno: ", iterador);
        scanf("%f", &nota2);

        printf("Por obséquio insira a 3a nota do %io aluno: ", iterador);
        scanf("%f", &nota3);

        media = (nota1 + nota2 + nota3)/3;

        if(media >= 7.0) {
            printf("Parabéns!!!! O %io aluno passou! E com a nota: %.1f\n", iterador, media);
        } else {
            printf("Infelizmente o %io aluno não passou! Ele terá que ir para as finais, pois ficou com a nota %.1f\n", iterador, media);
        }
    }
     
}