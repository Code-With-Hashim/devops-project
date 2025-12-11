# Architecture Overview

## System Architecture

This DevOps project demonstrates a modern, cloud-native application architecture with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                     CI/CD Pipeline                          │
│                  (GitHub Actions)                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Container Registry (GHCR)                      │
│              Docker Images                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Infrastructure (Terraform)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │     VPC      │  │   Subnets    │  │   IGW        │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Kubernetes Cluster                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Deployment (3 replicas)                           │    │
│  │  ┌────────┐  ┌────────┐  ┌────────┐              │    │
│  │  │  Pod   │  │  Pod   │  │  Pod   │              │    │
│  │  └────────┘  └────────┘  └────────┘              │    │
│  └────────────────────────────────────────────────────┘    │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Service (LoadBalancer)                            │    │
│  └────────────────────────────────────────────────────┘    │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Ingress (NGINX)                                   │    │
│  └────────────────────────────────────────────────────┘    │
│  ┌────────────────────────────────────────────────────┐    │
│  │  HPA (Auto-scaling)                                │    │
│  └────────────────────────────────────────────────────┘    │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Prometheus  │ │   Grafana    │ │  Application │
│  (Metrics)   │ │ (Dashboards) │ │   (Flask)    │
└──────────────┘ └──────────────┘ └──────────────┘
```

## Component Details

### Application Layer
- **Technology**: Python Flask
- **Web Server**: Gunicorn (4 workers)
- **Port**: 5000
- **Endpoints**: 
  - `/` - Homepage
  - `/health` - Health checks
  - `/api/info` - Application info
  - `/api/metrics` - Prometheus metrics

### Containerization
- **Base Image**: Python 3.11-slim
- **Build Strategy**: Multi-stage build
- **Security**: Non-root user
- **Size Optimization**: Minimal dependencies

### Orchestration
- **Local**: Docker Compose
- **Production**: Kubernetes
- **Scaling**: Horizontal Pod Autoscaler (HPA)
- **Replicas**: 3 (configurable)

### CI/CD Pipeline
1. **Linting**: Code quality checks
2. **Testing**: Automated unit tests
3. **Building**: Docker image creation
4. **Security**: Vulnerability scanning
5. **Deployment**: Automated to staging/production

### Infrastructure
- **IaC Tool**: Terraform
- **Cloud Provider**: AWS
- **Components**:
  - VPC with public/private subnets
  - Internet Gateway
  - Route Tables
  - (EKS ready for extension)

### Monitoring
- **Metrics Collection**: Prometheus
- **Visualization**: Grafana
- **Scraping**: Application metrics endpoint
- **Dashboards**: Pre-configured for application metrics

## Data Flow

1. **Development**: Developer pushes code to repository
2. **CI/CD**: GitHub Actions triggers pipeline
3. **Build**: Docker image is built and pushed to registry
4. **Deploy**: Kubernetes pulls image and deploys
5. **Monitor**: Prometheus scrapes metrics, Grafana visualizes
6. **Scale**: HPA adjusts replicas based on metrics

## Security Considerations

- Non-root containers
- Security scanning in CI/CD
- Resource limits in Kubernetes
- Health checks for reliability
- Secrets management (Kubernetes secrets)
- Network policies (can be added)

## Scalability

- Horizontal Pod Autoscaler (2-10 replicas)
- Based on CPU (70%) and Memory (80%) utilization
- Load balancing via Kubernetes Service
- Stateless application design

## High Availability

- Multiple replicas across nodes
- Health checks and auto-restart
- Load balancing
- Rolling updates with zero downtime

## Future Enhancements

- Add database layer (PostgreSQL/MySQL)
- Implement service mesh (Istio/Linkerd)
- Add distributed tracing (Jaeger)
- Implement blue-green deployments
- Add backup and disaster recovery
- Implement GitOps with ArgoCD/Flux

