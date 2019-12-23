default: lint

lint: lint_python lint_shell

lint_python:
	@echo "Linting python scripts..."
	isort -df -rc -w 99 *.py
	yapf -dr *.py
	pylama *.py

lint_shell:
	@echo "Linting shell scripts..."
	shellcheck *.sh
