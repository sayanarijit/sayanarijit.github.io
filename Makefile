.PHONY: build
build:
	@[ ! -d dist ] && mkdir dist || true
	@python3.7 src/index.py > dist/index.html
