pipeline {
    agent any
    // agent {
    //     docker {
    //         image 'axidex/devsecops:latest'
    //     }
    // }
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
                sh '/opt/homebrew/bin/wget cyclonedx-gomod_1.4.0_linux_arm64.tar.gz'
                sh '/usr/bin/tar -xvzf cyclonedx-gomod_1.4.0_linux_arm64.tar.gz'
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