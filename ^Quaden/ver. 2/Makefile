exec = main.out
sources = $(wildcard src/*.c)
objects = $(sources:.c=.o)
flags = -g

build_dir = build

$(build_dir)/%.o: %.c include/%.h
	gcc -c $(flags) $< -o $@

$(exec): $(objects)
	gcc $(objects) $(flags) -o $(exec)

install:
	make
	cp ./main.out /usr/local/bin/Quaden

clean:
	-rm *.out
	-rm *.objects
	-rm src/*.o

