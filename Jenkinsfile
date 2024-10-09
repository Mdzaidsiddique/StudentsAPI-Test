pipeline {
    agent any
    stages {
        // stage('Checkout') {
        //     steps {
        //         // Checkout the code from the repository
        //         git 'https://github.com/Mdzaidsiddique/StudentsAPI-Test.git'
        //     }
        // }
        stage('Install Dependencies') {
            steps {
                // Install the required Python packages
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                // Run the Behave tests and generate Allure results
                bat 'behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features/'
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Generate the Allure report from the results
                echo 'Generating Allure report...'
                bat 'allure generate allure-results --clean -o allure-report'
            }
        }
    }
    post {
        always {
            // Clean up the workspace and archive the results
            echo 'Cleaning up workspace...'
            cleanWs()
            echo 'Archiving Allure results...'
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
