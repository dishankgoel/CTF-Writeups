#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <fcntl.h>

// pwn1: gcc pwn2.c -o pwn2

// --------------------------------------------------- SETUP

char flag_buffer[1024];

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

void load_flag() {
    FILE* fp = fopen("/flag", "r");  
    int len = -1;
    if (fp == NULL) {
        printf("Error opening file: /flag\n");
        exit(-1);
    }

    fseek(fp, 0, SEEK_END);

    len = ftell(fp);

    // Read the flag
    fseek(fp, 0, SEEK_SET);
    fread(flag_buffer, 1, len, fp);
    fclose(fp);
}

// --------------------------------------------------- MENU

void print_stuff() {
    #ifndef CSCG_BUILDER
      printf("[!] You are using a self-compiled version of the challenge. Offsets might differ from the binary that is provided for the competition!\n");
    #endif
    char input_buffer[1024];
    memset(input_buffer, 0x00, 1024);

    printf("Give me some buffer: \n");
    scanf("%1023s", input_buffer);

    printf("You gave me: ");
    printf(input_buffer);
}


// --------------------------------------------------- MAIN

void main(int argc, char* argv[]) {
	ignore_me_init_buffering();
	ignore_me_init_signal();

  load_flag();
  print_stuff();
}

