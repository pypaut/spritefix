OBJS = src/*.py

all: lint
	python3 src/main.py

lint:
	flake8 $(OBJS)
