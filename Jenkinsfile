pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-ci-demo"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image with Python + dependencies
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests inside Docker container
                bat "docker run --rm -v %WORKSPACE%:/app %IMAGE_NAME% pytest --junitxml=/app/results.xml"
            }
            post {
                always {
                    // Publish test reports in Jenkins
                    junit 'results.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "🚀 Tests passed — deploying application"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed — check logs"
        }
        always {
            echo "🧹 Cleaning up Docker image"
            bat "docker image rm -f %IMAGE_NAME% || exit 0"
        }
    }
}
