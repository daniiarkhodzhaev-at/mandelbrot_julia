.PHONY: all clean build

all: build

build: calc.so

calc.so: calc.o
	gcc -shared calc.o -o calc.so

calc.o: calc.c
	gcc -c -fPIC -fpic -O3 calc.c -o calc.o -Wall -Wextra -Werror
