test:
	pytest --cov=. --cov-report term-missing tests/

default: test
