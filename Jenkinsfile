pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/python-ci-demo.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python -m venv ${VENV}'
                sh '''
                source ${VENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source ${VENV}/bin/activate
                pytest tests/ --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh '''
                echo "Deployment step: Your Python app is ready!"
                # Example: python deploy.py
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up"
            sh 'rm -rf ${VENV}'
        }
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
