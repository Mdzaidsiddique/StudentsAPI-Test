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
                // '-f allure_behave.formatter:AllureFormatter -o allure-results/ features/'
            }
        }
    }
    post {
        always {
            echo 'Generating Allure report...'
            bat 'allure generate allure-results --clean -o allure-report'
            echo 'Archiving Allure results and report...'
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
            // archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
