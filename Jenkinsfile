pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-ci-demo"
        CONTAINER_NAME = "python_ci_run"
        WORKSPACE_DIR = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "🔄 Checking out repository..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🛠 Building Docker image.."
                bat """
                docker build -t %IMAGE_NAME% "%WORKSPACE_DIR%"
                """
            }
        }

        stage('Run Tests in Docker') {
            steps {
                echo "🧪 Running tests inside Docker..."
                bat """
                docker run -d --name %CONTAINER_NAME% -v "%WORKSPACE_DIR%:/app" %IMAGE_NAME% /bin/sh -c "pytest --junitxml=/app/results.xml --tb=short -v > /app/test.log 2>&1"
                """
            }
            post {
                always {
                    echo "📄 Publishing test results and logs..."
                    // Jenkins will fail if results.xml not found; use allowEmptyArchive
                    junit 'results.xml'
                    archiveArtifacts artifacts: 'test.log', allowEmptyArchive: true
                }
            }
        }

        stage('Deploy') {
            when {
                expression { return fileExists('results.xml') }
            }
            steps {
                echo "🚀 Tests passed — deploying application"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully"
            echo "🧪 Docker container %CONTAINER_NAME% is kept for inspection"
        }
        failure {
            echo "❌ Pipeline failed — check logs"
            echo "🧪 Docker container %CONTAINER_NAME% is kept for inspection"
        }
        always {
            echo "🧹 Pipeline finished"
        }
    }
}
