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
                echo "🛠 Building Docker image..."
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running tests inside Docker..."
                // Mount Jenkins workspace to /app inside container
                bat """
                docker run --rm -v %WORKSPACE%:/app %IMAGE_NAME% \
                pytest --junitxml=/app/results.xml --tb=short -v > /app/test.log 2>&1
                """
            }
            post {
                always {
                    echo "📄 Publishing test results and logs..."
                    // Publish JUnit XML results
                    junit 'results.xml'

                    // Archive full test log for review
                    archiveArtifacts artifacts: 'test.log', allowEmptyArchive: true
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
            echo "🧹 Cleaning up Docker image..."
            bat "docker image rm -f %IMAGE_NAME% || exit 0"
        }
    }
}
