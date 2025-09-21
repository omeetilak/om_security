pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Replace with your repo URL
                git branch: 'main', url: 'https://github.com/sarthak20052005/simple_python_web_app.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest -q'
            }
        }
    }
}
