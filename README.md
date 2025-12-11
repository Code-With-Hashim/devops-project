# DevOps Project - Resume Demo

A comprehensive DevOps project demonstrating modern DevOps practices, CI/CD pipelines, containerization, infrastructure as code, and monitoring.

## 🚀 Features

- **Containerization**: Docker multi-stage builds for optimized production images
- **Orchestration**: Docker Compose for local development and Kubernetes manifests for production
- **CI/CD**: GitHub Actions pipeline with automated testing, building, and deployment
- **Infrastructure as Code**: Terraform configurations for AWS infrastructure
- **Monitoring**: Prometheus and Grafana setup for metrics and visualization
- **Security**: Non-root containers, security scanning, and best practices
- **Scalability**: Kubernetes HPA for automatic scaling

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.11+
- Kubernetes cluster (for K8s deployment)
- Terraform (for infrastructure provisioning)
- AWS CLI configured (for Terraform)

## 🛠️ Tech Stack

- **Application**: Python Flask
- **Containerization**: Docker
- **Orchestration**: Kubernetes, Docker Compose
- **CI/CD**: GitHub Actions
- **Infrastructure**: Terraform, AWS
- **Monitoring**: Prometheus, Grafana
- **Web Server**: Gunicorn

## 📦 Quick Start

### Local Development with Docker Compose

```bash
# Start all services
make up
# or
docker-compose up -d

# View logs
make logs
# or
docker-compose logs -f

# Stop services
make down
# or
docker-compose down
```

Access the application:
- Web App: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)

### Run Locally (Python)

```bash
# Install dependencies
make install-deps
# or
pip install -r requirements.txt

# Run application
make run-local
# or
python app.py
```

### Build Docker Image

```bash
make build
# or
docker build -t devops-project:latest .
```

## 🚢 Deployment

### Kubernetes Deployment

```bash
# Deploy to Kubernetes
make deploy-k8s
# or
kubectl apply -f kubernetes/

# Check deployment status
kubectl get pods
kubectl get services

# Remove deployment
make undeploy-k8s
# or
kubectl delete -f kubernetes/
```

### Infrastructure with Terraform

```bash
# Initialize Terraform
cd terraform
terraform init

# Review changes
terraform plan

# Apply infrastructure
terraform apply

# Destroy infrastructure
terraform destroy
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Linting**: Code quality checks with Flake8
2. **Testing**: Automated unit tests with pytest
3. **Building**: Docker image build and push to registry
4. **Security Scanning**: Trivy vulnerability scanning
5. **Deployment**: Automated deployment to staging and production

### Pipeline Triggers

- **Push to `main` or `develop`**: Runs lint, test, and build
- **Pull Requests**: Runs lint and test
- **Releases**: Full pipeline including production deployment

## 📊 Monitoring

### Prometheus

Prometheus scrapes metrics from:
- Application metrics endpoint (`/api/metrics`)
- Kubernetes pods (if configured)
- Prometheus itself

### Grafana

Pre-configured dashboards for:
- Application metrics
- System performance
- Request rates and response times

Access Grafana at http://localhost:3000 (default: admin/admin)

## 📁 Project Structure

```
.
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Multi-stage Docker build
├── docker-compose.yml    # Local development setup
├── Makefile             # Common commands
├── .github/
│   └── workflows/
│       └── ci-cd.yml    # CI/CD pipeline
├── kubernetes/
│   ├── deployment.yaml  # K8s deployment
│   ├── service.yaml     # K8s service
│   ├── ingress.yaml     # K8s ingress
│   ├── configmap.yaml   # K8s config
│   └── hpa.yaml         # Horizontal Pod Autoscaler
├── terraform/
│   ├── main.tf          # Main infrastructure
│   ├── variables.tf     # Variables
│   ├── outputs.tf       # Outputs
│   └── terraform.tfvars.example
├── monitoring/
│   ├── prometheus.yml   # Prometheus config
│   └── grafana/         # Grafana configs
└── tests/
    └── test_app.py      # Unit tests
```

## 🧪 Testing

```bash
# Run tests
make test
# or
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html
```

## 🔒 Security Best Practices

- Non-root user in Docker containers
- Multi-stage Docker builds for smaller images
- Security scanning in CI/CD pipeline
- Health checks and resource limits in Kubernetes
- Secrets management (use Kubernetes secrets or AWS Secrets Manager)

## 📝 Environment Variables

- `ENVIRONMENT`: Application environment (development, staging, production)
- `APP_VERSION`: Application version
- `PORT`: Application port (default: 5000)
- `FLASK_ENV`: Flask environment mode

## 🎯 API Endpoints

- `GET /` - Homepage
- `GET /health` - Health check endpoint
- `GET /api/info` - Application information
- `GET /api/metrics` - Prometheus metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is for demonstration purposes.

## 🔗 Useful Commands

```bash
# View all available commands
make help

# Check application health
curl http://localhost:5000/health

# View application info
curl http://localhost:5000/api/info

# View metrics
curl http://localhost:5000/api/metrics
```

## 📚 Learning Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Documentation](https://www.terraform.io/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Prometheus Documentation](https://prometheus.io/docs/)

---

**Note**: This is a demonstration project for resume purposes. Adjust configurations according to your specific requirements and security policies.

