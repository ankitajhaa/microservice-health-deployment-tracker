# Microservice Health and Deployment Tracker

A production-style backend platform to track internal microservices, deployments, environments, incidents, and reliability metrics.  

This project mirrors real engineering tools used in DevOps and Site Reliability Engineering (SRE) teams.

---

## 🚀 Tech Stack

- Django  
- Django REST Framework  
- MySQL  
- DRF Spectacular (Swagger / OpenAPI)  
- Docker & Docker Compose  
- Token Authentication  

---

## ✨ Features

- Service registry  
- Environment tracking (DEV / STAGING / PROD)  
- Deployment logging  
- Incident management & resolution workflow  
- Status history audit trail  
- Reliability metrics (MTTR, failure rate, instability ranking)  
- Secure token-based authentication  
- Automated tests  

---

## ⚙️ Setup & Run Instructions

### 1. Clone repository
```bash
git clone <https://github.com/ankitajhaa/microservice-health-deployment-tracker>
cd <microservice-health-deployment-tracker>

### 2. Build containers
docker compose build

### 3. Start the application
docker compose up

### 4. Run database migrations
docker compose run --rm app python manage.py migrate

### 5. Create a superuser
docker compose run --rm app python manage.py createsuperuser

## Authentication
All APIs require authentication.

### 1. Obtain token
POST /api/token/

### 2. Use token in header
Authorization: Token <your_token>

## Main API Endpoints

/api/services/
/api/environments/
/api/deployments/
/api/incidents/
/api/incidents/{id}/resolve/
/api/metrics/

## Reliability Metrics

- Deployment frequency
- Incident count per service
- Mean Time To Recovery (MTTR)
- Deployment failure rate
- Most unstable service

## API Documentation

### OpenAPI schema
/api/schema/

### Swagger UI
/api/docs/

## Run Tests
docker compose run --rm app python manage.py test

