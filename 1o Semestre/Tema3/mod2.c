#include <stdio.h>

// %d ou %i para int (base decimal) | %o int (base octoal) | %x ou %X para int (hexadecimal) | %hd para Short Int | %ld para Long Int
// %c para char (unico caracter) | %f ou %e ou %E para float ou double

void main () {

    int day = 12;
    float pi = 3.14;
    
    int birthDay = 25;
    char month = 'j';

    printf("Hello World!!!\n");
    printf("Is such a beautiful day, don't you think?\n");
    printf("Ah, and just to say, today is %d\n", day);

    printf("Ah, and do you know the number of PI? I will sai to you, is %.2f\n", pi);

    puts("Another way to show something =D, like\n");
    printf("Ah, just to remember, my birthday will happen in %i of %c", birthDay, month);
}
