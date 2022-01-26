pipeline {
    agent {
        dockerfile true
    }
    stage('Checkout repository') {
        steps{
            git branch: 'level_4',
            url: 'ssh:git@github.com:ilya1200/WorldOfGames.git'
        }
    }
    stage('Run Flask') {
        steps {
            sh 'python /app/flask_app.py &'
            sh 'curl 127.0.0.1:80'
        }
    }
    stage('Run app') {
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