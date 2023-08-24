pipeline {
    agent any

    stages {
        stage('SCM') {
            steps {
                echo 'SCM..'
            }
        }
        stage('SBOM') {
            steps {
                echo 'SBOM..'
                sh 'cyclonedx-gomod app -json=true  -output ./out.json src'
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