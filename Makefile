.PHONY: all build test clean

all: build test

build:
	python setup.py sdist

test:
	pytest tests/

clean:
	rm -rf dist *.egg-info

