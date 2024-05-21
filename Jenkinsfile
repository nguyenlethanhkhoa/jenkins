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
                echo ' ------------------------- Build Docker Image --------------------------- '

                sh "docker build -t python_app:${env.CHANGE_ID} -f src/Dockerfile"

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
                echo ' ------------------------- Build Docker Image --------------------------- '

                sh "docker run --entrypoint pytest /src --junitxml=./test_result.xml python_app:${env.CHANGE_ID}"
            }
        }
    }
}