pipeline {
    agent any
    // agent {
    //     docker {
    //         image 'axidex/devsecops:latest'
    //     }
    // }
    environment {
        PATH="/opt/homebrew/bin/:${env.PATH}"
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