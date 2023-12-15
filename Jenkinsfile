pipeline {
    agent any

    stages {
        stage('Authorize Microservice') {
            when {
                branch 'authorize_microservice_v*'
            }
            steps {
                dir('authorize') {
                    sh 'docker-compose build'
                    sh 'docker-compose up -d'
                }
            }
        }
        stage('Business Microservice') {
            when {
                branch 'business_microservice_v*'
            }
            steps {
                dir('business') {
                    sh 'docker-compose build'
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
