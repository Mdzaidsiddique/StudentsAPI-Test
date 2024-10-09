pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                bat 'behave'
            }
        }
    }
    post {
        always{
            bat 'allure generate allure-results --clean -o allure-report'
        }
        always {
            echo 'Archiving Allure results...'
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
