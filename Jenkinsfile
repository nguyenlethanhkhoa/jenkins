pipeline {
    agent any

    stages {
        stage('Build PR') {
            agent any
            when {
                beforeAgent true
                
                expression {
                    isDevelop = env.CHANGE_TARGET == 'develop'
                    isPullRequest = env.BRANCH_NAME ==~ /PR-.*/

                    echo "isDevelop : ${isDevelop} , isPullRequest : ${isPullRequest}"

                    return isDevelop && isPullRequest
                }
            }
            steps {
                echo ' -------------------------Build Stage --------------------------- '
                
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./build.sh"
            }
        }
    }
}