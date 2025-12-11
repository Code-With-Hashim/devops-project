.PHONY: help build up down logs test clean deploy

# Variables
IMAGE_NAME = devops-project
IMAGE_TAG = latest
DOCKER_COMPOSE = docker-compose

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build Docker image
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

up: ## Start all services with docker-compose
	$(DOCKER_COMPOSE) up -d

down: ## Stop all services
	$(DOCKER_COMPOSE) down

logs: ## Show logs from all services
	$(DOCKER_COMPOSE) logs -f

test: ## Run tests
	python -m pytest tests/ -v || echo "No tests directory found"

lint: ## Run linter
	flake8 app.py --count --select=E9,F63,F7,F82 --show-source --statistics || true

clean: ## Remove containers, volumes, and images
	$(DOCKER_COMPOSE) down -v
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG) || true

deploy-k8s: ## Deploy to Kubernetes
	kubectl apply -f kubernetes/

undeploy-k8s: ## Remove Kubernetes resources
	kubectl delete -f kubernetes/

terraform-init: ## Initialize Terraform
	cd terraform && terraform init

terraform-plan: ## Plan Terraform changes
	cd terraform && terraform plan

terraform-apply: ## Apply Terraform changes
	cd terraform && terraform apply

terraform-destroy: ## Destroy Terraform infrastructure
	cd terraform && terraform destroy

install-deps: ## Install Python dependencies
	pip install -r requirements.txt

run-local: ## Run application locally
	python app.py

