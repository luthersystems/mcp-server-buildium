.PHONY: generate-sdk clean install dev-install test lint format

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
	uv pip install -e .

# Install with dev dependencies
dev-install:
	uv pip install -e ".[dev]"

# Run tests
test:
	uv run pytest tests/ --ignore=tests/test_integration.py -v

# Run integration tests (requires .env file)
test-integration:
	uv run pytest tests/test_integration.py -v

# Run linter
lint:
	uv run ruff check .
	uv run ruff format --check .

# Format code
format:
	uv run ruff format .
	uv run ruff check --fix .

