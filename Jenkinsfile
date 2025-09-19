pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                // Clones your Flask repository code.
                git branch: 'main', url: 'https://github.com/sarthak20052005/simple_python_web_app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installs Flask and pytest from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                // Runs the tests defined in test_app.py
                sh 'pytest'
            }
        }
    }
}
