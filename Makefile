.PHONY: help install run test docker-build docker-up docker-up-d docker-down docker-logs clean venv

# Default target
help:
	@echo "HTTP Metadata Inventory Service - Available targets:"
	@echo ""
	@echo "  make install      - Install Python dependencies"
	@echo "  make run          - Run API locally (uvicorn with reload)"
	@echo "  make test         - Run pytest"
	@echo "  make venv         - Create virtual environment"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build - Build API image"
	@echo "  make docker-up    - Start all services (foreground)"
	@echo "  make docker-up-d  - Start all services (detached)"
	@echo "  make docker-down  - Stop all services"
	@echo "  make docker-logs  - Tail API container logs"
	@echo ""
	@echo "  make clean        - Remove cache and build artifacts"

# Python
VENV ?= .venv
PYTHON ?= python3
PIP ?= pip

venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Created $(VENV). Activate with: source $(VENV)/bin/activate"

install:
	$(PIP) install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest -v

# Docker
docker-build:
	docker-compose build

docker-up:
	docker-compose up --build

docker-up-d:
	docker-compose up -d --build

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f api

# Start only MongoDB (for local dev with uvicorn)
mongo:
	docker-compose up -d mongo

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Cleaned cache and artifacts"
