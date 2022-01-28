pipeline {
    agent {
        dockerfile true
    }
    stages{
        stage('Checkout repository') {
            steps{
                git branch: 'level_4',
                credentialsId: 'ilya1200',
                url: 'https://github.com/ilya1200/WorldOfGames.git'
            }
        }
        stage('Run App') {
            steps {
                sh 'python3 ./MainScores.py &'
            }
        }
        stage('Test with E2E') {
            steps {
                sh 'python3 ./tests/e2e.py'
            }
        }
    }
}