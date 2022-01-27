pipeline {
    agent {
        dockerfile true
    }
    stages{
        stage('Checkout repository') {
            steps{
                git branch: 'master',
                credentialsId: 'ilya1200',
                url: 'https://github.com/ilya1200/WorldOfGames.git'
            }
        }
        stage('Run App') {
            steps {
                sh 'pwd'
                sh 'ls -l'
                sh 'echo $HOME'
                sh 'python3 ./MainScores.py'
            }
        }
        stage('Test with E2E') {
            steps {
                sh 'python3 ./e2e.py'
            }
        }
    }
}