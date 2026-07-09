pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-final-project"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_PASS'
                    )]) {
                        sh '''
                            DOCKER_BUILDKIT=0 docker build --network=host -t $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER .
                            docker tag $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER $DOCKERHUB_USER/$IMAGE_NAME:latest
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_PASS'
                    )]) {
                        sh '''
                            echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin
                            docker push $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER
                            docker push $DOCKERHUB_USER/$IMAGE_NAME:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_PASS'
                    )]) {
                        sh '''
                            for NS in dev qa staging prod; do
                                kubectl create namespace $NS --dry-run=client -o yaml | kubectl apply -f -

                                sed "s|IMAGE_PLACEHOLDER|$DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER|g; s|ENV_PLACEHOLDER|$NS|g" k8s/deployment.yaml | kubectl -n $NS apply -f -

                                kubectl -n $NS apply -f k8s/service.yaml
                                kubectl -n $NS rollout status deployment/jenkins-final-app --timeout=300s
                            done
                        '''
                    }
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl get pods -n dev
                    kubectl get pods -n qa
                    kubectl get pods -n staging
                    kubectl get pods -n prod
                    kubectl get services -n prod
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
