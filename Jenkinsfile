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
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                bat '''
                python -m pytest
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
