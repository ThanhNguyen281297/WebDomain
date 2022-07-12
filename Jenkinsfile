pipeline {
    agent {
        label 'DockerNode'
    }
    stages {
        stage('Start minikube') {
            steps {
                sh 'minikube start'
            }
        }
    }
}