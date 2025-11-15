pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t flask-app-ci .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                sh '''
                    kubectl apply -f kubernetes/deployment.yaml
                    kubectl apply -f kubernetes/service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Verifying Kubernetes deployment..."
                sh '''
                    kubectl rollout status deployment/flask-app
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
    }
}
