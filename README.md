# Flask CI/CD Pipeline with Kubernetes & Jenkins

This project implements a complete **CI/CD pipeline** for a Python Flask application using:

- **GitHub + GitHub Actions** (Continuous Integration)
- **Docker** (Containerization)
- **Kubernetes (Minikube)** (Deployment)
- **Jenkins** (Continuous Delivery)
- **Branch Protection + Pull Requests** (Team workflow)

This assignment follows a real industry CI/CD workflow using Admin + Developer roles.

---

## 🚀 Project Features

### **1. Flask Application**

A simple Python Flask app running on port 5000:

- Route `/` returns **"Hello, World!"**

---

## 🐳 Docker Setup

To build and run locally:

```bash
docker build -t flask-ci-app .
docker run -p 5000:5000 flask-ci-app
```
