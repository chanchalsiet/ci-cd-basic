pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/chanchalsiet/ci-cd-basic.git'
            }
        }

        stage('Run App') {
            steps {
                sh 'python calculator.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install pytest && pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'mkdir -p deploy && cp *.py deploy/'
            }
        }
    }
}
