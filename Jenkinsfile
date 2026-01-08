pipeline {
    agent any

    stages {

        stage('Install dependencies') {
            steps {
                bat """
                C:\\Users\\Houssem\\AppData\\Local\\Programs\\Python\\Python313\\python.exe --version
                C:\\Users\\Houssem\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install --upgrade pip
                C:\\Users\\Houssem\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install -r requirements.txt
                """
            }
        }

        stage('Run tests') {
            steps {
                bat """
                C:\\Users\\Houssem\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest --junitxml=results.xml
                """
            }
            post {
                always {
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
            echo "🧹 Pipeline finished"
        }
    }
}
