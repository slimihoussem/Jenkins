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
                C:\\Users\\Houssem\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest
                """
            }
        }

        stage('Deploy') {
            steps {
                echo "Tests passed ✅ Deploying application..."
            }
        }
    }
}
