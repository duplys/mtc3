CFLAGS=-Wall -Werror -g -O3 -I/usr/local/include
LDFLAGS=-L/usr/local/lib -lgsl -lgslcblas -lm

all:
	gcc $(CFLAGS) src/enigma.c -o enigma.x
	gcc $(CFLAGS) src/reader.c $(LDFLAGS) -o reader.x

clean:
	rm -f *~
	rm -f enigma.x
	rm -f reader.x
	rm -f src/*.o

tidy: clean
	rm -f decrypted/*
