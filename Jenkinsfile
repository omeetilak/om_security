pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/omeetilak/om_security.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                // Windows cannot run flake8 directly through sh, so use bat
                bat 'flake8 . || ver > nul'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Security Scan - Filesystem') {
            steps {
                bat 'trivy fs . --exit-code 0 --severity HIGH,CRITICAL -o trivy_fs_report.txt'
            }
        }

        stage('Security Scan - Dependencies') {
            steps {
                bat 'trivy fs --dependency-tree . -o trivy_deps_report.txt'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'trivy*.txt', fingerprint: true
            }
        }
    }
}
