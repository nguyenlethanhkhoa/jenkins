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
                echo ' ------------------------- Build Stage --------------------------- '

                sh "./build.sh"
                // script {
                //     def image = docker.build("python_app:${env.BUILD_ID}")
                //     image.push()
                // }
            }
        }
    }
}