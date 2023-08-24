pipeline {
    agent none
    stages {
        stage('SCM') {
            steps {
                agent {
                    docker {
                        image 'axidex/devsecops:latest'
                    }
                }
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