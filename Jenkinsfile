pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo ' -------------------------Build Stage --------------------------- '
                echo 'GITHUB_PR_STATE' env.GITHUB_PR_STATE
                echo 'GITHUB_PR_TARGET_BRANCH' env.GITHUB_PR_TARGET_BRANCH
                echo 'GITHUB_PR_SOURCE_BRANCH' env.GITHUB_PR_SOURCE_BRANCH

                echo 'BRANCH_NAME' env.BRANCH_NAME
                echo 'BRANCH_IS_PRIMARY' env.BRANCH_IS_PRIMARY
                echo 'CHANGE_ID' env.CHANGE_ID
                echo 'CHANGE_URL' env.CHANGE_URL
                echo 'CHANGE_TITLE' env.CHANGE_TITLE
                echo 'CHANGE_AUTHOR' env.CHANGE_AUTHOR
                echo 'CHANGE_AUTHOR_DISPLAY_NAME' env.CHANGE_AUTHOR_DISPLAY_NAME
                echo 'CHANGE_AUTHOR_EMAIL' env.CHANGE_AUTHOR_EMAIL
                echo 'CHANGE_TARGET' env.CHANGE_TARGET
                echo 'CHANGE_BRANCH' env.CHANGE_BRANCH

            }
        }
    }
}