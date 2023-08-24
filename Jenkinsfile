pipeline {
    agent none

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
                sh 'wget https://github.com/CycloneDX/cyclonedx-gomod/releases/download/v1.4.1/cyclonedx-gomod_1.4.1_linux_amd64.tar.gz'
                sh 'tar -xvzf cyclonedx-gomod_1.4.1_linux_amd64.tar.gz'
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