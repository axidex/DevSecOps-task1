pipeline {
    agent any
    environment {
        PATH="/opt/homebrew/bin/:/usr/local/go/bin/:/usr/local/bin/:${env.PATH}"
    }

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
                // https://github.com/CycloneDX/cyclonedx-gomod
                sh 'echo $PATH'
                sh '/opt/homebrew/bin/cyclonedx-gomod app -output ./bom.xml src'
            }
        }
        stage('SCA') {
            steps {
                echo 'SCA..'
                // https://www.jenkins.io/doc/pipeline/steps/dependency-track/
                dependencyTrackPublisher artifact: 'sbom', projectName: 'tmp', projectVersion: '0.1', synchronous: true, autoCreateProjects: true, failedTotalCritical: 0, failedTotalHigh: 1, failedTotalMedium: 2
            }
        }
        stage('Results') {
            steps {
                echo 'Results..'
                // docker cp container_id:path path
                sh 'docker cp a6c78433e9faf908b2bdd7eddc2a9f7724c258828af53f97c6611c336f104cc8:/data/.dependency-track/dependency-track.log /Users/axidex/.jenkins/workspace/pipe1/dependency-track.log'
                sh 'cat dependency-track.log'
            }
        }
    }
}