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
        always {
            echo 'Checking Allure results...'
            bat 'dir allure-results' // Check if the results directory exists
            
            echo 'Generating Allure report...'
            bat 'allure generate allure-results --clean -o allure-report'
            
            echo 'Archiving Allure results...'
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true // Archive the generated report as well
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
