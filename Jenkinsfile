pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                // Run Behave tests and generate allure results
                bat 'behave -f allure_behave.formatter:AllureFormatter -o allure-results features/'
            }
        }
    }
    post {
        always {
            // Check if allure-results directory exists
            echo 'Checking Allure results...'
            bat 'if exist allure-results (echo Allure results found) else (echo No Allure results found)'

            // Generate the Allure report
            echo 'Generating Allure report...'
            bat 'allure generate allure-results --clean -o allure-report'
            
            // Archive the allure-results and allure-report
            echo 'Archiving Allure results and report...'
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
        }
        success {
            echo 'Build succeeded, tests passed!'
        }
        failure {
            echo 'Build failed, please check the logs.'
        }
    }
}
