.PHONY: validate test check

validate:
	python tools/validate_repo.py

test:
	python -m unittest discover -s tests -v

check: validate test
	python -m compileall -q tools tests
