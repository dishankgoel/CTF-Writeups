# Makefile for ttcomp

COMPILE = gcc -I. -O2 -Wall
LINK    = gcc -o $@

OBJ = implode.o ttdecomp.o

ttdecomp: $(OBJ)
	$(LINK) $(OBJ)

$(OBJ): common.h implode.h posix.h

.c.o:
	$(COMPILE) -c $<

clean:
	$(RM) *.o ttdecomp *~ *.bak
