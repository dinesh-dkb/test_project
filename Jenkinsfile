pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-python-app'
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/dinesh-dkb/test_project.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$DOCKER_TAG .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d --name my-app-container -p 5000:5000 $IMAGE_NAME:$DOCKER_TAG'
            }
        }
    }

    post {
        always {
            sh 'docker ps -a'
        }
    }
}