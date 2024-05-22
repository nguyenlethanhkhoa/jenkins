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
                echo " ------------------------- Build python_app:${env.BUILD_NUMBER} --------------------------- "
                sh "docker build -t python_app:${env.BUILD_NUMBER} app"
            }
        }

        stage('Test PR') {
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
                echo " ------------------------- Test python_app:${env.BUILD_NUMBER} --------------------------- "

                sh "docker run -v ./test_result:/app/test_result --entrypoint pytest python_app:${env.BUILD_NUMBER} ./src --junitxml=./test_result/unittest.xml"
                junit 'test_result/unittest.xml'
            }
        }
    }
}