#
# Makefile for ice9
CC	= gcc
CFLAGS	= -g -Wall -pedantic -std=c99

LIB	= -lfl
SRC	= ice9.l ice9.y
OBJ	= ice9.yy.o ice9.tab.o 

ice9:	$(OBJ)
	$(CC) -o $@ $^ $(LIB)

ice9.tab.c: ice9.y
	bison -d -t -v -o $@ $<

ice9.tab.h: ice9.y
	bison -d -o ice9.tab.c $<
	rm -f ice9.tab.c

ice9.tab.o: ice9.tab.c
	$(CC) $(CFLAGS) -c $<

ice9.yy.c: ice9.l ice9.tab.h
	flex -o$@ $<

ice9.yy.o: ice9.yy.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f $(OBJ) ice9.output

cleanest:
	make clean
	rm -f ice9.tab.c ice9.yy.c ice9.tab.h ice9

tar:	p1.tar.gz

p1.tar.gz:	Makefile $(SRC)
	tar czvf $@ Makefile $(SRC)