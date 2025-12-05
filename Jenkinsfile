pipeline {
    agent any

    environment {
        TRIVY = """C:\Users\admin\AppData\Local\Microsoft\WinGet\Packages\AquaSecurity.Trivy_Microsoft.Winget.Source_8wekyb3d8bbwe\trivy.exe"""   // <-- update this to your actual trivy.exe path
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
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
                bat '"%TRIVY%" fs . --exit-code 0 --severity HIGH,CRITICAL -o trivy_fs_report.txt'
            }
        }

        stage('Security Scan - Dependencies') {
            steps {
                bat '"%TRIVY%" fs --dependency-tree . -o trivy_deps_report.txt'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'trivy*.txt', fingerprint: true
            }
        }
    }
}
