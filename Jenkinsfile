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
                sh 'kubectl apply -k ./'
            }
        }
        stage('Run Web WP') {
            steps {
                sh "kubectl port-forward service/wordpress 8080:80 --address='0.0.0.0'"
            }
        }
    }   
}