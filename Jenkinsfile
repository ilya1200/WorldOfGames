pipeline {
    agent { label 'agent_1' }

    stages {
        stage('Checkout repository'){
            steps{
                git branch: 'level_4',
                url: 'ssh:git@github.com:ilya1200/WorldOfGames.git'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Run app') {
            agent {
                docker {
                    image 'mainscore'
                    reuseNode true
                }
            }
            steps {
                // sleep 20
                sh 'python /app/flask_app.py &'
                sh 'curl 127.0.0.1:80'
            }
        }

        stage('Run app') {
            sh 'python ./MainScores.py'
        }

        stage('Test with E2E') {
            steps {
                sh 'python ./e2e.py'
            }
        }
    }
}