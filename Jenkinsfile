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

                sh "touch ./pytest_result.xml"
                sh "ls -l ."
                sh "docker run --mount type=bind,source=./pytest_result.xml,target=/app/pytest_result.xml --entrypoint pytest python_app:${env.BUILD_NUMBER} ./src --junitxml=pytest_result.xml"
                sh "cat pytest_result.xml"
            }
        }
    }
}