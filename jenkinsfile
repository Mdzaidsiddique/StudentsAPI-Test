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
            archiveArtifacts artifacts: 'reports/*.xml', allowEmptyArchive: true
        }
    }
}
