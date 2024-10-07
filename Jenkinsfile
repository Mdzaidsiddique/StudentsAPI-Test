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
        // always {
        //     archiveArtifacts artifacts: 'reports/*.xml', allowEmptyArchive: true
        // }
        always {
            echo 'Cleaning up workspace'
            cleanWs()
            echo 'Archiving Allure reports...'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
