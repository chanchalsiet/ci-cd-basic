pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                 git branch: 'main', url: 'https://github.com/chanchalsiet/ci-cd-basic.git'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 calculator.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pip install pytest'
                sh 'python3 -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'mkdir -p deploy && cp *.py deploy/'
            }
        }
    }
}
