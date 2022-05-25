#include <stdio.h>
#include <stdlib.h>

int main() {
    int seed;
    printf("Enter the seed: \n");
    scanf("%d", &seed);
    srand(seed);
    printf("9%d", rand() % 10);
    printf("9%d", rand() % 10);
    printf("9%d", rand() % 10);
    printf("9%d", rand() % 10);
    printf("9%d", rand() % 10);
}
