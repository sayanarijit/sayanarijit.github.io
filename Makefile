.PHONY: install
install:
	@if [ -d .venv ]; then rm -rf .venv; fi
	@${MAKE} .venv

.venv:
	@python3.7 -m venv .venv
	@.venv/bin/pip install -r dev-requirements.txt

.PHONY: build
build: .venv
	@${MAKE} test
	@if [ -d dist ]; then rm -rf dist && mkdir dist; fi
	@PYTHONPATH=$$PWD/src .venv/bin/python src/index.py > dist/index.html

.PHONY: test
test: .venv
	@.venv/bin/black --diff src
	@.venv/bin/mypy src
	@.venv/bin/typecov 100 .typecov/report/linecount.txt
