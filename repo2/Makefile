SHELL := /bin/bash

test:
	uv run pytest tests/

test-with-editable:
	@if [ ! -d ../repo1 ]; then \
		echo "Cloning repo1 to ../repo1"; \
	fi
	@uv add -q --editable  "repo1 @ ../repo1" 
	-@uv run pytest tests/
	@uv add -q "repo1 @ ../dist/repo1-0.1.0-py3-none-any.whl"
