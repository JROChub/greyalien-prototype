.PHONY: test lint format format-check typecheck coverage ci release

test:
	python -m unittest discover -s tests

lint:
	ruff check .

format:
	ruff format .

format-check:
	ruff format --check .

typecheck:
	mypy

coverage:
	coverage run -m unittest discover -s tests
	coverage report

ci: lint format-check typecheck coverage test

release:
	@echo "1) Update CHANGELOG.md"
	@echo "2) Bump version in pyproject.toml"
	@echo "3) Run: make ci"
	@echo "4) Tag and push: git tag vX.Y.Z && git push origin vX.Y.Z"
	@echo "5) Create GitHub release with changelog notes"
