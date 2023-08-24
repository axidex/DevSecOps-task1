pipeline {
    //agent any
    environment {
        PATH="/opt/homebrew/bin/:/usr/local/go/bin/:/usr/local/bin/:${env.PATH}"
    }

    agent {
        docker {
            image 'axidex/devsecops:latest'
        }
    }
    stages {
        stage('SCM') {
            steps {
                echo 'SCM..'
                sh 'rm -rf govwa'
                sh 'git clone https://github.com/0c34/govwa.git'
                sh 'rm -rf src'
                sh 'mv govwa src'
            }
        }
        stage('SBOM') {
            steps {
                echo 'SBOM..'
                sh 'echo $PATH'
                sh '/opt/homebrew/bin/cyclonedx-gomod app -json=true -output ./out.json src'
            }
        }
        stage('SCA') {
            steps {
                echo 'SCA....'
                
            }
        }
        stage('Results') {
            steps {
                echo 'Results.....'
            }
        }
    }
}