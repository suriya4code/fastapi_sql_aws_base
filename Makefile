POETRY ?= poetry
PYTHON ?= python3

.PHONY: help env install run test clean

help:
	@echo "Available targets:"
	@echo "  env     - Set up the poetry environment and install dependencies"
	@echo "  run     - Run the FastAPI app with uvicorn (reload enabled)"
	@echo "  test    - Run all tests with coverage report"
	@echo "  clean   - Remove .venv and .pytest_cache"

env:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install poetry
	$(POETRY) install

install: env

run:
	$(POETRY) run uvicorn app.main:app --reload

test:
	PYTHONPATH=. $(POETRY) run pytest --cov=app --cov-report=term-missing

clean:
	rm -rf .venv .pytest_cache __pycache__
