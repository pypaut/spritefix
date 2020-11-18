OBJS = src/*.py

all: lint
	python3 src/main.py -r 13 -c 25

lint:
	black -l 79 $(OBJS)
