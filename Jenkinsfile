pipeline {
    agent any 
    stages {
        stage('Clone') { 
            steps {
                git 'https://github.com/pala3105/test-flask.git' 
            }
        }
        stage('Test') { 
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python app.py & sleep 5; pkill -f app.py'
            }
        }
        stage('Deploy') { 
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    sh 'git config --global user.email "jenkins@jenkins.com"'
                    sh 'git config --global user.name "jenkins"'
                    sh 'git add . '
                    sh 'git commit -m "Pipeline Commit"'
                    sh 'git push origin master'
            }
        }
    }