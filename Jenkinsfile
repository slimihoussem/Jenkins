pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-ci-demo"
        CONTAINER_NAME = "python_ci_run_${env.BUILD_NUMBER}" // unique container name per build
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
                bat """
                docker build -t %IMAGE_NAME% .
                """
            }
        }

        stage('Run Tests in Docker') {
            steps {
                echo "🧪 Running tests inside Docker..."
                bat """
                docker run -d --name %CONTAINER_NAME% -v "%CD%:/app" %IMAGE_NAME% ^
                cmd /c "pytest --junitxml=/app/results.xml --tb=short -v > /app/test.log 2>&1"
                """
            }
            post {
                always {
                    echo "📄 Publishing test results and logs..."
                    junit 'results.xml'
                    archiveArtifacts artifacts: 'test.log', allowEmptyArchive: true
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "🚀 Tests passed — deploy step can go here"
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
            echo "🧹 Pipeline finished. Container %CONTAINER_NAME% is kept for inspection."
        }
    }
}
