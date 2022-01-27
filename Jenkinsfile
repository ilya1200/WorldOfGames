pipeline {
    agent {
        dockerfile true
    }
    stages{
        stage('ls') {
            steps{
                 sh 'ls -l'
            }
        }
        stage('Checkout repository') {
            steps{
                git branch: 'master',
                credentialsId: 'ilya1200',
                url: 'https://github.com/ilya1200/WorldOfGame.git'
            }
        }
        stage('Run App') {
            steps {
                sh 'python ./MainScores.py'
            }
        }
        stage('Test with E2E') {
            steps {
                sh 'python ./e2e.py'
            }
        }
    }
}