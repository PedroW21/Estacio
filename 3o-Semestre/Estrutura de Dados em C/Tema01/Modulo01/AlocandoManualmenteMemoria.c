#include <stdlib.h>
#include <stdio.h>

void * malloc (size_t size); // aloca um determinado numero de bytes e retorna o ponteiro (a referencia do local) para o primeiro byte alocado ou null (se nao for possivel alocar)

void * calloc () // aloca um bloco de memoria suficiente para conter um vetor dinamico

void free (void *ptr); // liberação manual do espaço alocado

ptr = NULL; // não é obrigatório, mas aconselhável (boa pratica);

void * realloc (void *ptr, size_t newsize);

// Declaração de um ponteiro para acesso indireto a uma variavel 

Tipo_da_varial * Nome_da_Variavel;

//Ex: 
int *p;
float *q;
char *r;



