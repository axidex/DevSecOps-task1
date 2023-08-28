// Another port for jenkins
// /opt/homebrew/opt/openjdk@17/bin/java -Dmail.smtp.starttls.enable\=true -jar /opt/homebrew/opt/jenkins-lts/libexec/jenkins.war --httpListenAddress\=127.0.0.1 --httpPort\=7070
def git_ref = params.Git.split('/')
// def rep_name = git_ref[-1].split('.')[0]

pipeline {
    environment {
        PATH="/opt/homebrew/bin/:/usr/local/go/bin/:/usr/local/bin/:${env.PATH}"
    }

    // TODO: MacOS Jenkins can't refer to Mac docker when using agent{docker} 
    // agent {
    //     docker {
    //         image 'axidex/devsecops:latest'
    //     }
    // }
    //agent { dockerfile true }
    agent any

    stages {
        stage('SCM') {
            steps {
                echo 'SCM..'
                
                sh 'git clone ' + params.Git // https://github.com/0c34/govwa
                sh 'mv ' + git_ref[-1] + ' src'
            }
        }

        stage('SBOM') {
            steps {
                echo 'SBOM..'

                // https://github.com/CycloneDX/cyclonedx-gomod
                sh 'wget https://github.com/CycloneDX/cyclonedx-gomod/releases/download/v1.4.1/cyclonedx-gomod_1.4.1_linux_arm64.tar.gz'
                sh 'tar -xvzf cyclonedx-gomod_1.4.1_linux_arm64.tar.gz'
                sh './cyclonedx-gomod app -output ./sbom.xml src'
            }
        }

        stage('SCA') {
            steps {
                echo 'SCA..'

                // Helpful video https://youtu.be/3_25Itx1wmI?si=0vX02xDc1Hyp0bF7
                // https://www.jenkins.io/doc/pipeline/steps/dependency-track/                                                                    // flags for interrupt
                dependencyTrackPublisher artifact: 'sbom.xml', projectName: 'tmp', projectVersion: '0.1', synchronous: true, autoCreateProjects: true //, failedTotalCritical: 1, failedTotalHigh: 10, failedTotalMedium: 20                
            }
        }

        stage('Results') {
            steps {
                echo 'Results..'

                sh 'python3 logger.py'
                sh 'cat vuln.log'
                
                // docker cp container_id:path path. If u need tech logs from dependency-tracker in ur jenkins cli
                // sh 'docker cp a6c78433e9faf908b2bdd7eddc2a9f7724c258828af53f97c6611c336f104cc8:/data/.dependency-track/dependency-track.log /Users/axidex/.jenkins/workspace/pipe1/dependency-track.log'
                // sh 'cat dependency-track.log'
            }
        }
    }
    
    post {
        // Clean after build
        always {
                cleanWs( patterns: [[pattern: '.log', type: 'EXCLUDE']] )
        }
    }
}