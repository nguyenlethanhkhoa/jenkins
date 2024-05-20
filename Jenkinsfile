pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo ' -------------------------Build Stage --------------------------- '
                
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./build.sh"
            }
        }
    }
}