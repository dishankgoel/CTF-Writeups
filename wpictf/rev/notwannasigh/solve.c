#include<stdlib.h>
#include <stdio.h>

int main(){
    FILE *f;
    FILE *flag;
    srand(1585599106);
    f = fopen("flag-gif.EnCiPhErEd", "rb");
    flag = fopen("flag.gif", "wb");
    char c;
    c = fgetc(f);
    int counter = 0;
    while(counter < 374109){
        char k;
        printf("%c",c);
        k = c^rand();
        fputc(k, flag);
        c = fgetc(f);
        counter++;
    }
    // printf("\n%d",counter);
    fclose(flag);
    fclose(f);
}