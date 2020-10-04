SHELL := bash
.ONESHELL:
.DELETE_ON_ERROR:

python = python3
venv = ./.venv

venv: $(venv)

$(venv):
	$(python) -m venv $(venv)
	$(venv)/bin/pip install --upgrade pip
	$(venv)/bin/pip install -r requirements.txt

fmt: venv
	isort -rc *.py
	yapf -ir *.py

lint: venv
	pylint --rcfile=setup.cfg *.py

lint_shell:
	shellcheck *.sh
