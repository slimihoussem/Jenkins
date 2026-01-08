pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/slimihoussem/Jenkins.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                bat '''
                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Tests passed ✅ Deploying application..."
            }
        }
    }
}
