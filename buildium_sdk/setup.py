"""Setup script for buildium_sdk (generated from OpenAPI spec)."""
from setuptools import setup, find_packages

setup(
    name="buildium-sdk",
    version="0.1.0",
    description="Buildium API Python SDK (generated from OpenAPI specification)",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "python-dateutil>=2.8.2",
        "urllib3>=1.25.3",
        "httpx>=0.27.0",
        "pydantic>=2.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

