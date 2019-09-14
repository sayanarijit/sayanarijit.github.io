.PHONY: build
build:
	@if [ -d dist ]; then rm -rf dist && mkdir dist; fi
	@python3.7 src/index.py > dist/index.html
