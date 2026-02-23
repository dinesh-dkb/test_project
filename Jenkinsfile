pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("vehicle-telematics:latest")
                }
            }
        }

        stage('Deploy to Host') {
            steps {
                script {
                    // Use docker CLI on the host via mounted socket
                    sh """
                    docker run -d --name vehicle-telematics \
                      --env AWS_ACCESS_KEY_ID=test \
                      --env AWS_SECRET_ACCESS_KEY=test \
                      --env AWS_DEFAULT_REGION=us-east-1 \
                      --network=host \
                      vehicle-telematics:latest
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}