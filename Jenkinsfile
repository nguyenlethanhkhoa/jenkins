pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo ' -------------------------Build Stage --------------------------- '
                
                sh("./build.sh")
            }
        }
    }
}