init:
	pipenv install

test:
	pipenv run python -m unittest discover

.PHONY: init test
