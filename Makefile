.PHONY: default

default: test

install:
	pipenv install --dev --skip-lock

test:
	pytest
