PYTHON?=python

.PHONY: venv
venv:
	$(PYTHON) -m venv .venv
	source .venv/bin/activate && make setup dev
	@echo 'run `source .venv/bin/activate` to use virtualenv'

# The rest of these are intended to be run within the venv, where python points
# to whatever was used to set up the venv.

.PHONY: setup
setup:
	python -m pip install -Ur requirements.txt
	python -m pip install -Ur requirements-dev.txt

.PHONY: test
test:
	which python
	python -m coverage run -m woah.tests
	python -m coverage report

.PHONY: format
format:
	isort --recursive -y woah setup.py
	black woah setup.py

.PHONY: release
release:
	pip install -U wheel
	rm -r dist
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
