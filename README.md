📘 Flask CI/CD Pipeline with GitHub Actions, Jenkins & Kubernetes

This project demonstrates a complete CI/CD pipeline for a Python Flask application using GitHub Actions, Docker, Jenkins, and Kubernetes (Minikube). It follows real-world DevOps practices including branching strategy, code reviews, automated testing, containerization, and Kubernetes deployment.

🚀 Project Overview
Stage	Tool	Purpose
Version Control	Git + GitHub	Branching, PR workflow, branch protection
Continuous Integration	GitHub Actions	Linting, testing, Docker image build
Containerization	Docker	Build and run application images
Orchestration	Kubernetes (Minikube)	Deployment, scaling, rollouts
Continuous Delivery	Jenkins	Auto-deploy on main branch updates
🧩 Flask Application

A simple Flask application located in app.py.

Run Application Locally
python app.py

Output
Hello, World!

🐳 Docker Setup
Build Docker Image
docker build -t flask-ci-cd-app .

Run Container
docker run -p 5000:5000 flask-ci-cd-app


Application URL:
http://localhost:5000

⚙️ Continuous Integration — GitHub Actions

CI workflow file: .github/workflows/ci.yml

Pipeline includes:

Set up Python environment

Install dependencies

Run flake8 linting (max line length: 90)

Run pytest unit tests

Build Docker image

CI ensures only clean, tested code gets merged.

☸️ Kubernetes Deployment (Minikube)

Kubernetes manifests are located in kubernetes/:

deployment.yaml

service.yaml

Deploy to Kubernetes
kubectl apply -f kubernetes/
kubectl get pods
kubectl get services

Rollback Deployment
kubectl rollout undo deployment/flask-app

🔁 Continuous Delivery — Jenkins Pipeline

The Jenkinsfile automates deployment whenever changes are pushed to the main branch.

Jenkins Pipeline Stages
1. Build Docker Image

Uses Minikube’s Docker environment.

2. Deploy to Kubernetes
kubectl apply -f kubernetes/

3. Verify Rollout

Ensures:

Deployment is updated

Pods are healthy

NodePort service is accessible

📦 Kubernetes Features Demonstrated

Zero-downtime rolling updates

Auto-rollback

Replication & scaling

NodePort load balancing

Scale Deployment
kubectl scale deployment flask-app --replicas=3

📁 Repository Structure
flask-k8s-ci-cd-assignment/
│ app.py
│ Dockerfile
│ Jenkinsfile
│ requirements.txt
│ README.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── kubernetes/
    ├── deployment.yaml
    └── service.yaml

👥 Team Workflow
Admin (Areeba)

Created repository

Set branch protection

Created issues & milestones

Reviewed and merged PRs

Set up Minikube & Jenkins

Developer (Sharjeel)

Developed Flask application

Implemented GitHub Actions CI

Wrote Dockerfile

Built Kubernetes manifests

Created Jenkins CD pipeline

Workflow followed:
Feature Branch → Pull Request → Code Review → Merge

✅ Final Outcome

This project successfully demonstrates an end-to-end CI/CD pipeline:

Automated linting & testing

Docker image creation

GitHub Actions CI

Jenkins → Kubernetes deployment

Rolling updates, scaling & rollback

Production-style pipeline from code → cluster
