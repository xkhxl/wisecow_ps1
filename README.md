# Wisecow Application – Kubernetes Deployment with TLS & CI/CD
## Overview
Wisecow is a simple web application that serves "cow wisdom" quotes. This project demonstrates the **containerization, Kubernetes deployment, secure TLS communication, and CI/CD automation** using GitHub Actions.
## Project Objective
- Containerize the Wisecow application using Docker.
- Deploy it on a Kubernetes environment (Minikube or other clusters).
- Expose the application securely via Kubernetes Ingress with TLS.
- Automate build and deployment via GitHub Actions.
## Prerequisites
- **Local development / testing:**  
  - Docker  
  - Minikube (or other Kubernetes cluster)  
  - kubectl  
- **GitHub repository secrets:**  
  - `DOCKER_USERNAME` – Docker Hub username  
  - `DOCKER_PASSWORD` – Docker Hub password  
  - `KUBECONFIG` – Base64 encoded kubeconfig for your cluster (for CI/CD)  
- Install required utilities for local testing: `sudo apt install fortune-mod cowsay -y`
## Local Deployment
Start Minikube (if using locally): `minikube start`  
Enable ingress: `minikube addons enable ingress`  
Create TLS secret (if not already created): `kubectl create secret tls wisecow-tls --cert=k8s/certs/tls.crt --key=k8s/certs/tls.key`  
Deploy Wisecow application: `kubectl apply -f k8s/wisecow-deployment.yaml && kubectl apply -f k8s/wisecow-service.yaml && kubectl apply -f k8s/wisecow-ingress.yaml && kubectl rollout status deployment/wisecow-deployment`  
Test the deployment: `sudo --preserve-env=HOME minikube tunnel` and then `curl -k https://wisecow.local`
## GitHub Actions CI/CD
The workflow `.github/workflows/docker-build.yml` performs:
- Checkout code on push to main.
- Build the Docker image.
- Push the image to Docker Hub.
- Deploy the updated application to the Kubernetes cluster using kubectl.
Secrets required:
- `DOCKER_USERNAME` – Docker Hub username
- `DOCKER_PASSWORD` – Docker Hub password
- `KUBECONFIG` – Base64 encoded kubeconfig
Workflow triggers:
- On push to main branch.
## Access the Application
- Host: https://wisecow.local
- Port: 443 (HTTPS, TLS-secured)
- Note: Add `127.0.0.1 wisecow.local` to your `/etc/hosts` if testing locally.
## Validation
Check the resources after deployment: `kubectl get pods && kubectl get svc && kubectl get ingress && kubectl logs -f deployment/wisecow-deployment`  
You should see:
- Pods running
- NodePort service exposing port 4499
- Ingress serving traffic with TLS
- Logs showing HTTP GET requests
## Problem Statement 2 - Log File Analyzer & Application Health Checker
This folder contains solutions for Problem Statement 2 of the assignment. It includes two scripts:

Log File Analyzer (log_analyzer.py)

- Analyzes web server logs (access.log) for common patterns.
- Reports:
  - Total requests
  - Number of 404 errors
  - Top 10 requested pages
  - Top 10 IP addresses
- Usage:
  python3 problem_statement_2/log_analyzer.py
- Make sure access.log is present in the problem_statement_2 folder or update the LOG_FILE path in the script.

Application Health Checker (app_health_checker.py)

- Checks if a web application is up by sending an HTTP request.
- Reports [UP] if the application is responding with status code 200, otherwise [DOWN].
- Usage:
  python3 problem_statement_2/app_health_checker.py
- Update the URL variable in the script with the target application's URL.

Notes:

- Both scripts are written in Python 3.
- requests library is required for app_health_checker.py (pip install requests).
- Tested on Linux.

