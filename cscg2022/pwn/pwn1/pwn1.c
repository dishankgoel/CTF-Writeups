#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

// pwn1: gcc pwn1.c -o pwn1

// --------------------------------------------------- SETUP

void ignore_me_init_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    _exit(0);
  }
}

void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

// --------------------------------------------------- MENU

typedef void (*target_t)(int, int, int);

void one_shot() {
  #ifndef CSCG_BUILDER
    printf("[!] You are using a self-compiled version of the challenge. Offsets might differ from the binary that is provided for the competition!\n");
  #endif
    target_t target = NULL;
    printf("-----------------------------------------\n");
    printf("| Look                                   |\n");
    printf("| If you had                             |\n");
    printf("| One shot                               |\n");
    printf("| Or one opportunity                     |\n");
    printf("| To seize everything you ever wanted    |\n");
    printf("| In one moment                          |\n"); 
    printf("| Would you capture it                   |\n");
    printf("| Or just let it slip?                   |\n");
    printf("-----------------------------------------\n");

    printf("\nIt's dangerous to go alone! Take this: ");
    printf("%llx", setvbuf);
    printf("\n\nEnter your shot: ");
    scanf("%llx", &target);
   
    printf("\n\nGood luck\n");
    target(0, 0, 0);
}


// --------------------------------------------------- MAIN

void main(int argc, char* argv[]) {
	ignore_me_init_buffering();
	ignore_me_init_signal();

  one_shot();
}

