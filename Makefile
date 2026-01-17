.PHONY: help doctor preflight test lint format security coverage gates

help:
	@echo "Targets:"
	@echo "  doctor     - environment + repo sanity checks"
	@echo "  test       - pytest (fast)"
	@echo "  coverage   - pytest with coverage (needs pytest-cov injected)"
	@echo "  lint       - ruff check"
	@echo "  format     - black --check"
	@echo "  security   - pip-audit + bandit"
	@echo "  gates      - repo audit gates (scripts/...)"
	@echo "  preflight  - all of the above (local CI equivalent)"

doctor:
	./setup.sh --doctor

test:
	pytest -q

coverage:
	pytest --cov=. --cov-report=term-missing

lint:
	ruff check .

format:
	black --check .

security:
	pip-audit
	bandit -r . -x tests

gates:
	python3 scripts/audit_readiness_validation.py
	python3 scripts/redaction_gate.py
	python3 scripts/replay_determinism_gate.py

preflight:
	python3 -m compileall .
	$(MAKE) test
	$(MAKE) lint
	$(MAKE) format
	$(MAKE) security
	$(MAKE) gates
