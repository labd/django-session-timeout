.PHONY: install test upload docs


install:
	pip install -e .[docs,test]

test:
	py.test

retest:
	py.test -vvv --lf

coverage:
	py.test --cov=django_session_timeout --cov-report=term-missing --cov-report=html

docs:
	$(MAKE) -C docs html

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

BLACK_EXCLUDE="/(\.git|\.hg|\.mypy_cache|\.tox|\.venv|_build|buck-out|build|dist)/"
black:
	pip install --upgrade black
	black --verbose --exclude $(BLACK_EXCLUDE) ./src
	black --verbose --exclude $(BLACK_EXCLUDE) ./tests
