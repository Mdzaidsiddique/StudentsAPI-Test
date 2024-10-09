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
                bat 'behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features/'
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
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
