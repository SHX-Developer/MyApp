//  NAME:  SHAKHRIZOD
//  FILE:  Main jenkinsfile - Jenkins Pipelines
//  REQUIREMENTS:  Jenkins


pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SHX-Developer/MyApp.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run myapp pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 myapp'
            }
        }
    }
}
