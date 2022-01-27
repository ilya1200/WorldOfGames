pipeline {
    agent "worker-172.18.0.2-a5c8131e"
    stages{
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