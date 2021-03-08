
// Jenkinsfile (Declarative Pipeline)

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Notify Gitlab'
                updateGitlabCommitStatus name: 'build', state: 'pending'
                echo 'build step goes here'
                updateGitlabCommitStatus name: 'build', state: 'success'
            }
        }
    }
}

