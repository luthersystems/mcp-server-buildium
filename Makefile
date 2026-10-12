.PHONY: generate-sdk clean install dev-install test test-integration lint typecheck audit check format

PIP_AUDIT_VERSION ?= 2.10.1

# Generate Python SDK from OpenAPI spec using Docker
generate-sdk:
	@echo "Generating Python SDK from OpenAPI spec using Docker..."
	@docker run --rm -v "${PWD}:/local" -v /tmp:/tmp openapitools/openapi-generator-cli:latest generate \
		-i /tmp/buildium-openapi.json \
		-g python \
		-o /local/buildium_sdk \
		-p packageName=buildium_sdk,projectName=buildium-sdk,packageVersion=0.1.0,library=httpx,generateSourceCodeOnly=true \
		--skip-validate-spec
	@echo "SDK generated in buildium_sdk/ directory"
	@echo "Then run: uv run python scripts/lenient_response_enums.py"
	@echo "Installing generated SDK..."
	@cd buildium_sdk && uv pip install -e .

# Clean generated files
clean:
	rm -rf buildium_sdk/
	rm -f openapi-generator-cli.jar
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

# Install dependencies
install:
	uv sync

# Install with dev dependencies
dev-install:
	uv sync --extra dev

# Run the offline unit tests
test:
	uv run pytest tests/ --ignore=tests/test_integration.py

# Run integration tests (requires .env file)
test-integration:
	uv run pytest tests/test_integration.py -v

# Run linter
lint:
	uv run ruff check .
	uv run ruff format --check .

# Run the type checker
typecheck:
	uv run mypy

# Fail on any known vulnerability in uv.lock (dev tools included)
audit:
	mkdir -p build
	uv export --frozen --all-extras --no-emit-project --format requirements-txt -o build/requirements-audit.txt -q
	uvx pip-audit==$(PIP_AUDIT_VERSION) --strict --disable-pip --require-hashes -r build/requirements-audit.txt

# Everything CI checks, except the integration tests
check: lint typecheck test audit

# Format code
format:
	uv run ruff format .
	uv run ruff check --fix .

