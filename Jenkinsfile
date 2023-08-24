pipeline {
    agent {
        docker {
            image 'axidex/devsecops:latest'
        }
    }
    stages {
        stage('SCM') {
            steps {
                echo 'SCM..'
                sh 'git clone https://github.com/0c34/govwa.git'
                sh 'mv govwa src'
            }
        }
        stage('SBOM') {
            steps {
                echo 'SBOM..'
                sh './cyclonedx-gomod app -json=true  -output ./out.json src'
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