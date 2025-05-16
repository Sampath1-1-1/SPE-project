pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DockerHubCred') // ID from Jenkins credentials
        DOCKERHUB_USERNAME = '<sampath333>'     // Your Docker Hub username
        GIT_REPO_URL = '<https://github.com/Sampath1-1-1/SPE_Project.git>'              // Your GitHub repo URL
        EMAIL_RECIPIENT = '<sampathkumar1011c@gmail.com>'                     // Your email for notifications
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                git url: "${GIT_REPO_URL}", branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests...'
                dir('tests') {
                    sh 'python3 test_app.py'
                }
            }
        }

        stage('Build and Push Docker Images') {
            steps {
                echo 'Building Docker images...'
                // Build frontend image
                dir('frontend') {
                    sh 'docker build -t ${DOCKERHUB_USERNAME}/frontend:latest .'
                }
                // Build middleware image
                dir('venv') {
                    sh 'docker build -t ${DOCKERHUB_USERNAME}/middleware:latest .'
                }
                // Build model-service image
                dir('Model-service') {
                    sh 'docker build -t ${DOCKERHUB_USERNAME}/model-service:latest .'
                }

                echo 'Logging into Docker Hub...'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_USERNAME --password-stdin'

                echo 'Pushing Docker images to Docker Hub...'
                sh 'docker push ${DOCKERHUB_USERNAME}/frontend:latest'
                sh 'docker push ${DOCKERHUB_USERNAME}/middleware:latest'
                sh 'docker push ${DOCKERHUB_USERNAME}/model-service:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes using Ansible...'
                dir('ansible') {
                    sh 'ansible-playbook -i inventory.yml deploy.yml'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Jenkins Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} completed successfully.\nCheck the build at ${env.BUILD_URL}"
        }
        failure {
            echo 'Pipeline failed!'
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Jenkins Pipeline Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} failed.\nCheck the build at ${env.BUILD_URL}"
        }
        always {
            echo 'Cleaning up Docker images to free space...'
            sh 'docker rmi ${DOCKERHUB_USERNAME}/frontend:latest || true'
            sh 'docker rmi ${DOCKERHUB_USERNAME}/middleware:latest || true'
            sh 'docker rmi ${DOCKERHUB_USERNAME}/model-service:latest || true'
        }
    }
}