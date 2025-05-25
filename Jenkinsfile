pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "tusuario/reto-final-python"
    }

    stages {
        stage('Clonar código') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Linting') {
            steps {
                sh 'flake8 app tests'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --cov=app --cov-report=term-missing'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker image') {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                    branch 'develop'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }
    }
}
