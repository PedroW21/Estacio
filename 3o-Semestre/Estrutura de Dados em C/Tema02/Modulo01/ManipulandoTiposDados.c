#include <stdio.h>
#include <ctype.h>

void main()
{
    char arg[20] = "Example";

    int saberMaisculo = isupper(arg);
    int saberCaractere = isalpha(arg);
    char argMinusculo[sizeof(arg)] = tolower(arg);
}