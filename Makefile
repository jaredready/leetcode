all: init test

init:
	pipenv install

test:
	pipenv run python -m unittest discover

.PHONY: all init test
