.PHONY: build
build:
	@if [ -d dist ]; then rm -rf dist && mkdir dist; fi
	@cd src && python3.7 index.py > ../dist/index.html
