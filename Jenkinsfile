pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-repo/student-feedback.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t feedback-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 5000:5000 feedback-app'
            }
        }
    }
}