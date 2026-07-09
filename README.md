# Jenkins CI/CD Final Project

This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, DockerHub, GitHub, and Kubernetes.

## Project Objective

The objective of this project is to automate the software delivery process.

The pipeline automatically:

1. Pulls the source code from GitHub
2. Builds a Docker image
3. Pushes the image to DockerHub
4. Deploys the application to Kubernetes
5. Verifies that the application is running successfully

## Technologies Used

- Jenkins
- GitHub
- Docker
- DockerHub
- Kubernetes / k3s
- Nginx
- Ubuntu 24.04 VM

## GitHub Repository

Repository URL:

https://github.com/ozkoc/jenkins-final-project

## DockerHub Repository

DockerHub image:

makifist/jenkins-final-project

Created image tags:

- latest
- 3
- 1

## Application

The application is a lightweight static web application served by Nginx.

Application response:

Jenkins CI/CD Final Project

Status: Running successfully

Deployed with Jenkins, Docker and Kubernetes

## Project Structure

jenkins-final-project/
├── Dockerfile
├── Jenkinsfile
├── README.md
├── index.html
└── k8s/
    ├── deployment.yaml
    └── service.yaml

## Jenkins Pipeline

The Jenkins pipeline is defined in the Jenkinsfile.

Pipeline stages:

1. Declarative Checkout SCM
2. Checkout
3. Build Docker Image
4. Push Docker Image
5. Deploy to Kubernetes
6. Verify Deployment
7. Post Actions

## Docker Build and Push

Jenkins builds the Docker image and pushes it to DockerHub.

Example image:

makifist/jenkins-final-project:3

The latest successful build also updates the latest tag.

## Kubernetes Deployment

The application is deployed to four Kubernetes namespaces:

- dev
- qa
- staging
- prod

Each namespace contains the Jenkins final application deployment:

jenkins-final-app

The service name is:

jenkins-final-service

## Verification Commands

Pods were verified with:

kubectl get pods -n dev
kubectl get pods -n qa
kubectl get pods -n staging
kubectl get pods -n prod

Deployments were verified with:

kubectl get deployments -n dev
kubectl get deployments -n qa
kubectl get deployments -n staging
kubectl get deployments -n prod

The application was tested using port-forwarding:

kubectl -n prod port-forward svc/jenkins-final-service 8081:80

curl http://localhost:8081

The curl command returned the application HTML successfully.

## Troubleshooting

During the first deployment attempt, Kubernetes rollout failed because the VM was very slow and the rollout timed out.

To solve this issue:

- The application was changed to a lightweight Nginx-based image
- The deployment was reduced to one replica
- The Jenkins pipeline was executed again
- Build #3 completed successfully

## Final Result

The final Jenkins pipeline completed successfully.

Docker image was pushed to DockerHub.

The application was deployed successfully to Kubernetes namespaces:

- dev
- qa
- staging
- prod

The application was tested successfully with curl.
