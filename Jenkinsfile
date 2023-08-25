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
                sh '/opt/homebrew/bin/cyclonedx-gomod app -output ./bom.xml src'
            }
        }
        stage('SCA') {
            steps {
                echo 'SCA..'
                // https://www.jenkins.io/doc/pipeline/steps/dependency-track/
                dependencyTrackPublisher artifact: 'sbom', projectName: 'tmp', projectVersion: '0.1', synchronous: true, autoCreateProjects: true, failedTotalCritical: 1, failedTotalHigh: 10, failedTotalMedium: 20
                
                sh '''
                curl -X 'GET' \
                'http://localhost:8081/api/v1/metrics/project/e561948b-93e1-4f86-8c04-1f10560df992/current' \
                -H 'accept: application/json' \
                -H 'X-Api-Key: TimbOxMatBj7kSlCEq9KYJUoY70AsWmK' -o vuln.log
                    '''
                sh 'cat vuln.log'
            }
        }
        stage('Results') {
            steps {
                echo 'Results..'
                // docker cp container_id:path path. If u need tech logs from dependency-tracker in ur jenkins cli
                //sh 'docker cp a6c78433e9faf908b2bdd7eddc2a9f7724c258828af53f97c6611c336f104cc8:/data/.dependency-track/dependency-track.log /Users/axidex/.jenkins/workspace/pipe1/dependency-track.log'
                //sh 'cat dependency-track.log'


            }
        }
    }
}