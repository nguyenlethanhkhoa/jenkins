pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            // when {
            //     beforeAgent true
                
            // }
            steps {
                echo ' -------------------------Build Stage --------------------------- '
                
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./build.sh"

                script {
                    isDevelop = env.CHANGE_TARGET == 'develop'
                    isPullRequest = (env.BRANCH_NAME =~ /PR-.*/)

                    echo "isDevelop : ${isDevelop} , isPullRequest : ${isPullRequest}"
                }

                // expression {
                //     isDevelop = env.CHANGE_TARGET == 'develop'
                //     isPullRequest = env.BRANCH_NAME =~ /PR-.*/

                //     echo "isDevelop : ${isDevelop} , isPullRequest : ${isPullRequest}"
                // }
            }
        }
    }
}