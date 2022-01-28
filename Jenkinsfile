pipeline {
    agent {
        dockerfile true
    }
    stages{
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