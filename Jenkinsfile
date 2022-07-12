pipeline {
    agent {
        label 'DockerNode'
    }
    stages {
        stage('Clone code') {
            steps {
                git branch: 'main', url: 'https://github.com/ThanhNguyen281297/TestDeploy.git' 
            }
        }
        stage('Start minikube') {
            steps {
                sh 'minikube start' 
            }
        }
    }   
}