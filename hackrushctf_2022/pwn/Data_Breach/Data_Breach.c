#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

/* Ignore these functions */
void buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] DOS Alert\n");
        _exit(0);
    }
}

void kill_signal() {
    signal(SIGALRM, timeout);
    alarm(60);
}

// Real challenge starts here

void func() {
    char flag[50];
    FILE* f = fopen("flag.txt", "r");
    fscanf(f, "%s", flag);
    fclose(f);
    printf("[*] We suspect that there may be a big data breach that has happened on our servers\n");
    printf("Can you find what caused it?: ");
    char cause[100];
    fgets(cause, 100, stdin);
    printf(cause);
}

int main() {
    buffering();
    kill_signal();
    func();
}
