pipeline {
    agent { dockerfile true }

    stages {
        stage('Build PR') {
            agent {
                dockerfile {
                    filename 'src/Dockerfile'
                }
            }

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

                script {
                    def customImage = docker.build("my-image:${env.BUILD_ID}")
                    customImage.push()
                }
            }
        }
    }
}