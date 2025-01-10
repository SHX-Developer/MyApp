//  NAME:  SHAKHRIZOD
//  FILE:  Main jenkinsfile - Jenkins Pipelines
//  REQUIREMENTS:  Jenkins


pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SHX-Developer/MyApp.git',
                    credentialsId: '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'
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
